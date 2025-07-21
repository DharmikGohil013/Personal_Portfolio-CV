#!/usr/bin/env python3
"""
Script to verify that all HTML files have the standardized header
"""

import os
import glob
import re

# Define the directory containing the HTML files
portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

def verify_header_in_file(file_path):
    """Verify that a file has the standard header elements"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for key header elements
        checks = {
            'Header Element': r'<header[^>]*id="header"',
            'Logo': r'<img src="assets/img/dlogo\.png"',
            'Site Name': r'<h1 class="sitename">DHARMIK</h1>',
            'Navigation Menu': r'<nav id="navmenu"',
            'Social Links': r'<div class="header-social-links">',
            'Mobile Toggle': r'<i class="mobile-nav-toggle',
            'Home Link': r'href="https://dharmikgohil\.fun"',
            'Projects Dropdown': r'<span>Projects</span>',
            'Services Section': r'<span style="color: #15ff00;">Services</span>'
        }
        
        results = {}
        for check_name, pattern in checks.items():
            results[check_name] = bool(re.search(pattern, content, re.IGNORECASE))
        
        return results
        
    except Exception as e:
        print(f"✗ Error reading {os.path.basename(file_path)}: {e}")
        return None

def main():
    """Main function to verify headers in all HTML files"""
    # Get all HTML files in the directory
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("Verifying standardized headers across all HTML files...")
    print("=" * 70)
    
    total_files = 0
    perfect_files = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        
        # Skip test files
        if filename in ['loader-test.html', 'premium-loader-template.html']:
            continue
            
        total_files += 1
        
        print(f"\n📄 {filename}")
        print("-" * 50)
        
        results = verify_header_in_file(file_path)
        if results is None:
            continue
        
        all_passed = True
        for check_name, passed in results.items():
            status = "✅" if passed else "❌"
            print(f"  {status} {check_name}")
            if not passed:
                all_passed = False
        
        if all_passed:
            perfect_files += 1
            print(f"  🎉 {filename} - ALL CHECKS PASSED!")
        else:
            print(f"  ⚠️  {filename} - Some checks failed")
    
    print("\n" + "=" * 70)
    print(f"📊 SUMMARY:")
    print(f"   Total files checked: {total_files}")
    print(f"   Perfect headers: {perfect_files}")
    print(f"   Success rate: {(perfect_files/total_files*100):.1f}%")
    
    if perfect_files == total_files:
        print("   🎉 ALL FILES HAVE STANDARDIZED HEADERS!")
    else:
        print(f"   ⚠️  {total_files - perfect_files} files need attention")

if __name__ == "__main__":
    main()
