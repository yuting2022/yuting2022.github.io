import re, html, shutil, datetime, json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).parent
CONTENT = ROOT / 'content'
OUT = ROOT / 'docs'
SITE_TITLE = 'Yuting He | Research Notebook'

SOCIAL_LINKS = {
    'x': 'https://x.com/ytinghe?s=11&t=XWACFtYNgirOvXK8ZoiHjw',
    'scholar': 'https://scholar.google.com/citations?user=yOc4yeUAAAAJ&hl=en',
    'cv': '/cv.html',
    'email': 'mailto:yutinghe@utexas.edu',
}

def parse_frontmatter(text):
    meta = {}
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            fm = parts[1]
            body = parts[2].lstrip('\n')
            for line in fm.splitlines():
                if ':' in line:
                    k, v = line.split(':', 1)
                    meta[k.strip()] = v.strip().strip('"')
            return meta, body
    return meta, text

def slugify(s):
    s = s.lower().strip()
    s = re.sub(r'[^a-z0-9\u4e00-\u9fff]+', '-', s)
    return s.strip('-') or 'page'

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\*(.+?)\*', r'<em>\1</em>', s)
    s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', s)
    return s

def md_to_html(md):
    lines = md.splitlines()
    out = []
    in_ul = False
    in_code = False
    code = []
    def close_ul():
        nonlocal in_ul
        if in_ul:
            out.append('</ul>')
            in_ul = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('```'):
            if not in_code:
                close_ul(); in_code = True; code = []
            else:
                out.append('<pre><code>' + html.escape('\n'.join(code)) + '</code></pre>')
                in_code = False
            continue
        if in_code:
            code.append(line); continue
        if stripped.startswith('<') and stripped.endswith('>'):
            close_ul(); out.append(line); continue
        if not stripped:
            close_ul(); continue
        if line.startswith('#'):
            close_ul(); level = len(line) - len(line.lstrip('#'))
            text = line[level:].strip()
            out.append(f'<h{level} id="{slugify(text)}">{inline(text)}</h{level}>')
        elif re.match(r'^[-*]\s+', line):
            if not in_ul:
                out.append('<ul>'); in_ul = True
            out.append('<li>' + inline(re.sub(r'^[-*]\s+', '', line).strip()) + '</li>')
        else:
            close_ul(); out.append('<p>' + inline(line) + '</p>')
    close_ul()
    return '\n'.join(out)

def read_pages():
    pages = []
    for p in CONTENT.rglob('*.md'):
        rel = p.relative_to(CONTENT)
        text = p.read_text(encoding='utf-8')
        meta, body = parse_frontmatter(text)
        title = meta.get('title') or rel.stem.replace('-', ' ').title()
        date = meta.get('date', '')
        tags = [t.strip() for t in meta.get('tags', '').split(',') if t.strip()]
        url = 'index.html' if rel.name == 'index.md' and len(rel.parts) == 1 else str(rel.with_suffix('.html'))
        pages.append({'path': p, 'rel': rel, 'url': url, 'title': title, 'date': date, 'tags': tags, 'body': body, 'meta': meta})
    pages.sort(key=lambda x: (x['date'], x['title']), reverse=True)
    return pages

def top_header():
    return f'''<header class="site-header">
  <div class="site-header-inner">
    <div class="header-spacer"></div>
    <nav class="header-links" aria-label="Profile links">
      <a href="{SOCIAL_LINKS['scholar']}" target="_blank" rel="noopener">Google Scholar</a>
      <a href="{SOCIAL_LINKS['cv']}">CV</a>
      <a href="{SOCIAL_LINKS['email']}">Email</a>
    </nav>
  </div>
</header>'''

def rel_to_url(rel):
    if rel.name == 'index.md':
        if len(rel.parts) == 1:
            return '/index.html'
        return '/' + quote(str(rel.parent / 'index.html'), safe='/')
    return '/' + quote(str(rel.with_suffix('.html')), safe='/')

