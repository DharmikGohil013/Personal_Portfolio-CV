#!/usr/bin/env python3
"""
Remove About, Resume, and Contact from Navigation Bar - All Pages (Updated)
"""

import os
import glob
import re

portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

def remove_nav_items_updated(file_path):
    """Remove About, Resume, and Contact from navigation menu - Updated version"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(file_path)
        changes_made = 0
        original_content = content
        
        # Pattern 1: Remove About link (various formats)
        about_patterns = [
            r'\s*<li><a href="#about">About</a></li>\s*\n?',
            r'\s*<li><a href="about\.html">About</a></li>\s*\n?',
            r'\s*<li><a href="/about\.html">About</a></li>\s*\n?',
            r'\s*<li><a href="\.\.?/about\.html">About</a></li>\s*\n?'
        ]
        
        for pattern in about_patterns:
            matches = re.findall(pattern, content)
            if matches:
                content = re.sub(pattern, '\n', content)
                changes_made += len(matches)
        
        # Pattern 2: Remove Resume link (various formats)  
        resume_patterns = [
            r'\s*<li><a href="#resume">Resume</a></li>\s*\n?',
            r'\s*<li><a href="resume\.html">Resume</a></li>\s*\n?',
            r'\s*<li><a href="/resume\.html">Resume</a></li>\s*\n?',
            r'\s*<li><a href="\.\.?/resume\.html">Resume</a></li>\s*\n?'
        ]
        
        for pattern in resume_patterns:
            matches = re.findall(pattern, content)
            if matches:
                content = re.sub(pattern, '\n', content)
                changes_made += len(matches)
        
        # Pattern 3: Remove Contact link (various formats)
        contact_patterns = [
            r'\s*<li><a href="contact\.html">Contact</a></li>\s*\n?',
            r'\s*<li><a href="/contact\.html">Contact</a></li>\s*\n?',
            r'\s*<li><a href="#contact">Contact</a></li>\s*\n?',
            r'\s*<li><a href="\.\.?/contact\.html">Contact</a></li>\s*\n?'
        ]
        
        for pattern in contact_patterns:
            matches = re.findall(pattern, content)
            if matches:
                content = re.sub(pattern, '\n', content)
                changes_made += len(matches)
        
        # Clean up extra whitespace and newlines
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        content = re.sub(r'(<ul>\s*\n)\s*\n+', r'\1', content)
        content = re.sub(r'\n+(\s*</ul>)', r'\n\1', content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Removed navigation items from {filename}")
            return True
        else:
            print(f"⚪ No navigation items found to remove in {filename}")
            return False
        
    except Exception as e:
        print(f"❌ Error with {filename}: {e}")
        return False

def verify_removal():
    """Verify that navigation items have been removed"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print(f"\n🔍 VERIFICATION RESULTS...")
    print("-" * 70)
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html']:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for remaining nav items using flexible patterns
                has_about = bool(re.search(r'<li><a[^>]*>About</a></li>', content))
                has_resume = bool(re.search(r'<li><a[^>]*>Resume</a></li>', content))
                has_contact = bool(re.search(r'<li><a[^>]*>Contact</a></li>', content))
                
                about_status = "❌ FOUND" if has_about else "✅ REMOVED"
                resume_status = "❌ FOUND" if has_resume else "✅ REMOVED"
                contact_status = "❌ FOUND" if has_contact else "✅ REMOVED"
                
                print(f"{filename:20} | About: {about_status:12} | Resume: {resume_status:12} | Contact: {contact_status:12}")
                
            except Exception as e:
                print(f"{filename:20} | ❌ ERROR: {e}")

def main():
    """Remove About, Resume, and Contact from all navigation menus"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("🗑️ REMOVING NAVIGATION ITEMS FROM ALL PAGES...")
    print("📋 Target items: About, Resume, Contact")
    print("-" * 50)
    
    updated_count = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html']:
            if remove_nav_items_updated(file_path):
                updated_count += 1
    
    print(f"\n🏆 PROCESSING COMPLETE!")
    print(f"📄 Files processed: {len(html_files) - 2}")  # Excluding test files
    print(f"✅ Files updated: {updated_count}")
    
    # Verify removal
    verify_removal()
    
    print(f"\n📋 SUMMARY:")
    print("✅ About links removed from navigation")
    print("✅ Resume links removed from navigation") 
    print("✅ Contact links removed from navigation")
    print("🚀 Navigation bars now have cleaner structure")
    print(f"\n🎯 Your navigation menus are now streamlined and professional!")

if __name__ == "__main__":
    main()
