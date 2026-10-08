#!/usr/bin/env python3
"""Static blog builder.

Renders blog/<slug>.html (every article), blog/topics/<topic>.html (topic hubs)
and blog.html (index) from:
  - tools/blog/posts/<slug>.html   article body fragments
  - tools/blog/content.py          SEO titles, descriptions, FAQs, topics, links

Run from anywhere:  python tools/blog/build.py
Also rewrites sitemap.xml blog entries and llms.txt blog section.
"""
import html, json, math, os, re, sys
from datetime import date
from bs4 import BeautifulSoup, NavigableString

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
from content import SITE, TODAY, TOPICS, POSTS  # noqa: E402

EXTRACTED = json.load(open(os.path.join(HERE, 'extracted.json'), encoding='utf-8'))
esc = html.escape
for _slug, _p in POSTS.items():
    if _p.get('cover'):
        EXTRACTED[_slug]['cover'] = _p['cover']

PERSON = {
    '@type': 'Person', '@id': SITE + '/#person', 'name': 'Dharmik Gohil', 'url': SITE + '/',
    'jobTitle': 'Unity Game Developer & XR Engineer',
    'sameAs': ['https://github.com/DharmikGohil013', 'https://www.linkedin.com/in/dharmikgohil086/',
               'https://x.com/Dharmik086', 'https://dharmikgohil.itch.io/'],
}
PUBLISHER = {'@type': 'Organization', 'name': 'Dharmik Gohil', 'url': SITE + '/',
             'logo': {'@type': 'ImageObject', 'url': SITE + '/assets/img/logo.png'}}

SKIP_PARENTS = {'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'code', 'pre', 'script', 'style', 'button', 'summary', 'figcaption', 'th'}
SKIP_CLASSES = {'code-block', 'code-label', 'tech-badge', 'stat-box', 'gallery-caption', 'cta-bar'}


# ----------------------------------------------------------------- helpers
def abs_url(src, base_depth=1):
    if not src:
        return SITE + '/assets/img/dharmik-profile-photo-2026.jpg'
    if src.startswith('http'):
        return src
    return SITE + '/' + re.sub(r'^(\.\./)+', '', src)


def slugify(text):
    s = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
    return s[:60] or 'section'


def fmt_date(iso):
    d = date.fromisoformat(iso)
    return d.strftime('%b %d, %Y').replace(' 0', ' ')


def post_url(slug):
    return f'{SITE}/blog/{slug}.html'


def topic_url(t):
    return f'{SITE}/blog/topics/{t}.html'


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(',', ':')) + '</script>'


def trunc(s, n):
    return s if len(s) <= n else s[:n - 1].rsplit(' ', 1)[0] + '…'


# ----------------------------------------------------------------- article processing
def process_fragment(slug, raw, meta):
    soup = BeautifulSoup(raw, 'html.parser')
    title = meta['title']

    # headings -> ids + TOC
    toc, seen = [], set()
    for h in soup.find_all('h2'):
        text = h.get_text(' ', strip=True)
        base = slugify(text)
        sid, n = base, 2
        while sid in seen:
            sid, n = f'{base}-{n}', n + 1
        seen.add(sid)
        h['id'] = sid
        toc.append((sid, text))

    # drop images whose files are not in the repo (they would render as broken icons)
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if src and not re.match(r'^(https?:|//|data:)', src) and not os.path.exists(os.path.normpath(os.path.join(ROOT, 'blog', src))):
            print(f'  [warn] {slug}: removed missing image {src}')
            (img.find_parent(class_='gallery-item') or img).decompose()
    for grid in soup.select('.gallery-grid'):
        if not grid.find('img'):
            sec = grid.find_parent(class_='image-gallery-section')
            prev = (sec or grid).find_previous_sibling(['h2', 'h3'])
            (sec or grid).decompose()
            if prev is not None and prev.find_next_sibling() is None:
                prev.decompose()

    # images: alt text, lazy loading, lightbox wrappers
    for i, img in enumerate(soup.find_all('img'), 1):
        if not (img.get('alt') or '').strip():
            cap = img.find_next('div', class_='gallery-caption')
            alt = cap.get_text(' ', strip=True) if cap and cap.find_previous('img') is img else f'{title} – image {i}'
            img['alt'] = alt
        img['loading'] = 'lazy'
        img['decoding'] = 'async'
        img.attrs.pop('title', None)
        item = img.find_parent(class_='gallery-item')
        if item and img.parent.name != 'a':
            a = soup.new_tag('a', href=img['src'], attrs={'class': 'glightbox', 'data-gallery': 'post', 'data-title': img['alt']})
            img.wrap(a)

    # outbound links
    for a in soup.find_all('a', href=True):
        if a['href'].startswith('http') and 'dharmikgohil.art' not in a['href']:
            a['rel'] = 'noopener'
            a['target'] = '_blank'
        if a['href'].startswith('//'):
            a['rel'] = 'noopener'
    for f in soup.find_all('iframe'):
        f['loading'] = 'lazy'
        f.attrs.pop('style', None)
        if not f.get('title'):
            f['title'] = 'Embedded video – ' + title

    # contextual internal links (first whole-word occurrence per target)
    linked = 0
    used_targets = {a['href'] for a in soup.find_all('a', href=True)}
    pairs = list(POSTS[slug].get('links', [])) + [('Dharmik Gohil', 'page:about.html'), ('portfolio', 'page:portfolio.html')]
    for text, target in pairs:
        if target.startswith('page:'):
            href, ttl = '../' + target[5:], None
        else:
            href, ttl = f'{target}.html', EXTRACTED[target]['title']
            if target == slug:
                continue
        if href in used_targets:
            continue
        pat = re.compile(r'(?<![\w-])' + re.escape(text) + r'(?![\w-])')
        done = False
        for node in soup.find_all(string=True):
            if done:
                break
            m = pat.search(node) if isinstance(node, NavigableString) else None
            if not m:
                continue
            parents = [p for p in node.parents if p.name]
            if any(p.name in SKIP_PARENTS | {'blockquote'} for p in parents):
                continue
            if any(set(p.get('class') or []) & SKIP_CLASSES for p in parents):
                continue
            before, after = node[:m.start()], node[m.end():]
            a = soup.new_tag('a', href=href)
            if ttl:
                a['title'] = ttl
            a.string = m.group(0)
            node.replace_with(before, a, after)
            used_targets.add(href)
            linked += 1
            done = True
    return str(soup), toc, linked