def breadcrumb_for(pg):
    if pg['url'] == 'index.html':
        return ''
    rel = pg['rel']
    crumbs = [('<span class="crumb-home-script">Yuting He</span>', '/index.html')]
    parts = list(rel.parts)
    # Directories in the path
    dirs = parts[:-1]
    for i, part in enumerate(dirs):
        folder_rel = Path(*dirs[:i+1]) / 'index.md'
        folder_path = CONTENT / folder_rel
        label = part
        if folder_path.exists():
            meta, _ = parse_frontmatter(folder_path.read_text(encoding='utf-8'))
            label = meta.get('title', part)
        crumbs.append((html.escape(label), rel_to_url(folder_rel)))
    # Add current page only for non-index pages
    if rel.name != 'index.md':
        crumbs.append((html.escape(pg['title']), None))
    bits = []
    for i, (label, href) in enumerate(crumbs):
        if href:
            bits.append(f'<a href="{href}">{label}</a>')
        else:
            bits.append(f'<span aria-current="page">{label}</span>')
    return '<nav class="breadcrumbs" aria-label="Breadcrumb">' + '<span class="crumb-sep">/</span>'.join(bits) + '</nav>'

def page_kind(pg):
    if pg['url'] == 'index.html':
        return 'home-page'
    if pg['rel'].name == 'index.md':
        return 'section-page'
    if pg['meta'].get('article_class') == 'reading-note':
        return 'article-page'
    return 'content-page'

def layout(title, body, pg, meta_html=''):
    year = datetime.date.today().year
    kind = page_kind(pg)
    breadcrumb = breadcrumb_for(pg)
    header = '' if kind == 'home-page' else top_header()
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · {SITE_TITLE}</title><meta name="description" content="Research website and notebook of Yuting He, covering AI, political communication, journalism, and computational social science methods."><link rel="stylesheet" href="/assets/style.css?v=28"><script defer src="/assets/search.js?v=11"></script></head><body class="{kind}">{header}<main>{breadcrumb}<div class="utility-row"><div class="search-wrap"><input id="search" placeholder="Search research notes…"></div><button id="theme" aria-label="Toggle dark mode">◐</button></div>{meta_html}<article class="{html.escape(pg['meta'].get('article_class', ''))}">{body}</article><footer>© {year} Yuting He · Research Notebook</footer></main></body></html>'''

def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / 'assets').mkdir(parents=True)
    shutil.copytree(ROOT / 'assets', OUT / 'assets', dirs_exist_ok=True)
    pages = read_pages()
    search = []
    for pg in pages:
        target = OUT / pg['url']
        target.parent.mkdir(parents=True, exist_ok=True)
        show_header = pg['meta'].get('show_header', 'true').lower() != 'false'
        meta_html = ''
        if show_header:
            label = 'Essay' if pg['meta'].get('article_class') == 'reading-note' else 'Section'
            meta_html = f'<header class="pagehead"><p class="page-kicker">{label}</p><h1>{html.escape(pg["title"])}</h1>'
            bits = []
            if pg['date']:
                bits.append(pg['date'])
            if pg['tags']:
                bits.append(' '.join(f'<span class="tag">#{html.escape(t)}</span>' for t in pg['tags']))
            if bits:
                meta_html += '<div class="meta">' + ' · '.join(bits) + '</div>'
            meta_html += '</header>'
        target.write_text(layout(pg['title'], md_to_html(pg['body']), pg, meta_html), encoding='utf-8')
        search.append({'title': pg['title'], 'url': '/' + pg['url'], 'tags': pg['tags'], 'text': re.sub(r'\s+', ' ', pg['body'])[:800]})
    (OUT / 'assets' / 'search-index.json').write_text(json.dumps(search, ensure_ascii=False), encoding='utf-8')
    (OUT / '.nojekyll').write_text('', encoding='utf-8')

if __name__ == '__main__':
    build()
