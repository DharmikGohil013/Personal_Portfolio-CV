#!/usr/bin/env python3
"""
Add Favicon to All Pages - Quick Fix
"""

import os
import glob
import re

portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

def add_favicon_to_page(file_path):
    """Add favicon section to HTML page"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(file_path)
        
        # Skip if already has favicon
        if 'Favicons - Dharmik Gohil Logo' in content:
            print(f"✅ {filename} already has favicon")
            return True
        
        # Favicon HTML
        favicon_html = '''
  <!-- Favicons - Dharmik Gohil Logo -->
  <link rel="icon" type="image/png" sizes="32x32" href="assets/img/dlogo.png">
  <link rel="icon" type="image/png" sizes="16x16" href="assets/img/dlogo.png">
  <link rel="shortcut icon" href="assets/img/dlogo.png">
  <link rel="apple-touch-icon" sizes="180x180" href="assets/img/dlogo.png">
  <link rel="apple-touch-icon" sizes="152x152" href="assets/img/dlogo.png">
  <link rel="apple-touch-icon" sizes="144x144" href="assets/img/dlogo.png">
  <link rel="apple-touch-icon" sizes="120x120" href="assets/img/dlogo.png">
  <link rel="apple-touch-icon" sizes="114x114" href="assets/img/dlogo.png">
  <link rel="apple-touch-icon" sizes="76x76" href="assets/img/dlogo.png">
  <link rel="apple-touch-icon" sizes="72x72" href="assets/img/dlogo.png">
  <link rel="apple-touch-icon" sizes="60x60" href="assets/img/dlogo.png">
  <link rel="apple-touch-icon" sizes="57x57" href="assets/img/dlogo.png">
  <meta name="msapplication-TileImage" content="assets/img/dlogo.png">
  <meta name="msapplication-TileColor" content="#2d89ef">
  <meta name="theme-color" content="#2d89ef">
  <meta name="apple-mobile-web-app-title" content="Dharmik Gohil">
  <meta name="application-name" content="Dharmik Gohil">
'''

        # Try multiple insertion points
        insertion_points = [
            (r'(.*<meta property="twitter:creator"[^>]*>)', r'\1' + favicon_html),
            (r'(.*<!-- Fonts -->)', favicon_html + r'\n\1'),
            (r'(.*<link href="https://fonts\.googleapis\.com")', favicon_html + r'\n  \1'),
            (r'(.*</head>)', favicon_html + r'\n\1')
        ]
        
        inserted = False
        for pattern, replacement in insertion_points:
            if re.search(pattern, content, re.DOTALL):
                content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)
                inserted = True
                break
        
        if not inserted:
            print(f"⚠️ Could not find insertion point in {filename}")
            return False
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Added favicon to {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Error with {filename}: {e}")
        return False

def main():
    """Add favicon to all HTML pages"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("🎨 ADDING FAVICON TO ALL PAGES...")
    print("-" * 40)
    
    success_count = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html']:
            if add_favicon_to_page(file_path):
                success_count += 1
    
    print(f"\n🏆 SUCCESS! Added favicon to {success_count} pages")
    
    # Verify
    print("\n🔍 VERIFICATION...")
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html']:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                has_favicon_comment = 'Favicons - Dharmik Gohil Logo' in content
                has_dlogo = 'dlogo.png' in content
                favicon_links = len(re.findall(r'rel="(?:icon|apple-touch-icon|shortcut icon)"', content))
                
                status = "✅ COMPLETE" if has_favicon_comment and favicon_links >= 10 else "❌ MISSING"
                print(f"{filename:15} | {status} | {favicon_links} links")
                
            except Exception as e:
                print(f"{filename:15} | ❌ ERROR")

if __name__ == "__main__":
    main()