def article_text_words(body_html):
    return len(BeautifulSoup(body_html, 'html.parser').get_text(' ', strip=True).split())


# ----------------------------------------------------------------- shared chrome
def nav_html(prefix, active):
    def a(href, label, key=None):
        cls = ' class="active"' if key and key == active else ''
        return f'<a href="{prefix}{href}"{cls}>{label}</a>'
    games = ''.join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in [
        ('MAVERICKS BATTLEGROUND', 'https://dharmikgohil.itch.io/mavericks-battlegrounds'), ('FLOPPY BIRD', 'https://dharmik086.itch.io/floppy-bird-860'),
        ('FACADE', 'https://dharmikgohil.itch.io/facade'), ('GO GALAXY', 'https://dharmikgohil.itch.io/go-galaxy'),
        ('DRONE TRAINING', 'https://dharmikgohil.itch.io/drone-training'), ('HOOK SHOT', 'https://dharmikgohil.itch.io/hook-shot'),
        ('LOWXENA', 'https://lowxena.dharmikgohil.art/')])
    live = (f'<a href="{prefix}assets/Fit Sync.apk" download>FITSYNC APP (APK)</a>' + ''.join(
        f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in [
            ('ACTIFY', 'https://actify.dharmikgohil.art/'), ('LEARN LINK', 'https://learnlink.dharmikgohil.art'),
            ('GDGS GAMES', 'http://gdgs.dharmikgohil.art/'), ('FLIPKART CLONE', 'http://flipcart.dharmikgohil.art/'),
            ('KRISHNA CONSTRUCTION', 'http://krishna.dharmikgohil.art/'), ('WIFI SERVICE', 'https://fkm.vercel.app/')]))
    resume = f'<a href="{prefix}assets/img/Dharmik Gohil Game Desginer.pdf" target="_blank" rel="noopener">RESUME</a>'
    itch = open(os.path.join(HERE, 'itch.svg'), encoding='utf-8').read()
    social = ('<a href="https://github.com/DharmikGohil013" target="_blank" rel="noopener" aria-label="GitHub"><i class="bi bi-github"></i></a>'
              '<a href="https://www.linkedin.com/in/dharmikgohil086/" target="_blank" rel="noopener" aria-label="LinkedIn"><i class="bi bi-linkedin"></i></a>'
              '<a href="https://x.com/Dharmik086" target="_blank" rel="noopener" aria-label="Twitter / X"><i class="bi bi-twitter-x"></i></a>'
              '<a href="https://dharmikgohil.itch.io/" target="_blank" rel="noopener" aria-label="Itch.io">' + itch + '</a>')
    drawer = f'''
  <div class="masthead-mobile-drawer" id="mobileDrawer">
    <div class="drawer-header"><div class="drawer-title">THE DHARMIK GOHIL CHRONICLE</div><button class="drawer-close-btn" id="closeDrawerBtn">✕ CLOSE</button></div>
    <div class="drawer-body">
      <nav class="drawer-nav-links" aria-label="Mobile">
        {a('index.html', 'HOME')}{a('services.html', 'ABILITIES')}
        <div class="drawer-accordion"><button class="drawer-accordion-trigger">MY GAMES <span class="accordion-arrow">▼</span></button><div class="drawer-accordion-content">{games}</div></div>
        <div class="drawer-accordion"><button class="drawer-accordion-trigger">LIVE PROJECTS <span class="accordion-arrow">▼</span></button><div class="drawer-accordion-content">{live}</div></div>
        {a('Achivemtn.html', 'ACHIEVEMENTS')}{a('blog.html', 'BLOG', 'blog')}{a('contact.html', 'CONTACT')}{resume}
      </nav>
      <div class="drawer-footer"><div class="drawer-social-links">{social}</div><div class="drawer-edition">SURAT, INDIA · EST. 2006</div></div>
    </div>
  </div>
  <div class="masthead-drawer-overlay" id="drawerOverlay"></div>'''
    header = f'''
    <header class="masthead container">
      <div class="masthead-top">
        <div>EST. 2006 · SURAT, GUJARAT, INDIA · \U0001f310 GLOBAL REMOTE <button type="button" class="masthead-lang-trigger" aria-label="Choose from 200+ Languages">\U0001f310 200+ LANGUAGES</button></div>
        <div class="text-end">VOL. 1.0 · THE DHARMIK GOHIL CHRONICLE</div>
      </div>
      <div class="masthead-main"><a href="{prefix}index.html" class="masthead-home" aria-label="Dharmik Gohil – home"><span class="masthead-wordmark">Dh<span class="accent-text">a</span>rmik Gohil</span></a></div>
      <div class="masthead-nav-bar">
        <button class="mobile-menu-toggle-brutalist" id="menuToggleBtn" aria-label="Toggle Navigation">MENU ☰</button>
        <nav class="nav-links" aria-label="Primary">
          {a('index.html', 'HOME')} · {a('services.html', 'ABILITIES')} ·
          <div class="nav-dropdown"><span class="dropdown-trigger">MY GAMES <span class="arrow-down">▼</span></span><div class="dropdown-content">{games}</div></div> ·
          <div class="nav-dropdown"><span class="dropdown-trigger">LIVE PROJECTS <span class="arrow-down">▼</span></span><div class="dropdown-content">{live}</div></div> ·
          {a('Achivemtn.html', 'ACHIEVEMENTS')} · {a('blog.html', 'BLOG', 'blog')} · {a('contact.html', 'CONTACT')} · {resume}
        </nav>
        <div class="social-links-minimal">{social}</div>
      </div>
    </header>'''
    return drawer, header


