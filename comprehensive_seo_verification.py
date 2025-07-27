#!/usr/bin/env python3
"""
Comprehensive SEO Verification for Dharmik Gohil Portfolio
Validates aggressive SEO optimizations for maximum search visibility
"""

import os
import glob
import re
import json

portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

def analyze_page_seo(file_path):
    """Analyze SEO elements of a single page"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(file_path)
        
        # SEO Element Checks
        seo_elements = {
            'title_tag': bool(re.search(r'<title>[^<]+</title>', content)),
            'meta_description': bool(re.search(r'<meta name="description"[^>]*content="[^"]+"[^>]*/?>', content)),
            'meta_keywords': bool(re.search(r'<meta name="keywords"[^>]*content="[^"]+"[^>]*/?>', content)),
            'meta_author': bool(re.search(r'<meta name="author"[^>]*content="[^"]+"[^>]*/?>', content)),
            'canonical_url': bool(re.search(r'<link rel="canonical"[^>]*href="[^"]+"[^>]*/?>', content)),
            'og_title': bool(re.search(r'<meta property="og:title"[^>]*content="[^"]+"[^>]*/?>', content)),
            'og_description': bool(re.search(r'<meta property="og:description"[^>]*content="[^"]+"[^>]*/?>', content)),
            'og_image': bool(re.search(r'<meta property="og:image"[^>]*content="[^"]+"[^>]*/?>', content)),
            'twitter_card': bool(re.search(r'<meta[^>]*(?:name|property)="twitter:card"[^>]*content="[^"]+"[^>]*/?>', content)),
            'structured_data': bool(re.search(r'<script[^>]*type="application/ld\+json"[^>]*>', content)),
            'lang_attribute': bool(re.search(r'<html[^>]+lang="en"', content)),
            'viewport_meta': bool(re.search(r'<meta[^>]*name="viewport"', content)),
            'charset_meta': bool(re.search(r'<meta charset="utf-8"', content, re.IGNORECASE)),
        }
        
        # Advanced SEO Checks
        advanced_seo = {
            'geo_tags': bool(re.search(r'<meta name="geo\.(region|placename|position)"', content)),
            'institution_tags': bool(re.search(r'<meta name="(institution|college|university)"', content)),
            'profession_tags': bool(re.search(r'<meta name="(profession|specialization|expertise)"', content)),
            'robots_meta': bool(re.search(r'<meta name="robots"', content)),
            'googlebot_meta': bool(re.search(r'<meta name="googlebot"', content)),
            'revisit_meta': bool(re.search(r'<meta name="revisit-after"', content)),
        }
        
        # Keyword Density Analysis
        target_keywords = [
            'dharmik', 'dharmikgohil', 'gohil dharmik', 'game developer', 
            'unity developer', 'XR developer', 'CHARUSAT University', 'DEPSTAR College',
            'mobile game', 'VR AR', 'backend developer', 'gameplay engineer'
        ]
        
        keyword_density = {}
        content_lower = content.lower()
        for keyword in target_keywords:
            count = len(re.findall(re.escape(keyword.lower()), content_lower))
            keyword_density[keyword] = count
        
        # Image Alt Tag Analysis
        img_tags = re.findall(r'<img[^>]+>', content)
        images_with_alt = sum(1 for img in img_tags if 'alt=' in img)
        total_images = len(img_tags)
        
        # Calculate SEO Score
        basic_score = sum(seo_elements.values())
        advanced_score = sum(advanced_seo.values())
        total_possible = len(seo_elements) + len(advanced_seo)
        seo_percentage = ((basic_score + advanced_score) / total_possible) * 100
        
        return {
            'filename': filename,
            'basic_seo': seo_elements,
            'advanced_seo': advanced_seo,
            'keyword_density': keyword_density,
            'images': {'total': total_images, 'with_alt': images_with_alt},
            'seo_score': {
                'basic': basic_score,
                'advanced': advanced_score,
                'total': basic_score + advanced_score,
                'possible': total_possible,
                'percentage': seo_percentage
            }
        }
        
    except Exception as e:
        print(f"Error analyzing {filename}: {e}")
        return None

def generate_seo_report():
    """Generate comprehensive SEO analysis report"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("🚀 AGGRESSIVE SEO VERIFICATION REPORT")
    print("=" * 80)
    print("🎯 TARGET KEYWORDS: dharmik, dharmikgohil, gohil dharmik, game developer,")
    print("   unity developer, XR developer, CHARUSAT University, DEPSTAR College")
    print("=" * 80)
    
    all_results = []
    perfect_scores = 0
    total_keywords = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html']:
            result = analyze_page_seo(file_path)
            if result:
                all_results.append(result)
    
    # Display results for each page
    for result in all_results:
        print(f"\\n📄 {result['filename']}")
        print("-" * 50)
        
        # Basic SEO Elements
        print("🔧 Basic SEO Elements:")
        for element, status in result['basic_seo'].items():
            status_icon = "✅" if status else "❌"
            print(f"  {status_icon} {element.replace('_', ' ').title()}")
        
        # Advanced SEO Elements
        print("\\n🚀 Advanced SEO Elements:")
        for element, status in result['advanced_seo'].items():
            status_icon = "✅" if status else "❌"
            print(f"  {status_icon} {element.replace('_', ' ').title()}")
        
        # Keyword Density
        print("\\n🎯 Target Keyword Density:")
        for keyword, count in result['keyword_density'].items():
            if count > 0:
                print(f"  🔥 '{keyword}': {count} mentions")
                total_keywords += count
        
        # Images
        alt_ratio = (result['images']['with_alt'] / result['images']['total']) * 100 if result['images']['total'] > 0 else 0
        print(f"\\n🖼️  Images: {result['images']['with_alt']}/{result['images']['total']} with alt tags ({alt_ratio:.1f}%)")
        
        # SEO Score
        score = result['seo_score']
        print(f"\\n📊 SEO Score: {score['total']}/{score['possible']} ({score['percentage']:.1f}%)")
        
        if score['percentage'] >= 90:
            perfect_scores += 1
            print("🏆 EXCELLENT SEO OPTIMIZATION!")
        elif score['percentage'] >= 70:
            print("🎯 GOOD SEO OPTIMIZATION")
        else:
            print("⚠️  NEEDS IMPROVEMENT")
    
    # Overall Summary
    print("\\n" + "=" * 80)
    print("📊 OVERALL SEO PERFORMANCE SUMMARY")
    print("=" * 80)
    
    avg_score = sum(r['seo_score']['percentage'] for r in all_results) / len(all_results)
    print(f"📄 Total pages analyzed: {len(all_results)}")
    print(f"🏆 Pages with excellent SEO (90%+): {perfect_scores}")
    print(f"📈 Average SEO score: {avg_score:.1f}%")
    print(f"🎯 Total keyword mentions: {total_keywords}")
    
    # Check sitemap and robots.txt
    sitemap_exists = os.path.exists(os.path.join(portfolio_dir, "sitemap.xml"))
    robots_exists = os.path.exists(os.path.join(portfolio_dir, "robots.txt"))
    
    print(f"\\n🗺️  Infrastructure:")
    print(f"  {'✅' if sitemap_exists else '❌'} sitemap.xml")
    print(f"  {'✅' if robots_exists else '❌'} robots.txt")
    
    # SEO Readiness Assessment
    print("\\n🚀 SEARCH ENGINE DOMINANCE ASSESSMENT:")
    if avg_score >= 90 and perfect_scores >= len(all_results) * 0.7:
        print("🏆 PORTFOLIO READY TO DOMINATE SEARCH RESULTS!")
        print("   Your site is optimized for maximum visibility on:")
        print("   • Google, Bing, Yahoo, DuckDuckGo")
        print("   • Social media platforms (Facebook, Twitter, LinkedIn)")
        print("   • Target keyword rankings for 'dharmik', 'game developer', etc.")
    elif avg_score >= 70:
        print("🎯 STRONG SEO FOUNDATION - GOOD RANKING POTENTIAL")
        print("   Your site should rank well for most target keywords")
    else:
        print("⚠️  NEEDS MORE OPTIMIZATION FOR TOP RANKINGS")
    
    print("\\n🎯 NEXT STEPS FOR SEARCH DOMINANCE:")
    print("1. Submit sitemap to Google Search Console")
    print("2. Submit sitemap to Bing Webmaster Tools") 
    print("3. Monitor rankings for target keywords")
    print("4. Build quality backlinks to boost authority")
    print("5. Regular content updates to maintain freshness")

if __name__ == "__main__":
    generate_seo_report()
