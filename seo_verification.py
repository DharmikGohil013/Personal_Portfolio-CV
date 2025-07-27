#!/usr/bin/env python3
"""
Comprehensive SEO verification for the entire portfolio
"""

import os
import glob
import re
from urllib.parse import urljoin

portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

def check_seo_elements(file_path):
    """Check all SEO elements in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(file_path)
        results = {
            'file': filename,
            'title': bool(re.search(r'<title>[^<]+</title>', content)),
            'meta_description': bool(re.search(r'<meta name="description"[^>]*content="[^"]+"[^>]*/?>', content)),
            'meta_keywords': bool(re.search(r'<meta name="keywords"[^>]*content="[^"]+"[^>]*/?>', content)),
            'meta_author': bool(re.search(r'<meta name="author"[^>]*content="[^"]+"[^>]*/?>', content)),
            'canonical': bool(re.search(r'<link rel="canonical"[^>]*href="[^"]+"[^>]*/?>', content)),
            'og_title': bool(re.search(r'<meta property="og:title"[^>]*content="[^"]+"[^>]*/?>', content)),
            'og_description': bool(re.search(r'<meta property="og:description"[^>]*content="[^"]+"[^>]*/?>', content)),
            'og_image': bool(re.search(r'<meta property="og:image"[^>]*content="[^"]+"[^>]*/?>', content)),
            'twitter_card': bool(re.search(r'<meta[^>]*(?:name|property)="twitter:card"[^>]*content="[^"]+"[^>]*/?>', content)),
            'structured_data': bool(re.search(r'<script[^>]*type="application/ld\+json"[^>]*>', content)),
            'lang_attribute': bool(re.search(r'<html[^>]+lang="en"', content)),
            'viewport': bool(re.search(r'<meta[^>]*name="viewport"', content)),
            'charset': bool(re.search(r'<meta charset="utf-8"', content, re.IGNORECASE)),
            'images_with_alt': True  # Will be checked separately
        }
        
        # Check if all images have alt tags
        img_tags = re.findall(r'<img[^>]+>', content)
        for img in img_tags:
            if 'alt=' not in img:
                results['images_with_alt'] = False
                break
        
        return results
        
    except Exception as e:
        print(f"Error checking {filename}: {e}")
        return None

def check_additional_files():
    """Check for additional SEO files"""
    sitemap_exists = os.path.exists(os.path.join(portfolio_dir, "sitemap.xml"))
    robots_exists = os.path.exists(os.path.join(portfolio_dir, "robots.txt"))
    
    return {
        'sitemap': sitemap_exists,
        'robots': robots_exists
    }

def generate_seo_report():
    """Generate comprehensive SEO report"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("🔍 SEO VERIFICATION REPORT")
    print("=" * 80)
    
    all_results = []
    perfect_seo_count = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html']:
            results = check_seo_elements(file_path)
            if results:
                all_results.append(results)
    
    # Print detailed results
    seo_elements = [
        ('title', 'Page Title'),
        ('meta_description', 'Meta Description'),
        ('meta_keywords', 'Meta Keywords'),
        ('meta_author', 'Meta Author'),
        ('canonical', 'Canonical URL'),
        ('og_title', 'Open Graph Title'),
        ('og_description', 'Open Graph Description'),
        ('og_image', 'Open Graph Image'),
        ('twitter_card', 'Twitter Card'),
        ('structured_data', 'Structured Data'),
        ('lang_attribute', 'Language Attribute'),
        ('viewport', 'Viewport Meta'),
        ('charset', 'Character Encoding'),
        ('images_with_alt', 'Image Alt Tags')
    ]
    
    for element_key, element_name in seo_elements:
        print(f"\\n📋 {element_name}:")
        print("-" * 40)
        passed = 0
        for result in all_results:
            status = "✅" if result[element_key] else "❌"
            print(f"{status} {result['file']}")
            if result[element_key]:
                passed += 1
        print(f"   Status: {passed}/{len(all_results)} files optimized")
    
    # Check for perfect SEO scores
    print("\\n🏆 PERFECT SEO SCORES:")
    print("-" * 40)
    for result in all_results:
        score = sum(1 for key in seo_elements if result[key[0]])
        if score == len(seo_elements):
            perfect_seo_count += 1
            print(f"✅ {result['file']} - Perfect SEO (14/14)")
        else:
            print(f"⚠️  {result['file']} - {score}/{len(seo_elements)} elements")
    
    # Check additional files
    additional = check_additional_files()
    print("\\n📁 ADDITIONAL SEO FILES:")
    print("-" * 40)
    print(f"{'✅' if additional['sitemap'] else '❌'} sitemap.xml")
    print(f"{'✅' if additional['robots'] else '❌'} robots.txt")
    
    # Summary
    print("\\n📊 SUMMARY:")
    print("=" * 40)
    print(f"📄 Total HTML files checked: {len(all_results)}")
    print(f"🏆 Perfect SEO scores: {perfect_seo_count}")
    print(f"📋 Average elements per page: {sum(sum(1 for key in seo_elements if result[key[0]]) for result in all_results) / len(all_results):.1f}/14")
    print(f"🗺️  Sitemap available: {'Yes' if additional['sitemap'] else 'No'}")
    print(f"🤖 Robots.txt available: {'Yes' if additional['robots'] else 'No'}")
    
    if perfect_seo_count == len(all_results) and all(additional.values()):
        print("\\n🎉 CONGRATULATIONS! Your portfolio has PERFECT SEO optimization!")
        print("   All pages are fully optimized for search engines.")
    else:
        print(f"\\n💡 Portfolio is {(perfect_seo_count/len(all_results)*100):.1f}% SEO optimized")

if __name__ == "__main__":
    generate_seo_report()
