with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

checks = [
    '200+ INTERNATIONAL WORLD LANGUAGES HREFLANG ANNOTATIONS',
    'hreflang="x-default"',
    'hreflang="en"',
    'hreflang="es"',
    'hreflang="ja"',
    'hreflang="hi"',
    'hreflang="gu"',
    'hreflang="zh-CN"',
    'hreflang="ar"',
    'hreflang="fr"',
    'hreflang="de"',
    'GLOBAL GEOGRAPHIC & MULTI-REGION SEO',
    'name="geo.region" content="IN-GJ"',
    'name="coverage" content="Worldwide"',
    'name="keywords:multilingual"',
    'SCHEMA.ORG 200+ LANGUAGES & WORLDWIDE GEO TARGETING',
    'assets/css/global-multilingual.css',
    'assets/js/global-multilingual.js'
]

for chk in checks:
    if chk in c:
        print(f"PASS: {chk}")
    else:
        print(f"FAIL: {chk}")

# Check blog subfolder page as well
with open('blog/charusat-expo-3-mavericks-battlegrounds-showcase.html', 'r', encoding='utf-8') as f:
    b = f.read()

blog_checks = [
    'hreflang="x-default" href="https://dharmikgohil.art/blog/charusat-expo-3-mavericks-battlegrounds-showcase.html"',
    '../assets/css/global-multilingual.css',
    '../assets/js/global-multilingual.js'
]

for bchk in blog_checks:
    if bchk in b:
        print(f"PASS (Blog): {bchk}")
    else:
        print(f"FAIL (Blog): {bchk}")

# Check sitemap
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    s = f.read()

sitemap_checks = [
    'xmlns:xhtml="http://www.w3.org/1999/xhtml"',
    'xhtml:link rel="alternate" hreflang="x-default"',
    'xhtml:link rel="alternate" hreflang="es"'
]

for schk in sitemap_checks:
    if schk in s:
        print(f"PASS (Sitemap): {schk}")
    else:
        print(f"FAIL (Sitemap): {schk}")
