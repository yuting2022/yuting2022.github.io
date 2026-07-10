# Yuting He | Research Notebook

A lightweight academic homepage + research-notebook website for GitHub Pages.

## Local preview

From this folder, run:

```bash
python build.py
cd docs
python -m http.server 8080
```

Then open:

```text
http://localhost:8080
```

When you edit Markdown files in `content/`, go back to the project folder and run:

```bash
python build.py
```

Then refresh the browser.

## Edit content

Write Markdown files inside `content/`. Main sections are:

- `content/Research Notes/`
- `content/AI and Society/`
- `content/Political Communication/`
- `content/Research Tools and Methods/`

## Deploy on GitHub Pages

1. Create a GitHub repository.
2. Upload all files in this folder.
3. Go to **Settings → Pages**.
4. Choose **Deploy from a branch**.
5. Select branch `main`, folder `/docs`.

## Analytics

Create a GoatCounter account, then edit `build.py` and replace the GoatCounter placeholder with your code.