def link_hub(prefix):
    newest = sorted(POSTS, key=lambda s: POSTS[s]['date'], reverse=True)[:6]
    topics = ''.join(f'<li><a href="{prefix}blog/topics/{t}.html">{esc(v["name"])}</a></li>' for t, v in TOPICS.items())
    latest = ''.join(f'<li><a href="{prefix}blog/{s}.html">{esc(trunc(EXTRACTED[s]["title"], 52))}</a></li>' for s in newest)
    pages = ''.join(f'<li><a href="{prefix}{h}">{n}</a></li>' for n, h in [
        ('Home', 'index.html'), ('About Dharmik', 'about.html'), ('Services & pricing', 'services.html'), ('Portfolio', 'portfolio.html'),
        ('Achievements', 'Achivemtn.html'), ('Blog', 'blog.html'), ('Contact & hire', 'contact.html'), ('HTML sitemap', 'sitemap-page.html')])
    work = ''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>' for n, u in [
        ('Games on itch.io', 'https://dharmikgohil.itch.io/'), ('LowXena card game', 'https://lowxena.dharmikgohil.art/'),
        ('GitHub', 'https://github.com/DharmikGohil013'), ('LinkedIn', 'https://www.linkedin.com/in/dharmikgohil086/'), ('X / Twitter', 'https://x.com/Dharmik086')])
    return f'''
  <aside class="link-hub" aria-label="Site directory">
    <div class="link-hub-grid">
      <div><h2>Explore</h2><ul>{pages}</ul></div>
      <div><h2>Blog topics</h2><ul>{topics}</ul></div>
      <div><h2>Latest articles</h2><ul>{latest}</ul></div>
      <div><h2>Elsewhere</h2><ul>{work}</ul></div>
    </div>
    <p class="link-hub-note">Dharmik Gohil is a Unity game developer and XR / full-stack engineer based in Surat, Gujarat, India, working remotely with studios and founders worldwide. <a href="{prefix}services.html">See services</a> or <a href="{prefix}contact.html">get in touch</a> for a free consultation.</p>
  </aside>'''


def colophon():
    return '''
  <footer class="container">
    <div class="colophon-footer">
      <div class="colophon-sig">THE DHARMIK GOHIL CHRONICLE · <span>DESIGNED WITH INK &amp; PAPER</span></div>
      <div class="colophon-sig text-end">© 2026 DHARMIK GOHIL. ALL RIGHTS RESERVED.</div>
    </div>
  </footer>'''


