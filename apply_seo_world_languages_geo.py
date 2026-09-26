#!/usr/bin/env python3
"""
apply_seo_world_languages_geo.py
Comprehensive Global Multilingual (200+ Languages) and Worldwide GEO SEO Optimizer
Website: https://dharmikgohil.art
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

WORKSPACE_DIR = Path(__file__).resolve().parent
DOMAIN = "dharmikgohil.art"
BASE_URL = f"https://{DOMAIN}"

with open(WORKSPACE_DIR / 'languages.json', 'r', encoding='utf-8') as f:
    LANGUAGES = json.load(f)

# List of all 280 language names and codes for Schema.org
SCHEMA_LANGUAGES = [f"{l['name']} ({l['code']})" for l in LANGUAGES]

OG_LOCALES = [
    "en_GB", "en_CA", "en_AU", "en_IN", "en_NZ", "en_ZA",
    "es_ES", "es_LA", "es_MX", "fr_FR", "fr_CA", "de_DE", "de_AT", "de_CH",
    "it_IT", "pt_BR", "pt_PT", "ru_RU", "ja_JP", "zh_CN", "zh_TW", "zh_HK",
    "ko_KR", "ar_AR", "hi_IN", "gu_IN", "bn_IN", "pa_IN", "mr_IN", "ta_IN",
    "te_IN", "ur_PK", "tr_TR", "vi_VN", "th_TH", "id_ID", "ms_MY", "nl_NL",
    "pl_PL", "sv_SE", "da_DK", "fi_FI", "nb_NO", "el_GR", "he_IL", "cs_CZ",
    "hu_HU", "ro_RO", "uk_UA"
]

TOP_COUNTRIES = [
    ("United States", "US"), ("United Kingdom", "GB"), ("India", "IN"),
    ("Canada", "CA"), ("Australia", "AU"), ("Germany", "DE"),
    ("France", "FR"), ("Japan", "JP"), ("United Arab Emirates", "AE"),
    ("Singapore", "SG"), ("Switzerland", "CH"), ("Netherlands", "NL"),
    ("Sweden", "SE"), ("Saudi Arabia", "SA"), ("Brazil", "BR"),
    ("South Korea", "KR"), ("New Zealand", "NZ"), ("Ireland", "IE"),
    ("Spain", "ES"), ("Italy", "IT"), ("Norway", "NO"), ("Denmark", "DK"),
    ("Finland", "FI"), ("Poland", "PL"), ("Mexico", "MX"), ("Indonesia", "ID")
]

CONTINENTS = ["North America", "Europe", "Asia", "Oceania", "South America", "Africa"]

def get_canonical_url(rel_path):
    rel_path_str = str(rel_path).replace('\\', '/')
    if rel_path_str in ['index.html', './index.html']:
        return f"{BASE_URL}/"
    return f"{BASE_URL}/{rel_path_str}"

def build_hreflang_block(canonical_url):
    lines = [
        "  <!-- ======================================================= -->",
        "  <!-- 200+ INTERNATIONAL WORLD LANGUAGES HREFLANG ANNOTATIONS  -->",
        "  <!-- ======================================================= -->",
        f'  <link rel="alternate" hreflang="x-default" href="{canonical_url}">',
        f'  <link rel="alternate" hreflang="en" href="{canonical_url}">'
    ]
    sep = '&' if '?' in canonical_url else '?'
    for lang in LANGUAGES:
        code = lang['code']
        if code == 'en':
            continue
        loc_url = f"{canonical_url}{sep}lang={code}"
        lines.append(f'  <link rel="alternate" hreflang="{code}" href="{loc_url}">')
    return '\n'.join(lines)

def build_geo_block():
    return """  <!-- ======================================================= -->
  <!-- GLOBAL GEOGRAPHIC & MULTI-REGION SEO (WORLDWIDE REACH)     -->
  <!-- ======================================================= -->
  <meta name="geo.region" content="IN-GJ">
  <meta name="geo.placename" content="Surat, Gujarat, India; Global Remote Service">
  <meta name="geo.position" content="21.1702;72.8311">
  <meta name="ICBM" content="21.1702, 72.8311">
  <meta name="coverage" content="Worldwide">
  <meta name="distribution" content="Global">
  <meta name="target" content="all">
  <meta name="audience" content="all">
  <meta name="rating" content="general">
  <meta name="country" content="GLOBAL">
  <meta name="geography" content="Global, Worldwide, Remote">
  <meta name="target_country" content="US, GB, CA, AU, DE, FR, JP, IN, AE, SG, NL, CH, SE, BR, KR, SA, ES, IT, NZ, IE, Global">
  <meta name="DC.coverage" content="Worldwide">
  <meta name="DC.Language" content="en, hi, gu, es, fr, de, ja, zh, ru, ar, pt, it, ko, nl, tr, id, vi, pl, sv, uk">
  <meta name="DC.publisher" content="Dharmik Gohil">
  <meta name="DC.creator" content="Dharmik Gohil">
  <meta name="DC.format" content="text/html">
  <meta name="DC.type" content="InteractiveResource">"""

def build_og_locales_block():
    lines = [
        "  <!-- ======================================================= -->",
        "  <!-- MULTILINGUAL OPEN GRAPH ALTERNATE LOCALES                -->",
        "  <!-- ======================================================= -->"
    ]
    for loc in OG_LOCALES:
        lines.append(f'  <meta property="og:locale:alternate" content="{loc}">')
    return '\n'.join(lines)

def build_multilingual_keywords_block():
    return """  <!-- ======================================================= -->
  <!-- MULTILINGUAL KEYWORDS FOR GLOBAL ORGANIC DISCOVERY          -->
  <!-- ======================================================= -->
  <meta name="keywords:multilingual" content="hire game developer india, unity developer, XR developer, contratar desarrollador videojuegos, développeur jeux vidéo unity, Unity Spieleentwickler, ゲーム開発者 依頼, 聘请游戏开发者, गेम डेवलपर, ગેમ ડેવલપર, توظيف مطور ألعاب, desenvolvedor de jogos, unity разработчик, sviluppatore videogiochi, 게임 개발자, Unity ontwikelaar, gry developer, oyun geliştirici, pengembang game">"""

def build_schema_geo_multilingual_block(canonical_url):
    area_served_list = [{"@type": "Place", "name": "Worldwide"}]
    for cont in CONTINENTS:
        area_served_list.append({"@type": "Continent", "name": cont})
    for country_name, code in TOP_COUNTRIES:
        area_served_list.append({"@type": "Country", "name": country_name, "identifier": code})

    schema_data = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "@id": f"{canonical_url}#globalservice",
        "name": "Dharmik Gohil — Global Unity Game Developer & XR Specialist",
        "url": canonical_url,
        "image": f"{BASE_URL}/assets/img/dharmik-profile-photo-2026.jpg",
        "description": "Worldwide game development and XR engineering services by Dharmik Gohil. Shipped 10+ titles, IIT Bombay Techfest winner, available globally for Unity 3D, multiplayer (Photon PUN), AR/VR, and full-stack solutions.",
        "currenciesAccepted": "USD, EUR, GBP, INR, AED, CAD, AUD, JPY, SGD",
        "paymentAccepted": "Credit Card, Wire Transfer, Wise, PayPal, Cryptocurrency, UPI",
        "priceRange": "$$",
        "areaServed": area_served_list,
        "availableLanguage": SCHEMA_LANGUAGES,
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Global Game Development & XR Engineering Services",
            "itemListElement": [
                {"@type": "Offer", "name": "Unity 3D/2D Game Development", "category": "Game Development"},
                {"@type": "Offer", "name": "Photon PUN Multiplayer Game Networking", "category": "Multiplayer Games"},
                {"@type": "Offer", "name": "AR/VR/XR Spatial Computing Experiences", "category": "XR Development"},
                {"@type": "Offer", "name": "Full Stack Web & Web3 Development", "category": "Web Applications"}
            ]
        },
        "contactPoint": {
            "@type": "ContactPoint",
            "contactType": "Worldwide Client Inquiries & Bookings",
            "email": "dharmikgohil.work@gmail.com",
            "url": f"{BASE_URL}/contact.html",
            "areaServed": "Worldwide",
            "availableLanguage": SCHEMA_LANGUAGES
        }
    }
    json_str = json.dumps(schema_data, indent=2, ensure_ascii=False)
    return f"""  <!-- ======================================================= -->
  <!-- SCHEMA.ORG 200+ LANGUAGES & WORLDWIDE GEO TARGETING         -->
  <!-- ======================================================= -->
  <script type="application/ld+json">
{json_str}
  </script>"""

def process_html_file(file_path):
    rel_path = file_path.relative_to(WORKSPACE_DIR)
    canonical_url = get_canonical_url(rel_path)
    
    # Calculate relative path to assets folder
    depth = len(rel_path.parts) - 1
    asset_prefix = "../" * depth if depth > 0 else ""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove any previous generated global multilingual/geo blocks if present
    content = re.sub(r'<!-- =+\s*-->\s*<!-- 200\+ INTERNATIONAL WORLD LANGUAGES.*?<!-- =+\s*-->', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- =+\s*-->\s*<!-- GLOBAL GEOGRAPHIC & MULTI-REGION SEO.*?<!-- =+\s*-->', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- =+\s*-->\s*<!-- MULTILINGUAL OPEN GRAPH ALTERNATE LOCALES.*?<!-- =+\s*-->', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- =+\s*-->\s*<!-- MULTILINGUAL KEYWORDS FOR GLOBAL ORGANIC DISCOVERY.*?<!-- =+\s*-->', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- =+\s*-->\s*<!-- SCHEMA\.ORG 200\+ LANGUAGES.*?<!-- =+\s*-->\s*<script type="application/ld\+json">.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<link rel="stylesheet" href="[^"]*global-multilingual\.css"[^>]*>', '', content)
    content = re.sub(r'<script src="[^"]*global-multilingual\.js"[^>]*></script>', '', content)

    hreflang_block = build_hreflang_block(canonical_url)
    geo_block = build_geo_block()
    og_locales_block = build_og_locales_block()
    multilingual_keywords_block = build_multilingual_keywords_block()
    schema_block = build_schema_geo_multilingual_block(canonical_url)

    css_link = f'  <link rel="stylesheet" href="{asset_prefix}assets/css/global-multilingual.css">'
    js_script = f'  <script src="{asset_prefix}assets/js/global-multilingual.js" defer></script>'

    combined_head_block = f"""
{hreflang_block}

