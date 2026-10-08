#!/usr/bin/env python3
"""HTML sitemap blog section, robots.txt tooling rule and homepage ItemList JSON-LD. Idempotent."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import build  # noqa: E402
from content import POSTS, TOPICS, SITE  # noqa: E402
build.prepare_bodies()


def rw(path, fn):
    raw = open(path, encoding='utf-8', newline='').read()
    crlf = '\r\n' in raw
    out = fn(raw.replace('\r\n', '\n'))
    open(path, 'w', encoding='utf-8', newline='').write(out.replace('\n', '\r\n') if crlf else out)


def fenced(name, body, html, anchor):
    block = f'<!-- motion:{name} -->\n{body}\n<!-- /motion:{name} -->'
    pat = re.compile(rf'<!-- motion:{name} -->.*?<!-- /motion:{name} -->', re.S)
    if pat.search(html):
        return pat.sub(lambda m: block, html, count=1)
    i = html.index(anchor)
    return html[:i] + block + '\n    ' + html[i:]


# 1. HTML sitemap: topic hubs + every article
def sitemap_page(html):
    items = lambda rows: ''.join(f'<div class="link-item"><a href="{u}">{t}</a><div class="link-description">{d}</div></div>' for t, u, d in rows)
    hubs = [(v['name'], f'/blog/topics/{k}.html', v['intro']) for k, v in TOPICS.items()]
    posts = [(build.EXTRACTED[s]['title'], f'/blog/{s}.html', POSTS[s]['description']) for s in sorted(POSTS, key=lambda s: POSTS[s]['date'], reverse=True)]
    body = (f'<div class="section"><h2>Blog Topics</h2><div class="links">{items(hubs)}</div></div>\n'
            f'    <div class="section"><h2>Blog Articles</h2><div class="links">{items(posts)}</div></div>')
    return fenced('blog-sitemap', body, html, '<div class="section">\n      <h2>Featured Projects</h2>')


rw(os.path.join(ROOT, 'sitemap-page.html'), sitemap_page)

# 2. robots.txt: keep build tooling and article source fragments out of the index
def robots(txt):
    if 'Disallow: /tools/' in txt:
        return txt
    return txt.replace('Disallow: /forms/\n', 'Disallow: /forms/\nDisallow: /tools/\n', 1)


rw(os.path.join(ROOT, 'robots.txt'), robots)

# 3. Homepage: ItemList of the newest articles (helps discovery of the blog from the root)
def index_ld(html):
    newest = sorted(POSTS, key=lambda s: POSTS[s]['date'], reverse=True)[:8]
    ld = {'@context': 'https://schema.org', '@type': 'ItemList', 'name': 'Latest articles by Dharmik Gohil', 'url': SITE + '/blog.html',
          'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': build.post_url(s), 'name': build.EXTRACTED[s]['title']} for i, s in enumerate(newest)]}
    body = '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False, separators=(',', ':')) + '</script>'
    return fenced('ld-journal', body, html, '</head>')


rw(os.path.join(ROOT, 'index.html'), index_ld)
print('misc patched')
