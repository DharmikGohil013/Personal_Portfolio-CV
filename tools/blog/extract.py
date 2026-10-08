"""One-time migration: pull article body fragments out of the legacy blog posts.

Output: tools/blog/posts/<slug>.html (clean body fragment, headings promoted one
level so the page <h1> is the only h1) and tools/blog/extracted.json (title/cover).
Run from the repository root. Reads the legacy pages from the pre-migration commit
(LEGACY_REV) so it still works after build.py has regenerated blog/*.html.
"""
import json, os, re, subprocess, sys
from bs4 import BeautifulSoup, NavigableString

LEGACY_REV = 'e4b4507'
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'tools', 'blog', 'posts')
os.makedirs(OUT, exist_ok=True)

slugs = subprocess.check_output(['git', 'ls-tree', '--name-only', LEGACY_REV, 'blog/'], cwd=ROOT, text=True).split()
meta = {}
PROMOTE = {'h3': 'h2', 'h4': 'h3', 'h5': 'h4', 'h6': 'h5'}

for path in slugs:
    if not path.endswith('.html'):
        continue
    slug = os.path.basename(path)[:-5]
    raw = subprocess.check_output(['git', 'show', LEGACY_REV + ':' + path], cwd=ROOT).decode('utf-8', 'replace')
    soup = BeautifulSoup(raw, 'html.parser')
    art = soup.select_one('article.article')
    title = art.select_one('h2.title').get_text(' ', strip=True)
    cover = art.select_one('.post-img img')
    content = art.select_one('div.content')

    for el in content.select('script, style'):
        el.decompose()
    for el in content.find_all(True):
        for attr in ('style', 'data-aos', 'data-aos-delay', 'data-aos-duration', 'onclick'):
            el.attrs.pop(attr, None)
    # Heading levels: page h1 = title, article sections = h2
    for h in content.find_all(['h6', 'h5', 'h4', 'h3']):
        h.name = PROMOTE[h.name]
    html = content.decode_contents()
    html = html.replace('\ufffd', '—')
    html = re.sub(r'\s+—\s+', ' — ', html)
    open(os.path.join(OUT, slug + '.html'), 'w', encoding='utf-8', newline='\n').write(html.strip() + '\n')
    meta[slug] = {
        'title': title.replace('\ufffd', '—'),
        'cover': cover['src'] if cover else None,
        'cover_alt': cover.get('alt') if cover else None,
    }
    print(slug, len(html))

json.dump(meta, open(os.path.join(ROOT, 'tools', 'blog', 'extracted.json'), 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
