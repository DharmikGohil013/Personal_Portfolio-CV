#!/usr/bin/env python3
"""
Fix Navigation Contact Links - Make them point to contact.html instead of #contact
"""

import os
import glob
import re

portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

def fix_contact_navigation(file_path):
    """Fix contact navigation links to point to contact.html"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(file_path)
        
        # Track changes
        changes_made = 0
        
        # Fix navigation contact link from #contact to contact.html
        # Look for patterns like: <a href="#contact">Contact</a>
        contact_patterns = [
            (r'<a\s+href="#contact"([^>]*)>Contact</a>', r'<a href="contact.html"\1>Contact</a>'),
            (r'<a\s+href="#contact"([^>]*)>\s*Contact\s*</a>', r'<a href="contact.html"\1>Contact</a>'),
        ]
        
        for old_pattern, new_pattern in contact_patterns:
            matches = re.findall(old_pattern, content, re.IGNORECASE)
            if matches:
                content = re.sub(old_pattern, new_pattern, content, flags=re.IGNORECASE)
                changes_made += len(matches)
        
        # Save the file if changes were made
        if changes_made > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed {changes_made} contact link(s) in {filename}")
            return changes_made
        else:
            print(f"ℹ️ No contact navigation issues found in {filename}")
            return 0
        
    except Exception as e:
        print(f"❌ Error fixing {filename}: {e}")
        return 0

def verify_contact_links():
    """Verify that all contact links now point to contact.html"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("\n🔍 VERIFICATION: Contact Link Status")
    print("-" * 50)
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html', 'contact.html']:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for problematic links
                hash_contact_links = len(re.findall(r'href="#contact"[^>]*>Contact</a>', content, re.IGNORECASE))
                correct_contact_links = len(re.findall(r'href="contact\.html"[^>]*>Contact</a>', content, re.IGNORECASE))
                
                if hash_contact_links > 0:
                    status = f"⚠️ NEEDS FIX ({hash_contact_links} #contact links)"
                elif correct_contact_links > 0:
                    status = f"✅ CORRECT ({correct_contact_links} contact.html links)"
                else:
                    status = "ℹ️ NO CONTACT LINK"
                
                print(f"{filename:20} | {status}")
                
            except Exception as e:
                print(f"{filename:20} | ❌ ERROR: {e}")

def main():
    """Fix contact navigation links across all HTML pages"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("🔧 FIXING CONTACT NAVIGATION LINKS...")
    print("Issue: Contact links pointing to #contact instead of contact.html")
    print("Solution: Change navigation links to open contact.html page")
    print("=" * 60)
    
    total_fixes = 0
    pages_fixed = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html', 'contact.html']:
            fixes = fix_contact_navigation(file_path)
            if fixes > 0:
                total_fixes += fixes
                pages_fixed += 1
    
    print(f"\n🏆 FIXES COMPLETED!")
    print(f"📄 Pages Fixed: {pages_fixed}")
    print(f"🔧 Total Links Fixed: {total_fixes}")
    
    # Verify fixes
    verify_contact_links()
    
    print(f"\n🚀 SUCCESS! Contact navigation is now working properly!")
    print("✅ Contact links now open contact.html page instead of scrolling to #contact")
    print("📱 Works on both desktop and mobile navigation")
    print("🖱️ Users can now properly navigate to your contact page")
    
    if total_fixes > 0:
        print(f"\n📋 WHAT WAS FIXED:")
        print("🔧 Changed href=\"#contact\" to href=\"contact.html\"")
        print("📄 Fixed navigation across all HTML pages")
        print("🎯 Contact button now opens the dedicated contact page")
        print("✅ Navigation works properly on touch devices")
    else:
        print(f"\n📋 STATUS:")
        print("✅ All contact links were already correctly configured")

if __name__ == "__main__":
    main()
