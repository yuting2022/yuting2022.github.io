import re, html, shutil, datetime, json
from pathlib import Path

ROOT = Path(__file__).parent
CONTENT = ROOT / 'content'
OUT = ROOT / 'docs'
SITE_TITLE = 'Yuting He | Research Notebook'

CUSTOM_NAV = [
    ('Home', '/index.html', []),
    ('Research Notes', '/Research Notes/index.html', []),
    ('AI & Society', '/AI and Society/index.html', [
        ('Introduction to AI', '/AI and Society/introduction-to-ai.html'),
        ('Human–AI Interaction', '/AI and Society/human-ai-interaction.html'),
        ('AI Effects on Society', '/AI and Society/ai-effects-on-society.html'),
        ('AI, News & Journalism', '/AI and Society/AI News and Journalism/index.html'),
    ]),
    ('Political Communication', '/Political Communication/index.html', []),
    ('Research Tools & Methods', '/Research Tools and Methods/index.html', [
        ('Natural Language Processing', '/Research Tools and Methods/Natural Language Processing NLP/index.html'),
        ('Statistics', '/Research Tools and Methods/Statistics/index.html'),
        ('AI as a Method', '/Research Tools and Methods/AI as a Method/index.html'),
    ]),
]

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

def nav_tree():
    htmls = [f'''<aside class="sidebar">
<a class="profile" href="/index.html" aria-label="Home">
  <img src="/assets/avatar.jpg" alt="Yuting He" class="avatar">
</a>
<nav class="navlinks">''']
    for label, href, children in CUSTOM_NAV:
        if children:
            htmls.append(f'<details open><summary>{label}</summary>')
            for child, chref in children:
                htmls.append(f'<a href="{chref}">{child}</a>')
            htmls.append('</details>')
        else:
            htmls.append(f'<a href="{href}">{label}</a>')
    htmls.append('''</nav>
<div class="sidebar-footer">
  <a href="{x}" aria-label="X / Twitter" title="X / Twitter" target="_blank" rel="noopener">𝕏</a>
  <a href="{scholar}" aria-label="Google Scholar" title="Google Scholar" target="_blank" rel="noopener">Scholar</a>
  <a href="{cv}" aria-label="CV" title="CV">CV</a>
  <a href="{email}" aria-label="Email" title="Email">Email</a>
</div>
</aside>'''.format(**SOCIAL_LINKS))
    return '\n'.join(htmls)

def layout(title, body, nav, meta='', article_class=''):
    year = datetime.date.today().year
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · {SITE_TITLE}</title><link rel="stylesheet" href="/assets/style.css?v=15"><script defer src="/assets/search.js?v=11"></script><!-- GoatCounter analytics: create an account and replace YOUR-CODE below. --><!-- <script data-goatcounter="https://YOUR-CODE.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script> --></head><body>{nav}<main><div class="topbar"><input id="search" placeholder="Search research notes…"><button id="theme" aria-label="Toggle dark mode">◐</button></div>{meta}<article class="{html.escape(article_class)}">{body}</article><footer>© {year} Yuting He · Research Notebook</footer></main></body></html>'''

def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / 'assets').mkdir(parents=True)
    shutil.copytree(ROOT / 'assets', OUT / 'assets', dirs_exist_ok=True)
    pages = read_pages()
    nav = nav_tree()
    search = []
    for pg in pages:
        target = OUT / pg['url']
        target.parent.mkdir(parents=True, exist_ok=True)
        show_header = pg['meta'].get('show_header', 'true').lower() != 'false'
        meta_html = ''
        if show_header:
            header_class = "pagehead article-pagehead" if pg['meta'].get('article_class') == 'reading-note' else "pagehead"
            meta_html = f'<header class="{header_class}"><h1>{html.escape(pg["title"])}</h1>'
            bits = []
            if pg['date']:
                bits.append(pg['date'])
            if pg['tags']:
                bits.append(' '.join(f'<span class="tag">#{html.escape(t)}</span>' for t in pg['tags']))
            if bits:
                meta_html += '<div class="meta">' + ' · '.join(bits) + '</div>'
            meta_html += '</header>'
        target.write_text(layout(pg['title'], md_to_html(pg['body']), nav, meta_html, pg['meta'].get('article_class', '')), encoding='utf-8')
        search.append({'title': pg['title'], 'url': '/' + pg['url'], 'tags': pg['tags'], 'text': re.sub(r'\s+', ' ', pg['body'])[:800]})
    (OUT / 'assets' / 'search-index.json').write_text(json.dumps(search, ensure_ascii=False), encoding='utf-8')

if __name__ == '__main__':
    build()
