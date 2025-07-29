#!/usr/bin/env python3
"""
Add Comprehensive Favicon Support - Dharmik Gohil Logo
"""

import os
import glob
import re

portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

def add_comprehensive_favicon(file_path):
    """Add complete favicon implementation using Dharmik's logo"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(file_path)
        
        # Comprehensive favicon HTML with Dharmik's logo
        favicon_html = '''  <!-- Favicons - Dharmik Gohil Logo -->
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
  <meta name="application-name" content="Dharmik Gohil">'''

        # Remove existing favicon section if present
        # Pattern to match from <!-- Favicons --> to the end of favicon links
        favicon_pattern = r'(\s*<!-- Favicons.*?-->\s*(?:<link[^>]*(?:icon|apple-touch-icon)[^>]*>\s*)*)'
        
        if re.search(favicon_pattern, content, re.DOTALL):
            # Replace existing favicon section
            content = re.sub(favicon_pattern, '\n' + favicon_html + '\n', content, flags=re.DOTALL)
        else:
            # If no favicon section exists, add before <!-- Fonts --> or before </head>
            if '<!-- Fonts -->' in content:
                content = content.replace('  <!-- Fonts -->', favicon_html + '\n\n  <!-- Fonts -->')
            elif '</head>' in content:
                content = content.replace('</head>', favicon_html + '\n</head>')
        
        # Ensure proper spacing
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"Error adding favicon to {filename}: {e}")
        return False

def verify_favicon_implementation():
    """Verify favicon implementation across all pages"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("\n🔍 VERIFYING FAVICON IMPLEMENTATION...")
    print("-" * 50)
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html']:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                favicon_count = len(re.findall(r'rel="(?:icon|apple-touch-icon|shortcut icon)"', content))
                theme_color = 'theme-color' in content
                msapp_tile = 'msapplication-TileImage' in content
                
                status = "✅ COMPLETE" if favicon_count >= 10 and theme_color and msapp_tile else "⚠️ PARTIAL"
                print(f"{status} {filename}: {favicon_count} favicon links, Theme: {theme_color}, MS Tile: {msapp_tile}")
                
            except Exception as e:
                print(f"❌ ERROR {filename}: {e}")

def main():
    """Add comprehensive favicon support to all HTML pages"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("🎨 ADDING COMPREHENSIVE FAVICON SUPPORT...")
    print("📱 Using Dharmik Gohil Logo (dlogo.png)")
    print("-" * 50)
    
    updated_count = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html']:
            if add_comprehensive_favicon(file_path):
                print(f"✅ Added comprehensive favicon to {filename}")
                updated_count += 1
    
    print(f"\n🏆 SUCCESS! Updated {updated_count} pages with comprehensive favicon support")
    
    # Verify implementation
    verify_favicon_implementation()
    
    print("\n🎯 FAVICON FEATURES ADDED:")
    print("✅ Multiple icon sizes (16x16, 32x32)")
    print("✅ Apple Touch Icons (all sizes)")
    print("✅ Microsoft Tile support")
    print("✅ Theme color configuration")
    print("✅ Application name metadata")
    print("✅ Cross-platform compatibility")
    
    print("\n🚀 Your Dharmik Gohil logo is now the favicon across your entire website!")
    print("📱 Works on: Desktop browsers, Mobile devices, iOS, Android, Windows tiles")

if __name__ == "__main__":
    main()