def head_common(prefix, title, description, canonical, og_image, og_type, extra_meta='', schema=''):
    fonts = 'https://fonts.googleapis.com/css2?family=Bebas+Neue&family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,700;1,400&family=Lora:ital,wght@0,400;0,600;0,700;1,400&family=Playfair+Display:ital,wght@0,900;1,900&display=swap'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script>(function(d){{if(!matchMedia('(prefers-reduced-motion: reduce)').matches){{d.classList.add('motion-ok');setTimeout(function(){{if(!window.__motionReady)d.classList.remove('motion-ok')}},4500)}}}})(document.documentElement)</script>
  <noscript><style>[data-reveal],[data-kinetic]{{opacity:1!important;transform:none!important;clip-path:none!important}}.post-cover{{clip-path:none!important;animation:none!important}}</style></noscript>
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <meta name="author" content="Dharmik Gohil">
  <meta name="theme-color" content="#f2f0eb">
  <meta name="geo.region" content="IN-GJ"><meta name="geo.placename" content="Surat, Gujarat, India"><meta name="geo.position" content="21.1702;72.8311"><meta name="ICBM" content="21.1702, 72.8311">
  <link rel="alternate" hreflang="en" href="{canonical}"><link rel="alternate" hreflang="x-default" href="{canonical}">
  <link rel="author" href="https://www.linkedin.com/in/dharmikgohil086/">
  <meta property="og:site_name" content="Dharmik Gohil – Unity Game Developer"><meta property="og:locale" content="en_US">
  <meta property="og:type" content="{og_type}"><meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}">
  <meta property="og:image" content="{og_image}"><meta property="og:image:alt" content="{esc(title)}">
  <meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@Dharmik086"><meta name="twitter:creator" content="@Dharmik086">
  <meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(description)}"><meta name="twitter:image" content="{og_image}">
  {extra_meta}
  <link rel="icon" type="image/png" href="{prefix}assets/img/dlogo.png"><link rel="apple-touch-icon" href="{prefix}assets/img/dlogo.png">
  <link rel="alternate" type="application/rss+xml" title="Dharmik Gohil – Blog" href="{SITE}/feed.xml">
  <link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="{fonts}">
  <link rel="stylesheet" href="{prefix}assets/vendor/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="{prefix}assets/css/main.css">
  <link rel="stylesheet" href="{prefix}index.css">
  <link rel="stylesheet" href="{prefix}assets/css/responsive-global.css">
  <link rel="stylesheet" href="{prefix}assets/vendor/bootstrap-icons/bootstrap-icons.css">
  <link rel="stylesheet" href="{prefix}assets/vendor/glightbox/css/glightbox.min.css">
  <link rel="stylesheet" href="{prefix}assets/css/global-multilingual.css">
  <link rel="stylesheet" href="{prefix}assets/css/blog-post.css">
  <link rel="stylesheet" href="{prefix}assets/css/motion.css">
  <meta name="google-adsense-account" content="ca-pub-4658801537271443">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4658801537271443" crossorigin="anonymous"></script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-GE7F8SZSJ9"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-GE7F8SZSJ9');</script>
  {schema}
</head>'''


def foot_scripts(prefix):
    return f'''
  <script src="{prefix}assets/vendor/glightbox/js/glightbox.min.js" defer></script>
  <script src="{prefix}assets/js/blog-post.js" defer></script>
  <script src="{prefix}assets/js/motion.js" defer></script>
  <script src="{prefix}assets/js/global-multilingual.js" defer></script>