{geo_block}

{og_locales_block}

{multilingual_keywords_block}

{schema_block}

{css_link}
"""

    # Inject right before </head>
    if '</head>' in content:
        content = content.replace('</head>', f'{combined_head_block}\n</head>', 1)
    else:
        print(f"Warning: No </head> tag found in {file_path}")

    # Inject js script right before </body>
    if '</body>' in content:
        content = content.replace('</body>', f'{js_script}\n</body>', 1)

    # In broadsheet masthead header if present, add button if not already there
    if 'EST. 2006 · SURAT, GUJARAT, INDIA' in content and 'masthead-lang-trigger' not in content:
        content = content.replace(
            'EST. 2006 · SURAT, GUJARAT, INDIA',
            'EST. 2006 · SURAT, GUJARAT, INDIA · 🌐 GLOBAL REMOTE <button type="button" class="masthead-lang-trigger" aria-label="Choose from 200+ Languages">🌐 200+ LANGUAGES</button>',
            1
        )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Optimized {rel_path} with 280 languages hreflang, worldwide GEO, OG locales & schema!")

def update_sitemap():
    sitemap_path = WORKSPACE_DIR / 'sitemap.xml'
    if not sitemap_path.exists():
        return

    with open(sitemap_path, 'r', encoding='utf-8') as f:
        sitemap_content = f.read()

    # Ensure xmlns:xhtml is in urlset
    if 'xmlns:xhtml' not in sitemap_content:
        sitemap_content = sitemap_content.replace(
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n        xmlns:xhtml="http://www.w3.org/1999/xhtml"',
            1
        )

    today = datetime.now().strftime("%Y-%m-%d")
    # Update lastmod dates
    sitemap_content = re.sub(r'<lastmod>.*?</lastmod>', f'<lastmod>{today}</lastmod>', sitemap_content)

    # Add multilingual alternates to the homepage <url> block
    top_langs_for_sitemap = [
        "en", "es", "fr", "de", "ja", "zh-CN", "hi", "gu", "ar", "pt", "ru",
        "it", "ko", "nl", "tr", "vi", "id", "pl", "sv", "uk", "bn", "pa", "mr", "ta", "te"
    ]
    xhtml_links = ['    <xhtml:link rel="alternate" hreflang="x-default" href="https://dharmikgohil.art/"/>']
    for l in top_langs_for_sitemap:
        if l == 'en':
            xhtml_links.append(f'    <xhtml:link rel="alternate" hreflang="en" href="https://dharmikgohil.art/"/>')
        else:
            xhtml_links.append(f'    <xhtml:link rel="alternate" hreflang="{l}" href="https://dharmikgohil.art/?lang={l}"/>')
    
    xhtml_block = '\n'.join(xhtml_links)

    # Clean old homepage xhtml:link if present
    sitemap_content = re.sub(r'<xhtml:link[^>]*/>\s*', '', sitemap_content)

    # Insert under homepage <loc>
    homepage_match = re.search(r'(<loc>https://dharmikgohil\.art/?</loc>\s*<lastmod>.*?</lastmod>\s*<changefreq>.*?</changefreq>\s*<priority>.*?</priority>)', sitemap_content)
    if homepage_match:
        old_part = homepage_match.group(1)
        new_part = f"{old_part}\n{xhtml_block}"
        sitemap_content = sitemap_content.replace(old_part, new_part, 1)

    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    print("Updated sitemap.xml with xmlns:xhtml, updated lastmod, and homepage international hreflang links!")

def update_llms_txt():
    llms_path = WORKSPACE_DIR / 'llms.txt'
    if not llms_path.exists():
        return

    with open(llms_path, 'r', encoding='utf-8') as f:
        txt = f.read()

    international_note = """
