#!/usr/bin/env python3
"""
Add Protected Access Service to All Navigation Menus
"""

import os
import glob
import re

portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

def add_protected_access_service(file_path):
    """Add protected access service to services dropdown menu"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(file_path)
        
        # Skip if already has protected access
        if 'Protected Access' in content:
            print(f"✅ {filename} already has Protected Access service")
            return True
        
        # Pattern to find services dropdown and add the protected access service
        services_pattern = r'(<li><a href="https://learnlink\.dharmikgohil\.fun"[^>]*>Learn Link</a></li>\s*)(</ul>)'
        
        if re.search(services_pattern, content):
            # Add protected access service before closing </ul>
            replacement = r'\1    <li><a href="protected-access.html">🔐 Protected Access</a></li> <!-- ✅ NEW PASSWORD PROTECTED SERVICE -->\n    \n  \2'
            content = re.sub(services_pattern, replacement, content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Added Protected Access service to {filename}")
            return True
        else:
            print(f"⚠️ Services dropdown not found in {filename}")
            return False
        
    except Exception as e:
        print(f"❌ Error with {filename}: {e}")
        return False

def main():
    """Add protected access service to all HTML pages"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("🔐 ADDING PROTECTED ACCESS SERVICE TO ALL PAGES...")
    print("-" * 50)
    
    success_count = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html', 'protected-access.html']:
            if add_protected_access_service(file_path):
                success_count += 1
    
    print(f"\n🏆 SUCCESS! Added Protected Access service to navigation menus")
    print(f"📄 Pages updated: {success_count}")
    
    # Verify
    print(f"\n🔍 VERIFICATION...")
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html']:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                has_protected_access = 'Protected Access' in content
                status = "✅ HAS SERVICE" if has_protected_access else "❌ MISSING"
                print(f"{filename:20} | {status}")
                
            except Exception as e:
                print(f"{filename:20} | ❌ ERROR")

if __name__ == "__main__":
    main()