</body>
</html>
'''


def crumbs_html(trail):
    items = []
    for i, (label, href) in enumerate(trail):
        last = i == len(trail) - 1
        items.append(f'<li><span aria-current="page">{esc(label)}</span></li>' if last else f'<li><a href="{href}">{esc(label)}</a></li>')
    return f'<nav aria-label="Breadcrumb"><ol class="crumbs">{"".join(items)}</ol></nav>'


def breadcrumb_ld(trail):
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(trail)]}


def card_html(slug, prefix, show_excerpt=True):
    p, m = POSTS[slug], EXTRACTED[slug]
    cover = m['cover'] or ''
    if cover.startswith('../'):
        cover = prefix + cover[3:]
    tname = TOPICS[p['topic']]['short']
    return f'''<a class="post-card" href="{prefix}blog/{slug}.html">
      <div class="thumb"><img src="{esc(cover)}" alt="{esc(m['cover_alt'] or m['title'])}" loading="lazy" decoding="async" width="640" height="360"></div>
      <div class="body"><span class="tag">{esc(tname)}</span><h3>{esc(m['title'])}</h3>{f'<p>{esc(trunc(p["description"], 120))}</p>' if show_excerpt else ''}
      <span class="foot">{fmt_date(p['date'])} · {p['minutes']} min read</span></div></a>'''


# ----------------------------------------------------------------- page renderers
def render_post(slug, bodies):
    p, m = POSTS[slug], EXTRACTED[slug]
    topic = TOPICS[p['topic']]
    body, toc, _ = bodies[slug]
    prefix = '../'
    title = m['title']
    url = post_url(slug)
    cover = m['cover'] or ''
    cover_abs = abs_url(cover)
    cover_src = prefix + cover[3:] if cover.startswith('../') else cover

    # related
    rel = [r for r in p['related'] if r in POSTS and r != slug][:4]
    topic_posts = topic['posts']
    idx = topic_posts.index(slug) if slug in topic_posts else 0
    prev_s = topic_posts[(idx - 1) % len(topic_posts)]
    next_s = topic_posts[(idx + 1) % len(topic_posts)]

    trail = [('Home', SITE + '/'), ('Blog', SITE + '/blog.html'), (topic['name'], topic_url(p['topic'])), (title, url)]
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'BlogPosting', '@id': url + '#article', 'headline': trunc(title, 110), 'description': p['description'],
         'image': [cover_abs], 'datePublished': p['date'], 'dateModified': TODAY, 'inLanguage': 'en',
         'author': {k: v for k, v in PERSON.items()}, 'publisher': PUBLISHER,
         'mainEntityOfPage': {'@type': 'WebPage', '@id': url}, 'isPartOf': {'@type': 'Blog', '@id': SITE + '/blog.html#blog', 'name': 'Dharmik Gohil Blog', 'url': SITE + '/blog.html'},
         'articleSection': topic['name'], 'keywords': ', '.join(p['tags']), 'wordCount': p['words'], 'timeRequired': f'PT{p["minutes"]}M',
         'about': [{'@type': 'Thing', 'name': t} for t in p['tags']]},
        breadcrumb_ld(trail),
        {'@type': 'FAQPage', '@id': url + '#faq', 'mainEntity': [
            {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in p['faqs']]},
    ]}
    extra = (f'<meta property="article:published_time" content="{p["date"]}T00:00:00+05:30"><meta property="article:modified_time" content="{TODAY}T00:00:00+05:30">'
             f'<meta property="article:author" content="https://www.linkedin.com/in/dharmikgohil086/"><meta property="article:section" content="{esc(topic["name"])}">'
             + ''.join(f'<meta property="article:tag" content="{esc(t)}">' for t in p['tags'])
             + f'<meta name="keywords" content="{esc(", ".join(p["tags"] + [topic["name"], "Dharmik Gohil"]))}">'
             + f'<link rel="preload" as="image" href="{esc(cover_src)}" fetchpriority="high">')
    head = head_common(prefix, p['seo_title'], p['description'], url, cover_abs, 'article', extra, jsonld(ld))
    drawer, header = nav_html(prefix, 'blog')

    toc_li = ''.join(f'<li><a href="#{i}">{esc(t)}</a></li>' for i, t in toc)
    toc_block = f'<nav class="toc" aria-label="Table of contents"><p class="toc-title">On this page</p><ol>{toc_li}</ol></nav>'
    takeaways = ''.join(f'<li>{esc(t)}</li>' for t in p['takeaways'])
    faq = ''.join(f'<details><summary>{esc(q)}</summary><div class="answer"><p>{esc(a)}</p></div></details>' for q, a in p['faqs'])
    aside_topic = ''.join(f'<li><a href="{s}.html">{esc(trunc(EXTRACTED[s]["title"], 70))}<small>{fmt_date(POSTS[s]["date"])}</small></a></li>' for s in topic_posts if s != slug)
    tags = ''.join(f'<span class="tech-badge">{esc(t)}</span>' for t in p['tags'])
    share_u = url
    return f'''{head}
