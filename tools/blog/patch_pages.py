#!/usr/bin/env python3
"""Add a 'Related reading' block, the site link hub and the shared motion layer to the main pages.

Idempotent (fenced with <!-- motion:... --> markers). Run after tools/blog/build.py.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import build  # noqa: E402

build.prepare_bodies()

PAGES = {
    'about.html': ('More about how I work', ['charusat-university-experience', 'game-developer-career-guide', 'mavericks-battlegrounds-game-development-journey', 'getting-started-unity-game-development']),
    'services.html': ('Guides behind the services', ['getting-started-unity-xr', 'multiplayer-games-photon-unity', 'mobile-game-optimization', 'react-vs-nextjs-which-to-choose']),
    'portfolio.html': ('Project write-ups', ['mavericks-battlegrounds-game-development-journey', 'lowxena-game-development-insights', 'charusat-expo-3-mavericks-battlegrounds-showcase', 'multiplayer-games-photon-unity']),
    'Achivemtn.html': ('Stories behind the achievements', ['iit-bombay-techfest-2024-experience', 'hackron-hackathon-2025-blinkit-experience', 'daiict-hackathon-ai-meeting-monitor', 'charusat-expo-3-mavericks-battlegrounds-showcase']),
    'contact.html': ('Read before we talk', ['getting-started-unity-game-development', 'multiplayer-games-photon-unity', 'react-vs-nextjs-which-to-choose', 'game-developer-career-guide']),
}

HEAD = '''<script>(function(d){if(!matchMedia('(prefers-reduced-motion: reduce)').matches){d.classList.add('motion-ok');setTimeout(function(){if(!window.__motionReady)d.classList.remove('motion-ok')},4500)}})(document.documentElement)</script>
  <noscript><style>[data-reveal],[data-kinetic]{opacity:1!important;transform:none!important;clip-path:none!important}</style></noscript>
  <link rel="stylesheet" href="assets/css/blog-post.css">
  <link rel="stylesheet" href="assets/css/motion.css">'''


def fence(name, body):
    return f'<!-- motion:{name} -->\n{body.strip()}\n<!-- /motion:{name} -->'


def put(html, name, body, anchor, where):
    block = fence(name, body)
    pat = re.compile(rf'<!-- motion:{name} -->.*?<!-- /motion:{name} -->', re.S)
    if pat.search(html):
        return pat.sub(lambda m: block, html, count=1)
    m = re.search(anchor, html, re.S)
    if not m:
        return None
    i = m.start() if where == 'before' else m.end()
    return html[:i] + block + '\n  ' + html[i:] if where == 'before' else html[:i] + '\n  ' + block + html[i:]


for page, (title, slugs) in PAGES.items():
    path = os.path.join(ROOT, page)
    raw = open(path, encoding='utf-8', newline='').read()
    crlf = '\r\n' in raw
    html = raw.replace('\r\n', '\n')
    cards = ''.join(build.card_html(s, '') for s in slugs)
    block = f'''<aside class="related-reading" aria-label="Related articles" style="max-width:1200px;margin:3rem auto 0;padding:0 clamp(1.2rem,5vw,3.5rem)">
    <h2 class="block-label">{title}</h2>
    <div class="card-grid">{cards}</div>
    <p style="margin:1.5rem 0 0"><a class="journal-all" href="blog.html">Browse all {len(build.POSTS)} articles &rarr;</a></p>
    {build.link_hub('')}
  </aside>'''
    out = html
    for name, body, anchor in (('head', HEAD, r'</head>'), ('related', block, r'<footer'), ('script', '<script src="assets/js/motion.js" defer></script>', r'</body>')):
        out = put(out, name, body, anchor, 'before')
        if out is None:
            break
    if out is None:
        print('!! anchor missing in', page, '- skipped'); continue
    open(path, 'w', encoding='utf-8', newline='').write(out.replace('\n', '\r\n') if crlf else out)
    print('patched', page)