## Global Availability & Multilingual Accessibility

- Worldwide Service: Available for remote clients, game studios, and teams across 100+ countries including North America, Europe, Asia, Australia, Middle East, and Latin America.
- Multilingual Support: Portfolio and services support 200+ world languages with integrated instant localization (English, Spanish, French, German, Japanese, Chinese, Hindi, Gujarati, Arabic, Portuguese, Russian, Italian, Korean, Dutch, Turkish, Vietnamese, Indonesian, and more).
- Accepted Currencies: USD, EUR, GBP, INR, AED, CAD, AUD, JPY, SGD.
- Coordinates / HQ: Surat, Gujarat, India (21.1702 N, 72.8311 E) with 100% remote delivery capabilities.
"""
    if 'Global Availability & Multilingual Accessibility' not in txt:
        if '## Services' in txt:
            txt = txt.replace('## Services', f'{international_note}\n## Services', 1)
        else:
            txt += f'\n{international_note}'

        with open(llms_path, 'w', encoding='utf-8') as f:
            f.write(txt)
        print("Updated llms.txt with global availability and 200+ language support!")

def main():
    exclude_files = [
        'loader-test.html', 'premium-loader-template.html',
        'dome-gallery-demo.html', 'dome-gallery-diagnostic.html',
        'META-TAGS-TEMPLATES.html', 'schema-markup-complete.html'
    ]

    target_files = []
    for root, dirs, files in os.walk(WORKSPACE_DIR):
        # Skip .git, assets, vendor
        if '.git' in root or 'assets' in root or 'forms' in root:
            continue
        for file in files:
            if file.endswith('.html') and file not in exclude_files:
                target_files.append(Path(root) / file)

    print(f"Found {len(target_files)} HTML pages to optimize.")
    for tf in target_files:
        process_html_file(tf)

    update_sitemap()
    update_llms_txt()
    print("\nALL GLOBAL MULTILINGUAL (200+ LANGUAGES) & GEO SEO TASKS COMPLETED!")

if __name__ == '__main__':
    main()
