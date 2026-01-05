#!/usr/bin/env python3
"""
Update Google Analytics Measurement ID
Updates all HTML files with new Google Analytics tracking code
Old ID: G-B2T6PJQMCJ → New ID: G-KHJXN2DGEE
"""

import os
from pathlib import Path

# Configuration
OLD_GA_ID = "G-B2T6PJQMCJ"
NEW_GA_ID = "G-KHJXN2DGEE"
WORKSPACE_PATH = Path(__file__).parent

def update_google_analytics():
    """Update Google Analytics ID in all HTML files"""
    
    # Find all HTML files
    html_files = list(WORKSPACE_PATH.glob('*.html')) + list(WORKSPACE_PATH.glob('blog/*.html'))
    
    updated_files = []
    total_replacements = 0
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file contains old GA ID
            if OLD_GA_ID in content:
                # Count replacements
                count = content.count(OLD_GA_ID)
                
                # Replace old ID with new ID
                updated_content = content.replace(OLD_GA_ID, NEW_GA_ID)
                
                # Write back to file
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                
                updated_files.append(str(html_file.relative_to(WORKSPACE_PATH)))
                total_replacements += count
                
        except Exception as e:
            print(f"Error processing {html_file}: {e}")
    
    return updated_files, total_replacements

def main():
    """Main execution"""
    print("=" * 70)
    print("Google Analytics Measurement ID Update")
    print("=" * 70)
    print(f"\nOld Measurement ID: {OLD_GA_ID}")
    print(f"New Measurement ID: {NEW_GA_ID}")
    print("\nUpdating HTML files...\n")
    
    updated_files, total_replacements = update_google_analytics()
    
    print(f"✅ Updated {len(updated_files)} files")
    print(f"✅ Total replacements: {total_replacements}")
    
    if updated_files:
        print("\n📄 Updated Files:")
        for file in sorted(updated_files):
            print(f"   - {file}")
    
    print("\n" + "=" * 70)
    print("✅ Google Analytics Update Complete!")
    print("=" * 70)
    print(f"\n📊 Your new GA4 tracking is live!")
    print(f"🔗 Measurement ID: {NEW_GA_ID}")
    print(f"🌐 Stream URL: https://dharmikgohil.art/")
    print("\n💡 Next Steps:")
    print("   1. Verify tracking in Google Analytics (Real-time reports)")
    print("   2. Check data collection is working")
    print("   3. Set up conversion goals")
    print("   4. Configure custom events if needed")
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
