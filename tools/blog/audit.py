"""Audit generated pages: broken local links/assets, duplicate ids, missing alts, h1 count, JSON-LD validity."""
import glob, json, os, re, sys
from urllib.parse import urlparse, unquote
from bs4 import BeautifulSoup
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
pages = ['blog.html', 'index.html'] + sorted(glob.glob(os.path.join(ROOT, 'blog', '*.html')) + glob.glob(os.path.join(ROOT, 'blog', 'topics', '*.html')))
bad = 0
for p in pages:
    path = p if os.path.isabs(p) else os.path.join(ROOT, p)
    soup = BeautifulSoup(open(path, encoding='utf-8').read(), 'html.parser')
    issues = []
    ids = [e['id'] for e in soup.find_all(id=True)]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup: issues.append(f'dup ids {sorted(dup)[:5]}')
    if len(soup.find_all('h1')) != 1 and 'index.html' not in path: issues.append(f'h1 count {len(soup.find_all("h1"))}')
    noalt = [i.get('src') for i in soup.find_all('img') if not (i.get('alt') or '').strip()]
    if noalt: issues.append(f'{len(noalt)} imgs without alt')
    for tag, attr in (('a', 'href'), ('img', 'src'), ('link', 'href'), ('script', 'src'), ('source', 'src')):
        for e in soup.find_all(tag, **{attr: True}):
            u = e[attr]
            if re.match(r'^(https?:|//|mailto:|tel:|data:|javascript:|#)', u) or not u: 
                if u.startswith('#') and len(u) > 1 and not soup.find(id=u[1:]): issues.append(f'dead anchor {u}')
                continue
            t = unquote(urlparse(u).path)
            if not t: continue
            target = os.path.normpath(os.path.join(os.path.dirname(path), t))
            if not os.path.exists(target): issues.append(f'missing {tag} {u}')
    for s in soup.find_all('script', type='application/ld+json'):
        try: json.loads(s.string)
        except Exception as ex: issues.append(f'bad json-ld: {ex}')
    if issues:
        bad += 1; print(os.path.relpath(path, ROOT)); [print('   -', i) for i in sorted(set(issues))[:12]]
print('pages audited:', len(pages), '| pages with issues:', bad)