<body class="blog-post-page index-page">
  <div class="read-progress" aria-hidden="true"><i></i></div>
{drawer}
  <main class="main">{header}
    <div class="post-shell">
      {crumbs_html([('Home', prefix + 'index.html'), ('Blog', prefix + 'blog.html'), (topic['name'], f'topics/{p["topic"]}.html'), (trunc(title, 56), '')])}
      <div class="post-grid">
        <article class="post-main" itemscope itemtype="https://schema.org/BlogPosting">
          <header class="post-head">
            <a class="post-kicker" href="topics/{p['topic']}.html"><i class="bi {topic['icon']}"></i> {esc(topic['name'])}</a>
            <h1 class="post-title" data-kinetic itemprop="headline">{esc(title)}</h1>
            <p class="post-deck">{esc(p['description'])}</p>
            <ul class="post-meta">
              <li><i class="bi bi-person"></i><a href="{prefix}about.html" rel="author">Dharmik Gohil</a></li>
              <li><i class="bi bi-calendar3"></i><time datetime="{p['date']}" itemprop="datePublished">{fmt_date(p['date'])}</time></li>
              <li><i class="bi bi-arrow-repeat"></i>Updated <time datetime="{TODAY}" itemprop="dateModified">{fmt_date(TODAY)}</time></li>
              <li><i class="bi bi-clock"></i>{p['minutes']} min read</li>
            </ul>
          </header>
          <figure class="post-cover"><img src="{esc(cover_src)}" alt="{esc(m['cover_alt'] or title)}" width="1200" height="675" fetchpriority="high" decoding="async"></figure>
          <div class="takeaways"><ul>{takeaways}</ul></div>
          <div class="toc-mobile">{toc_block}</div>
          <div class="article-body" itemprop="articleBody">
{body}
          </div>
          <div class="tech-stack" style="margin-top:2rem">{tags}</div>
          <div class="share-row"><span>Share</span>
            <a href="https://x.com/intent/tweet?url={esc(share_u)}&amp;text={esc(title)}" target="_blank" rel="noopener"><i class="bi bi-twitter-x"></i> Post</a>
            <a href="https://www.linkedin.com/sharing/share-offsite/?url={esc(share_u)}" target="_blank" rel="noopener"><i class="bi bi-linkedin"></i> LinkedIn</a>
            <button type="button" data-copy="{esc(share_u)}"><i class="bi bi-link-45deg"></i> <span>Copy link</span></button>
          </div>
          <section class="faq" aria-labelledby="faq-h"><h2 class="block-label" id="faq-h">Questions, answered</h2>{faq}</section>
          <div class="byline-box">
            <img src="{prefix}assets/img/dharmik-gohil-professional-headshot-photo.png" alt="Dharmik Gohil, Unity game developer" width="84" height="84" loading="lazy">
            <div><h3>Dharmik Gohil</h3><p>Unity game developer and XR / full-stack engineer from Surat, India. I ship multiplayer games, AR/VR experiences and web apps, and write about what works.</p>
              <div class="links"><a href="{prefix}about.html">About</a><a href="{prefix}services.html">Services</a><a href="{prefix}portfolio.html">Portfolio</a><a href="{prefix}contact.html">Hire me</a></div></div>
          </div>
          <nav class="post-nav" aria-label="More in {esc(topic['name'])}">
            <a class="prev" href="{prev_s}.html" rel="prev"><small>← Previous in {esc(topic['short'])}</small><strong>{esc(trunc(EXTRACTED[prev_s]['title'], 80))}</strong></a>
            <a class="next" href="{next_s}.html" rel="next"><small>Next in {esc(topic['short'])} →</small><strong>{esc(trunc(EXTRACTED[next_s]['title'], 80))}</strong></a>
          </nav>
        </article>
        <aside class="post-aside" aria-label="Article sidebar">
          <div class="aside-card" data-toc-desktop><h2>On this page</h2>{toc_block}</div>
          <div class="aside-card"><h2>More in {esc(topic['short'])}</h2><ul class="aside-list">{aside_topic}<li><a href="topics/{p['topic']}.html">All {esc(topic['name'])} articles →</a></li></ul></div>
          <div class="aside-cta"><h3>Need this built?</h3><p>I take on Unity, XR, multiplayer and full-stack projects. Free consultation, reply within 24 hours.</p><a href="{prefix}contact.html">Start a project →</a></div>
        </aside>
      </div>
      <section class="related" aria-labelledby="rel-h"><h2 class="block-label" id="rel-h">Keep reading</h2>
        <div class="card-grid">{''.join(card_html(r, prefix) for r in rel)}</div></section>
      {link_hub(prefix)}
    </div>
  </main>{colophon()}
{foot_scripts(prefix)}'''


def render_topic(tkey, prefix='../../'):
    t = TOPICS[tkey]
    url = topic_url(tkey)
    posts = sorted(t['posts'], key=lambda s: POSTS[s]['date'], reverse=True)
    trail = [('Home', SITE + '/'), ('Blog', SITE + '/blog.html'), (t['name'], url)]
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'CollectionPage', '@id': url, 'url': url, 'name': t['name'] + ' – Dharmik Gohil Blog', 'description': t['description'], 'inLanguage': 'en',
         'isPartOf': {'@type': 'Blog', '@id': SITE + '/blog.html#blog'}, 'about': {'@type': 'Thing', 'name': t['name']}, 'author': PERSON,
         'mainEntity': {'@type': 'ItemList', 'numberOfItems': len(posts), 'itemListElement': [
             {'@type': 'ListItem', 'position': i + 1, 'url': post_url(s), 'name': EXTRACTED[s]['title']} for i, s in enumerate(posts)]}},
        breadcrumb_ld(trail)]}
    head = head_common(prefix, t['title'], t['description'], url, abs_url(EXTRACTED[posts[0]]['cover']), 'website', '', jsonld(ld))
    drawer, header = nav_html(prefix, 'blog')
    nav = ''.join(f'<li><a href="{k}.html"{" aria-current=page" if k == tkey else ""}><i class="bi {v["icon"]}"></i> {esc(v["short"])}</a></li>' for k, v in TOPICS.items())
    svc_label, svc_href = t['service']
    return f'''{head}
