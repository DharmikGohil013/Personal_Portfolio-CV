#!/usr/bin/env python3
"""
Fix HTML lang attributes that may have been malformed during SEO optimization
"""

import os
import glob
import re

portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

def fix_lang_attribute(file_path):
    """Fix malformed lang attribute in HTML files"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix malformed lang attribute
        content = re.sub(r'<html\\1 lang="en">', '<html lang="en">', content)
        content = re.sub(r'<html([^>]*?)\\1 lang="en">', r'<html\1 lang="en">', content)
        
        # Also ensure proper lang attribute if missing
        if 'lang=' not in content:
            content = re.sub(r'<html([^>]*)>', r'<html\1 lang="en">', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error fixing {os.path.basename(file_path)}: {e}")
        return False

def main():
    """Fix lang attributes in all HTML files"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html']:
            if fix_lang_attribute(file_path):
                print(f"✅ Fixed lang attribute in {filename}")

if __name__ == "__main__":
    main()
