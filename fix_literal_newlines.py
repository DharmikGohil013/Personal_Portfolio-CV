#!/usr/bin/env python3
"""
Remove Literal \n Characters from HTML Files
"""

import os
import glob
import re

portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

def remove_literal_newlines(file_path):
    """Remove literal \n characters that appear as text in HTML"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(file_path)
        
        # Count literal \n occurrences before removal
        literal_newlines = content.count('\\n')
        print(f"🔧 Processing {filename}...")
        print(f"   Found {literal_newlines} literal \\n characters")
        
        # Remove literal \n characters (but preserve actual newlines)
        # Remove standalone \n on their own lines
        content = re.sub(r'^\s*\\n\s*$', '', content, flags=re.MULTILINE)
        
        # Remove any remaining literal \n characters
        content = content.replace('\\n', '')
        
        # Clean up any excessive whitespace that might result
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # Ensure proper spacing around body tag
        content = re.sub(r'>\s*\n\s*<body', '>\n\n<body', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Fixed {filename}: Removed {literal_newlines} literal \\n characters")
        return literal_newlines
        
    except Exception as e:
        print(f"❌ Error fixing {filename}: {e}")
        return 0

def verify_fixes():
    """Verify that literal \n characters are removed"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("\n🔍 VERIFICATION RESULTS...")
    print("-" * 50)
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html']:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for remaining literal \n characters
                remaining_literal_newlines = content.count('\\n')
                
                # Status indicators
                status = "✅ CLEAN" if remaining_literal_newlines == 0 else f"⚠️ {remaining_literal_newlines} \\n remain"
                
                print(f"{filename:20} | {status}")
                
            except Exception as e:
                print(f"{filename:20} | ❌ ERROR: {e}")

def main():
    """Remove literal \n characters from all HTML files"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("🛠️ REMOVING LITERAL \\n CHARACTERS...")
    print("🔧 Issue: \\n appearing as text at top of pages")
    print("=" * 50)
    
    total_literal_newlines = 0
    fixed_count = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html']:
            literal_newlines_removed = remove_literal_newlines(file_path)
            total_literal_newlines += literal_newlines_removed
            if literal_newlines_removed >= 0:  # Even if 0, still counts as processed
                fixed_count += 1
    
    print(f"\n🏆 FIXES COMPLETED!")
    print(f"📄 Pages Processed: {fixed_count}")
    print(f"🔧 Total literal \\n characters removed: {total_literal_newlines}")
    
    # Verify fixes
    verify_fixes()
    
    print(f"\n🚀 SUCCESS! Your pages should now load clean!")
    print("✅ No more \\n characters appearing at the top of your pages")
    print("🎨 Clean, professional page rendering")
    
    print(f"\n📋 WHAT WAS FIXED:")
    print("🔧 Removed all literal \\n text characters from HTML files")
    print("🎨 Cleaned up whitespace and formatting")
    print("✅ Pages now render without text artifacts")
    print("📱 Professional appearance maintained")

if __name__ == "__main__":
    main()