<body class="blog-post-page index-page">
  <div class="read-progress" aria-hidden="true"><i></i></div>
{drawer}
  <main class="main">{header}
    <div class="post-shell">
      {crumbs_html([('Home', prefix + 'index.html'), ('Blog', prefix + 'blog.html'), (t['name'], '')])}
      <header class="hub-hero">
        <span class="post-kicker"><i class="bi {t['icon']}"></i> Topic hub</span>
        <h1 class="post-title" data-kinetic>{esc(t['name'])}</h1>
        <p class="post-deck">{esc(t['intro'])}</p>
        <p class="hub-lead">{esc(t['lead'])}</p>
        <span class="hub-count">{len(posts)} articles · <a href="{svc_href}">{esc(svc_label)} →</a></span>
      </header>
      <ul class="topic-nav" aria-label="Blog topics">{nav}</ul>
      <div class="card-grid">{''.join(card_html(s, prefix) for s in posts)}</div>
      <div class="cta-bar" style="max-width:none"><h3>Have a {esc(t['short'].lower())} project in mind?</h3><p>I am available for freelance and contract work worldwide. Tell me what you are building.</p><a class="cta-btn" href="{prefix}contact.html"><i class="bi bi-send"></i> Get a free consultation</a></div>
      {link_hub(prefix)}
    </div>
  </main>{colophon()}
{foot_scripts(prefix)}'''


def render_index(prefix=''):
    url = SITE + '/blog.html'
    allp = sorted(POSTS, key=lambda s: POSTS[s]['date'], reverse=True)
    trail = [('Home', SITE + '/'), ('Blog', url)]
    desc = 'Unity, multiplayer, XR and full-stack tutorials plus hackathon and event stories from game developer Dharmik Gohil. Browse by topic or read the latest.'
    title = 'Game Development Blog: Unity, XR & Multiplayer | Dharmik Gohil'
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'Blog', '@id': url + '#blog', 'url': url, 'name': 'Dharmik Gohil Blog', 'description': desc, 'inLanguage': 'en', 'author': PERSON, 'publisher': PUBLISHER,
         'blogPost': [{'@type': 'BlogPosting', '@id': post_url(s) + '#article', 'headline': trunc(EXTRACTED[s]['title'], 110), 'url': post_url(s), 'datePublished': POSTS[s]['date'],
                       'image': abs_url(EXTRACTED[s]['cover']), 'author': {'@id': PERSON['@id']}} for s in allp]},
        {'@type': 'CollectionPage', '@id': url, 'url': url, 'name': title, 'description': desc, 'isPartOf': {'@id': SITE + '/#website'},
         'mainEntity': {'@type': 'ItemList', 'numberOfItems': len(allp), 'itemListElement': [
             {'@type': 'ListItem', 'position': i + 1, 'url': post_url(s), 'name': EXTRACTED[s]['title']} for i, s in enumerate(allp)]}},
        breadcrumb_ld(trail)]}
    head = head_common(prefix, title, desc, url, abs_url(EXTRACTED[allp[0]]['cover']), 'website', '', jsonld(ld))
    drawer, header = nav_html(prefix, 'blog')
    nav = ''.join(f'<li><a href="blog/topics/{k}.html"><i class="bi {v["icon"]}"></i> {esc(v["short"])} <small>({len(v["posts"])})</small></a></li>' for k, v in TOPICS.items())
    feat = allp[0]
    fp, fm = POSTS[feat], EXTRACTED[feat]
    fcover = fm['cover'][3:] if fm['cover'].startswith('../') else fm['cover']
    cards = ''.join(card_html(s, prefix) for s in allp[1:])
    hubs = ''.join(f'<a class="hub-link" href="blog/topics/{k}.html"><i class="bi {v["icon"]}"></i><strong>{esc(v["name"])}</strong><span>{esc(trunc(v["intro"], 110))}</span></a>' for k, v in TOPICS.items())
    return f'''{head}
