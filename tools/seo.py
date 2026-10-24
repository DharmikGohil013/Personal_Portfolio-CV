"""Maintain static search metadata. Run: python tools/seo.py [--check]. No dependencies."""
import html
import json
import re
import sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://dharmikgohil.art'
NS = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
LD = re.compile(r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>.*?</script>', re.S | re.I)
PERSON = {'@type': 'Person', '@id': SITE + '/#person', 'name': 'Dharmik Gohil',
          'url': SITE + '/about.html', 'jobTitle': 'Unity Game Developer and Full-Stack Developer',
          'image': SITE + '/assets/img/dharmik-profile-photo-2026.jpg',
          'sameAs': ['https://github.com/DharmikGohil013', 'https://www.linkedin.com/in/dharmikgohil086/',
                     'https://x.com/Dharmik086', 'https://dharmikgohil.itch.io/']}
UTILITY = ['loader-test.html', 'premium-loader-template.html', 'dome-gallery-demo.html',
           'dome-gallery-diagnostic.html', 'META-TAGS-TEMPLATES.html', 'schema-markup-complete.html',
           'protected-access.html']


class Page(HTMLParser):
    def __init__(self, raw):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.feed(raw)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def find(self, tag, **attrs):
        return [a for t, a in self.tags if t == tag and all(a.get(k) == v for k, v in attrs.items())]


def read(p):
    return p.read_text(encoding='utf-8')


def write(p, text):
    if not p.exists() or read(p) != text:
        p.write_text(text, encoding='utf-8', newline='\n')


def pages():
    for loc in ET.parse(ROOT / 'sitemap.xml').findall('s:url/s:loc', NS):
        rel = urlparse(loc.text).path.lstrip('/') or 'index.html'
        yield loc.text, ROOT / rel


def normalize(raw, url):
    page = Page(raw)
    title = html.unescape(re.search(r'<title>(.*?)</title>', raw, re.S).group(1)).strip()
    desc = page.find('meta', name='description')[0]['content']
    # Remove invented translations, obsolete metadata and duplicate social tags.
    def tag_filter(m):
        tag = Page(m.group()).tags[0]
        a = tag[1]
        name = a.get('name', a.get('property', '')).lower()
        remove = (tag[0] == 'link' and ('hreflang' in a or a.get('rel') == 'canonical')) or (
            tag[0] == 'meta' and (name.startswith(('og:', 'twitter:', 'geo.', 'icbm')) or name in {
                'description', 'robots', 'googlebot', 'bingbot', 'keywords', 'revisit-after',
                'abstract', 'summary', 'classification', 'distribution', 'coverage', 'target',
                'subject', 'url', 'identifier-url', 'category', 'language', 'rating',
                'pinterest:image', 'pinterest:description'}))
        return '' if remove else m.group()
    raw = re.sub(r'<(?:meta|link)\b[^>]*>', tag_filter, raw, flags=re.I)
    # Keep only editorial article lists; replace conflicting person/business graphs.
    def ld_filter(m):
        data = json.loads(re.sub(r'^.*?>|</script>\s*$', '', m.group(), flags=re.S))
        return m.group() if data.get('@type') == 'ItemList' else ''
    raw = LD.sub(ld_filter, raw)
    kind = 'ProfilePage' if url.endswith('/about.html') else 'ContactPage' if url.endswith('/contact.html') else 'CollectionPage' if url.endswith(('/portfolio.html', '/Achivemtn.html')) else 'WebPage'
    graph = [PERSON, {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/',
                      'name': 'Dharmik Gohil', 'inLanguage': 'en', 'publisher': {'@id': PERSON['@id']}},
             {'@type': kind, '@id': url + '#webpage', 'url': url, 'name': title,
              'description': desc, 'inLanguage': 'en', 'isPartOf': {'@id': SITE + '/#website'},
              'about': {'@id': PERSON['@id']}}]
    if kind == 'ProfilePage':
        graph[-1]['mainEntity'] = {'@id': PERSON['@id']}
    image = PERSON['image']
    metadata = '\n'.join([
        f'<meta name="description" content="{html.escape(desc, quote=True)}">',
        f'<link rel="canonical" href="{url}">',
        '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">',
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="Dharmik Gohil">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:title" content="{html.escape(title, quote=True)}">',
        f'<meta property="og:description" content="{html.escape(desc, quote=True)}">',
        f'<meta property="og:image" content="{image}">',
        '<meta property="og:image:alt" content="Dharmik Gohil, Unity game and full-stack developer">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{html.escape(title, quote=True)}">',
        f'<meta name="twitter:description" content="{html.escape(desc, quote=True)}">',
        f'<meta name="twitter:image" content="{image}">',
        '<meta name="twitter:image:alt" content="Dharmik Gohil, Unity game and full-stack developer">',
        '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False) + '</script>'
    ])
    raw = raw.replace('</head>', metadata + '\n</head>', 1)
    # Remove legacy SEO-only comments and resulting blank runs without reformatting the page.
    raw = re.sub(r'<!--(?:(?!-->).)*(?:SEO|Schema|STRUCTURED DATA|HREFLANG|Language Alternates|GLOBAL GEOGRAPHIC)(?:(?!-->).)*-->', '', raw, flags=re.S | re.I)
    return re.sub(r'\n[ \t]*\n(?:[ \t]*\n)+', '\n\n', raw)


def setup():
    for url, p in pages():
        if p.parent == ROOT and p.name != 'blog.html':
            write(p, normalize(read(p), url))
    for name in UTILITY:
        p = ROOT / name
        if not p.exists():
            continue
        raw = re.sub(r'<meta\b[^>]*name=["\'](?:robots|googlebot|bingbot)["\'][^>]*>', '', read(p), flags=re.I)
        write(p, raw.replace('</head>', '<meta name="robots" content="noindex, follow">\n</head>', 1))
    write(ROOT / 'robots.txt', '# Allow search engines to render public pages and assets.\nUser-agent: *\nAllow: /\nDisallow: /forms/\nDisallow: /tools/\nDisallow: /*.py$\nDisallow: /*.md$\n\nSitemap: ' + SITE + '/sitemap.xml\n')
    # Optional lastmod is omitted when no trustworthy editorial timestamp is available.
    raw = read(ROOT / 'sitemap.xml')
    raw = re.sub(r'\s*<(lastmod|priority|changefreq)>[^<]*</\1>', '', raw)
    write(ROOT / 'sitemap.xml', raw)


def check():
    errors = []
    titles = set()
    count = 0
    for url, p in pages():
        count += 1
        if not p.exists():
            errors.append(f'{url}: missing file')
            continue
        raw = read(p)
        page = Page(raw)
        for name, found in [('canonical', page.find('link', rel='canonical')), ('description', page.find('meta', name='description'))]:
            if len(found) != 1:
                errors.append(f'{p.name}: expected one {name}, found {len(found)}')
        canonical = page.find('link', rel='canonical')
        if canonical and canonical[0].get('href') != url:
            errors.append(f'{p.name}: sitemap/canonical mismatch')
        if any('noindex' in m.get('content', '') for m in page.find('meta', name='robots')):
            errors.append(f'{p.name}: noindex URL in sitemap')
        if len(page.find('h1')) != 1:
            errors.append(f'{p.name}: expected one h1')
        if any('hreflang' in a and (a['hreflang'] not in ('en', 'x-default') or a.get('href') != url) for _, a in page.tags):
            errors.append(f'{p.name}: untranslated alternate URL')
        title = re.findall(r'<title>(.*?)</title>', raw, re.S)
        if len(title) != 1 or title[0] in titles:
            errors.append(f'{p.name}: missing or duplicate title')
        titles.update(title)
        for m in LD.finditer(raw):
            try:
                json.loads(re.sub(r'^.*?>|</script>\s*$', '', m.group(), flags=re.S))
            except ValueError:
                errors.append(f'{p.name}: invalid JSON-LD')
        for a in page.find('meta', property='og:image'):
            image = urlparse(a.get('content', ''))
            if image.netloc == urlparse(SITE).netloc and not (ROOT / unquote(image.path.lstrip('/'))).is_file():
                errors.append(f'{p.name}: missing social image')
    robots = read(ROOT / 'robots.txt')
    if 'Disallow: /assets/' in robots:
        errors.append('robots.txt blocks rendering assets')
    print(f'Checked {count} sitemap pages: {len(errors)} SEO errors')
    for error in errors:
        print(' - ' + error)
    return bool(errors)


if __name__ == '__main__':
    if '--check' not in sys.argv:
        setup()
    sys.exit(check())
