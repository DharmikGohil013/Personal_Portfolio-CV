#!/usr/bin/env python3
"""Idempotently patch index.html with the motion layer and internal-link sections.

Inserted blocks are fenced with <!-- motion:NAME --> ... <!-- /motion:NAME --> so re-running
replaces them instead of duplicating. Run after tools/blog/build.py.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import build  # noqa: E402
from content import POSTS, TOPICS  # noqa: E402

build.prepare_bodies()
PATH = os.path.join(ROOT, 'index.html')
src = open(PATH, encoding='utf-8', newline='').read()
crlf = '\r\n' in src
html = src.replace('\r\n', '\n')


def fence(name, body):
    return f'<!-- motion:{name} -->\n{body.strip()}\n<!-- /motion:{name} -->'


def put(html, name, body, anchor_regex, where):
    """Insert (or replace) a fenced block before/after the anchor match."""
    block = fence(name, body)
    pat = re.compile(rf'<!-- motion:{name} -->.*?<!-- /motion:{name} -->', re.S)
    if pat.search(html):
        return pat.sub(lambda m: block, html, count=1)
    m = re.search(anchor_regex, html, re.S)
    if not m:
        raise SystemExit(f'anchor not found for {name}: {anchor_regex}')
    i = m.start() if where == 'before' else m.end()
    return html[:i] + ('' if where == 'before' else '\n    ') + block + ('\n    ' if where == 'before' else '') + html[i:]


# ------------------------------------------------------------------ head
head_block = '''<script>(function(d){if(!matchMedia('(prefers-reduced-motion: reduce)').matches){d.classList.add('motion-ok');setTimeout(function(){if(!window.__motionReady)d.classList.remove('motion-ok')},4500)}})(document.documentElement)</script>
  <noscript><style>[data-reveal],[data-kinetic]{opacity:1!important;transform:none!important;clip-path:none!important}</style></noscript>
  <link rel="stylesheet" href="assets/css/blog-post.css">
  <link rel="stylesheet" href="assets/css/motion.css">
  <link rel="alternate" type="application/rss+xml" title="Dharmik Gohil – Blog" href="https://dharmikgohil.art/feed.xml">'''
html = put(html, 'head', head_block, r'</head>', 'before')

# hero headline: kinetic type
html = html.replace('<h2 class="hero-editorial-headline">', '<h2 class="hero-editorial-headline" data-kinetic>', 1)

# ------------------------------------------------------------------ ticker
words = ['Unity 6', 'C#', 'Photon PUN', 'AR Foundation', 'XR Toolkit', 'Oculus SDK', 'React', 'Node.js', 'MongoDB', 'WebSockets', 'ERPNext', 'n8n', 'Web3']
lis = ''.join(f'<li{" class=alt" if i % 3 == 2 else ""}>{w}</li>' for i, w in enumerate(words))
ticker = f'''<div class="ticker" role="marquee" aria-label="Technologies I work with">
      <div class="ticker-track"><ul>{lis}</ul><ul aria-hidden="true">{lis}</ul></div>
    </div>'''
html = put(html, 'ticker', ticker, r'<section id="hero".*?</section>', 'after')

# ------------------------------------------------------------------ orbit
def chip(label, href=None, icon=None):
    i = f'<i class="bi {icon}"></i>' if icon else ''
    return f'<a class="orbit-chip" href="{href}">{i}{label}</a>' if href else f'<span class="orbit-chip">{i}{label}</span>'

def node(a, c):
    return f'<div class="orbit-node" style="--a:{a}deg">{c}</div>'

r1 = [chip('Unity', 'blog/topics/unity-game-development.html', 'bi-controller'), chip('XR', 'blog/topics/xr-vr-ar-development.html', 'bi-badge-vr'), chip('Multiplayer', 'blog/topics/multiplayer-game-development.html', 'bi-people-fill')]
r2 = [chip('C#', None, 'bi-braces'), chip('Photon PUN', 'blog/multiplayer-games-photon-unity.html'), chip('AR Foundation', 'blog/getting-started-unity-xr.html'), chip('WebSockets', 'blog/lowxena-game-development-insights.html')]
r3 = [chip('React', 'blog/react-vs-nextjs-which-to-choose.html', 'bi-code-slash'), chip('Node.js'), chip('MongoDB'), chip('Git &amp; GitHub', 'blog/git-github-essential-commands.html'), chip('ERPNext')]
ring = lambda cls, chips, off: f'<div class="orbit-ring {cls}">' + ''.join(node(off + k * 360 // len(chips), c) for k, c in enumerate(chips)) + '</div>'
orbit = f'''<section id="stack-orbit" class="orbit-section section" aria-labelledby="orbit-h" style="border-bottom: 2px solid var(--ink) !important;">
      <div class="container section-title">
        <h2 id="orbit-h">The Stack, In Orbit</h2>
        <p>What I build with &middot; hover to pause &middot; tap a node to go deeper</p>
      </div>
      <div class="orbit-grid">
        <div class="orbit-copy">
          <p>Games and web products share a spine: real-time state, fast feedback and ruthless performance budgets. I work from the engine (Unity and C#) out to the network layer (Photon PUN, WebSockets) and up to the web stack (React, Node.js, MongoDB).</p>
          <p>Each node on the diagram links to an article or topic hub where I explain how I use it on real projects.</p>
          <ul>
            <li><a href="blog/topics/unity-game-development.html"><i class="bi bi-controller"></i><span>Unity game development</span><i class="bi bi-arrow-right"></i></a></li>
            <li><a href="blog/topics/xr-vr-ar-development.html"><i class="bi bi-badge-vr"></i><span>AR, VR &amp; XR development</span><i class="bi bi-arrow-right"></i></a></li>
            <li><a href="blog/topics/multiplayer-game-development.html"><i class="bi bi-people-fill"></i><span>Multiplayer &amp; networking</span><i class="bi bi-arrow-right"></i></a></li>
            <li><a href="services.html"><i class="bi bi-briefcase"></i><span>Services &amp; pricing</span><i class="bi bi-arrow-right"></i></a></li>
          </ul>
        </div>
        <figure class="orbit" aria-label="Diagram of core technologies orbiting a core of XR, games and web">
          <span class="orbit-pulse"></span><span class="orbit-pulse"></span><span class="orbit-pulse"></span>
          {ring('r3', r3, 20)}{ring('r2', r2, 45)}{ring('r1', r1, 90)}
          <div class="orbit-core"><span>XR<br>GAMES<br>WEB</span></div>
        </figure>
      </div>
    </section>'''
html = put(html, 'orbit', orbit, r'<section id="explore".*?</section>', 'after')

# ------------------------------------------------------------------ process
steps = [
    ('Discover', 'Scope the platform, the audience and the single mechanic that has to feel great.', ['Scope', 'Platform', 'Core loop']),
    ('Prototype', 'A playable greybox early, so decisions are made on feel instead of slides.', ['Greybox', 'Playtest', 'Iterate']),
    ('Build', 'Unity and C# or the MERN stack, networked with Photon or WebSockets and profiled on real devices.', ['Unity', 'MERN', 'Netcode']),
    ('Ship', 'Store builds, WebGL or web deploys, then monitoring and post-launch fixes.', ['Release', 'Monitor', 'Support']),
]
li = ''.join(f'<li><h3>{t}</h3><p>{d}</p><div class="tools">' + ''.join(f'<span>{x}</span>' for x in tl) + '</div></li>' for t, d, tl in steps)
process = f'''<section id="process" class="process section" aria-labelledby="process-h" style="border-bottom: 2px solid var(--ink) !important;">
      <div class="container section-title">
        <h2 id="process-h">How A Build Ships</h2>
        <p>From brief to launch in four moves</p>
      </div>
      <ol class="pipeline">{li}</ol>
      <p style="margin-top:2.2rem;font:700 11px/1.6 var(--font-mono);letter-spacing:.16em;text-transform:uppercase"><a href="contact.html" class="cta-link">Start a project <span class="arrow">&rarr;</span></a> &nbsp; <a href="services.html" class="cta-link">See services <span class="arrow">&rarr;</span></a> &nbsp; <a href="portfolio.html" class="cta-link">View portfolio <span class="arrow">&rarr;</span></a></p>
    </section>'''
html = put(html, 'process', process, r'<section id="resume".*?</section>', 'after')

# ------------------------------------------------------------------ journal (latest posts)
newest = sorted(POSTS, key=lambda s: POSTS[s]['date'], reverse=True)[:6]
cards = ''.join(build.card_html(s, '') for s in newest)
topics = ''.join(f'<li><a href="blog/topics/{k}.html"><i class="bi {v["icon"]}"></i> {v["short"]}</a></li>' for k, v in TOPICS.items())
journal = f'''<section id="journal" class="journal section" aria-labelledby="journal-h" style="border-bottom: 2px solid var(--ink) !important;">
      <div class="container section-title">
        <div class="journal-head"><div><h2 id="journal-h">Field Notes</h2><p>Latest articles on Unity, XR, multiplayer and full-stack</p></div><a class="journal-all" href="blog.html">All {len(POSTS)} articles &rarr;</a></div>
      </div>
      <ul class="topic-nav" aria-label="Blog topics" style="margin-top:1rem">{topics}</ul>
      <div class="card-grid">{cards}</div>
    </section>'''
html = put(html, 'journal', journal, r'<section id="contact"', 'before')

# ------------------------------------------------------------------ link hub (footer directory)
hub = '<div class="main">' + build.link_hub('') + '</div>'
html = put(html, 'linkhub', hub, r'<footer class="container">', 'before')

# ------------------------------------------------------------------ design: client showcase + Gain Live card (legacy neon styles -> ink/paper)
def swap(html, name, body, original_regex):
    block = fence(name, body)
    fenced = re.compile(rf'<!-- motion:{name} -->.*?<!-- /motion:{name} -->', re.S)
    if fenced.search(html):
        return fenced.sub(lambda m: block, html, count=1)
    orig = re.compile(original_regex, re.S)
    if not orig.search(html):
        raise SystemExit(f'original block not found for {name}')
    return orig.sub(lambda m: block, html, count=1)

clients = '''<section id="clients" class="clients section" aria-labelledby="clients-h" style="border-bottom: 2px solid var(--ink) !important;">
      <div class="container section-title">
        <h2 id="clients-h">Global Client Showcase</h2>
        <p>International client projects &amp; enterprise partnerships</p>
      </div>
      <article class="client-feature" data-reveal>
        <div class="client-logo"><img src="assets/img/clients/gain-live-logo.png" alt="Gain Live Bangladesh client logo" width="1024" height="1024" loading="lazy"></div>
        <div class="client-body">
          <span class="client-badge">🇧🇩 International client &middot; Bangladesh</span>
          <h3>Gain Live</h3>
          <p class="client-tagline">&ldquo;Play smart. Win big.&rdquo;</p>
          <p>Custom gaming platform engineered for our Bangladesh client. Includes custom UI/UX design, real-time gaming mechanics, player telemetry systems, and responsive cross-device optimization.</p>
          <div class="d-flex flex-wrap gap-2">
            <span class="skill-tag solid">iGAMING PLATFORM</span>
            <span class="skill-tag hollow">REAL-TIME MECHANICS</span>
            <span class="skill-tag red-border">CROSS-DEVICE UI/UX</span>
          </div>
          <p class="client-cta"><a href="contact.html" class="cta-link">Start a similar project <span class="arrow">&rarr;</span></a></p>
        </div>
      </article>
    </section>'''
html = swap(html, 'clients', clients, r'<section id="clients".*?</section>')

gain = '''<div class="portfolio-item filter-client filter-product filter-app3d filter-appmobile filter-app work-card work-card--client" style="cursor: default;">
            <div class="work-card-image work-card-image--logo">
              <img src="assets/img/clients/gain-live-logo.png" alt="Gain Live Bangladesh client project logo" loading="lazy" width="1024" height="1024">
              <span class="work-number">CLIENT</span>
            </div>
            <div class="work-card-content">
              <div class="work-card-header">
                <h3 class="work-title">Gain Live</h3>
                <span class="work-arrow">🇧🇩 BANGLADESH</span>
              </div>
              <p class="work-desc">Custom gaming platform engineered for our Bangladesh client: UI/UX, real-time gaming mechanics, player telemetry and cross-device optimization.</p>
              <div class="work-meta">
                <span class="skill-tag solid">GAIN LIVE</span>
                <span class="skill-tag hollow">BANGLADESH CLIENT</span>
                <span class="skill-tag red-border">★ CLIENT PROJECT</span>
              </div>
            </div>
          </div>'''
html = swap(html, 'gainlive', gain, r'<div class="portfolio-item filter-client[^>]*>\s*<div class="work-card-image" style="background: radial-gradient.*?</div>\s*</div>\s*</div>\s*(?=<!-- Row 01)')

# videos: valid attributes, lighter first load, posters where a cover exists
POSTERS = {'mavericks-battleground.mp4': 'assets/img/portfolio/mavericks-battleground-thumbnail.jpg', 'hook-shot.mp4': 'assets/img/portfolio/hookshot-cover.webp', 'just-divide.mp4': 'assets/img/portfolio/just-divide-cover.webp'}
def fix_video(m):
    label, srcline = m.group(1), m.group(2)
    name = os.path.basename(re.search(r'src="([^"]+)"', srcline).group(1))
    poster = f' poster="{POSTERS[name]}"' if name in POSTERS else ''
    return f'<video autoplay loop muted playsinline preload="metadata" aria-label="{label}"{poster}>{srcline}'
html = re.sub(r'<video autoplay loop muted playsinline alt="([^"]*)">(\s*<source[^>]*>)', fix_video, html)

# ------------------------------------------------------------------ scripts
html = put(html, 'script', '<script src="assets/js/motion.js" defer></script>', r'<script src="assets/js/global-multilingual\.js" defer></script>', 'before')

out = html.replace('\n', '\r\n') if crlf else html
open(PATH, 'w', encoding='utf-8', newline='').write(out)
print('index.html patched; crlf =', crlf)