<body class="blog-post-page index-page">
  <div class="read-progress" aria-hidden="true"><i></i></div>
{drawer}
  <main class="main">{header}
    <div class="post-shell">
      {crumbs_html([('Home', 'index.html'), ('Blog', '')])}
      <header class="hub-hero">
        <span class="post-kicker"><i class="bi bi-rss-fill"></i> Field notes</span>
        <h1 class="post-title" data-kinetic>Game Dev Blog &amp; Insights</h1>
        <p class="post-deck">Unity, multiplayer, XR and full-stack lessons from shipped projects, plus honest write-ups from hackathons and tech festivals.</p>
        <span class="hub-count">{len(allp)} articles · {len(TOPICS)} topics · updated {fmt_date(TODAY)}</span>
      </header>
      <ul class="topic-nav" aria-label="Blog topics">{nav}</ul>
      <a class="post-card" href="blog/{feat}.html" style="margin-bottom:1.6rem;flex-direction:row;flex-wrap:wrap">
        <div class="thumb" style="flex:1 1 380px;border-bottom:0;border-right:2px solid var(--ink)"><img src="{esc(fcover)}" alt="{esc(fm['cover_alt'] or fm['title'])}" width="1200" height="675" fetchpriority="high"></div>
        <div class="body" style="flex:1 1 320px;justify-content:center;padding:2rem"><span class="tag">Latest · {esc(TOPICS[fp['topic']]['short'])}</span><h2 style="font-family:var(--font-editorial);font-weight:900;font-size:clamp(1.5rem,3vw,2.2rem);line-height:1.15;margin:0">{esc(fm['title'])}</h2><p>{esc(fp['description'])}</p><span class="foot">{fmt_date(fp['date'])} · {fp['minutes']} min read · Read article →</span></div>
      </a>
      <div class="card-grid">{cards}</div>
      <section class="related" aria-labelledby="hub-h"><h2 class="block-label" id="hub-h">Browse by topic</h2><div class="hub-index" style="margin-top:0">{hubs}</div></section>
      {link_hub(prefix)}
    </div>
  </main>{colophon()}
{foot_scripts(prefix)}'''


# ----------------------------------------------------------------- sitemap / llms.txt / feed
def update_sitemap():
    path = os.path.join(ROOT, 'sitemap.xml')
    xml = open(path, encoding='utf-8').read()
    # drop any existing blog/* and topic entries, then append fresh ones
    xml = re.sub(r'\s*<url>\s*<loc>https://dharmikgohil\.art/blog/[^<]*</loc>.*?</url>', '', xml, flags=re.S)
    xml = re.sub(r'(<loc>https://dharmikgohil\.art/blog\.html</loc>\s*<lastmod>)[^<]*', r'\g<1>' + TODAY, xml)
    entries = []
    for t in TOPICS:
        entries.append(f'  <url>\n    <loc>{topic_url(t)}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>')
    for s in sorted(POSTS, key=lambda s: POSTS[s]['date'], reverse=True):
        img = abs_url(EXTRACTED[s]['cover'])
        entries.append(f'  <url>\n    <loc>{post_url(s)}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n'
                       f'    <image:image><image:loc>{esc(img)}</image:loc><image:title>{esc(EXTRACTED[s]["title"])}</image:title></image:image>\n  </url>')
    block = '\n  <!-- BLOG: TOPIC HUBS + ARTICLES (generated by tools/blog/build.py) -->\n' + '\n'.join(entries) + '\n'
    xml = xml.replace('</urlset>', block + '</urlset>')
    open(path, 'w', encoding='utf-8', newline='\n').write(xml)


def update_llms():
    path = os.path.join(ROOT, 'llms.txt')
    txt = open(path, encoding='utf-8').read()
    start = txt.find('## Blog')
    section = '## Blog\n\n- Blog index: https://dharmikgohil.art/blog.html\n' + ''.join(
        f'- {v["name"]} (topic hub): {topic_url(k)}\n' for k, v in TOPICS.items()) + '\n### Articles\n\n' + ''.join(
        f'- [{EXTRACTED[s]["title"]}]({post_url(s)}): {POSTS[s]["description"]}\n' for s in sorted(POSTS, key=lambda s: POSTS[s]['date'], reverse=True)) + '\n'
    if start >= 0:
        nxt = re.search(r'\n## ', txt[start + 5:])
        end = start + 5 + nxt.start() + 1 if nxt else len(txt)
        txt = txt[:start] + section + txt[end:]
    else:
        txt = txt.rstrip() + '\n\n' + section
    open(path, 'w', encoding='utf-8', newline='\n').write(txt)


def write_feed():
    items = ''.join(
        f'<item><title>{esc(EXTRACTED[s]["title"])}</title><link>{post_url(s)}</link><guid isPermaLink="true">{post_url(s)}</guid>'
        f'<pubDate>{date.fromisoformat(POSTS[s]["date"]).strftime("%a, %d %b %Y 00:00:00 +0530")}</pubDate><category>{esc(TOPICS[POSTS[s]["topic"]]["name"])}</category>'
        f'<description>{esc(POSTS[s]["description"])}</description></item>'
        for s in sorted(POSTS, key=lambda s: POSTS[s]['date'], reverse=True))
    feed = (f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>Dharmik Gohil – Game Dev Blog</title><link>{SITE}/blog.html</link>'
            f'<description>Unity, XR, multiplayer and full-stack articles by Dharmik Gohil.</description><language>en</language>{items}</channel></rss>\n')
    open(os.path.join(ROOT, 'feed.xml'), 'w', encoding='utf-8', newline='\n').write(feed)


# ----------------------------------------------------------------- main
def prepare_bodies():
    """Process every fragment and fill words/minutes on POSTS (needed by card renderers)."""
    bodies = {}
    for slug in POSTS:
        raw = open(os.path.join(HERE, 'posts', slug + '.html'), encoding='utf-8').read()
        b, toc, n = process_fragment(slug, raw, EXTRACTED[slug])
        w = article_text_words(b)
        POSTS[slug]['words'] = w
        POSTS[slug]['minutes'] = max(2, math.ceil(w / 200))
        bodies[slug] = (b, toc, n)
    missing = set(EXTRACTED) - set(POSTS)
    assert not missing, f'posts without metadata: {missing}'
    return bodies


def main():
    bodies = prepare_bodies()

    for slug in POSTS:
        out = os.path.join(ROOT, 'blog', slug + '.html')
        open(out, 'w', encoding='utf-8', newline='\n').write(render_post(slug, bodies))
    os.makedirs(os.path.join(ROOT, 'blog', 'topics'), exist_ok=True)
    for t in TOPICS:
        open(os.path.join(ROOT, 'blog', 'topics', t + '.html'), 'w', encoding='utf-8', newline='\n').write(render_topic(t))
    open(os.path.join(ROOT, 'blog.html'), 'w', encoding='utf-8', newline='\n').write(render_index())
    update_sitemap()
    update_llms()
    write_feed()
    print(f'built {len(POSTS)} posts, {len(TOPICS)} topic hubs, blog index, sitemap, llms.txt, feed.xml')
    for s, (b, toc, n) in bodies.items():
        print(f'  {s[:48]:48} words={POSTS[s]["words"]:5} read={POSTS[s]["minutes"]:2}m toc={len(toc):2} ctx-links={n}')


if __name__ == '__main__':
    main()
