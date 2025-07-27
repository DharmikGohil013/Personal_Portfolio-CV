#!/usr/bin/env python3
"""
Optimize alt tags for better SEO and accessibility
"""

import os
import glob
import re

portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

# Specific alt text mappings for better SEO
alt_mappings = {
    'dlogo.png': 'Dharmik Gohil Logo - Game Developer',
    'DharmikGohil (1).png': 'Dharmik Gohil - Professional Game Developer Profile Picture',
    'DharmikGohil (1).webp': 'Dharmik Gohil - Game Developer Portfolio Photo',
    'profile-img.jpg': 'Dharmik Gohil Professional Profile Image',
    'hero-bg.jpg': 'Game Development Background - Gaming Environment',
    'game1 (1).png': 'Floppy Bird Game Screenshot - Unity Mobile Game',
    'game1 (2).png': 'Floppy Bird Gameplay - Mobile Gaming Experience',
    'game1 (3).png': 'Floppy Bird Game Interface - Unity Development',
    'game1 (4).png': 'Floppy Bird Score Screen - Gaming Achievement',
    'game1 (5).png': 'Floppy Bird Game Menu - User Interface Design',
    'game1 (6).png': 'Floppy Bird Gameplay Features - Mobile Game Development',
    '2 (1).png': 'Cross Out Game Screenshot - Strategic Puzzle Game',
    '2 (2).png': 'Cross Out Gameplay Interface - Unity Game Development',
    '2 (3).png': 'Cross Out Game Strategy - Puzzle Mechanics',
    '2 (4).png': 'Cross Out Game Features - Interactive Gaming',
    '2 (6).png': 'Cross Out Game Development - Unity Project',
    '2 (7).png': 'Cross Out Game Design - User Interface',
    '2 (8).png': 'Cross Out Gameplay Elements - Game Mechanics',
    '2 (9).png': 'Cross Out Game Achievement - Gaming Success',
    'multi.webp': 'Mavericks Battlegrounds - Multiplayer Game Development',
    'Unity.webp': 'Unity Game Engine - Game Development Platform',
    'Subject-Game-Development.webp': 'Game Development Education - Learning Unity',
    'C_Programming_Language.svg.png': 'C Programming Language - Software Development Skills',
    'C++_logo.png': 'C++ Programming - Game Development Language',
    'Python-logo-notext.svg.png': 'Python Programming - Web Development Skills',
    'js.png': 'JavaScript Programming - Web Development Technology',
    'node.png': 'Node.js Development - Backend Programming',
    'mongodb.svg': 'MongoDB Database - Web Development Technology',
    'Mysql_logo.png': 'MySQL Database - Data Management Skills',
    'man-wearing-vr-goggles-gaming.jpg': 'Virtual Reality Gaming - VR Development Experience',
    '21858352_6537974.svg': 'AR/VR Technology - Immersive Experience Development'
}

def optimize_image_alt_tags(file_path):
    """Optimize alt tags in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find all img tags
        img_pattern = r'<img([^>]+)>'
        
        def improve_alt_tag(match):
            img_tag = match.group(1)
            
            # Extract src attribute
            src_match = re.search(r'src="([^"]*)"', img_tag)
            if not src_match:
                return match.group(0)
            
            src = src_match.group(1)
            filename = os.path.basename(src)
            
            # Check if alt attribute exists
            alt_match = re.search(r'alt="([^"]*)"', img_tag)
            
            # Get optimized alt text
            if filename in alt_mappings:
                new_alt = alt_mappings[filename]
            else:
                # Generate descriptive alt text from filename
                base_name = os.path.splitext(filename)[0]
                new_alt = base_name.replace('-', ' ').replace('_', ' ').replace('(', '').replace(')', '').title()
                if 'game' in base_name.lower():
                    new_alt += ' - Game Development Project'
                elif any(tech in base_name.lower() for tech in ['unity', 'js', 'python', 'node', 'mysql', 'mongodb']):
                    new_alt += ' - Programming Technology'
                else:
                    new_alt += ' - Dharmik Gohil Portfolio'
            
            # Update or add alt attribute
            if alt_match:
                # Replace existing alt
                new_img_tag = re.sub(r'alt="[^"]*"', f'alt="{new_alt}"', img_tag)
            else:
                # Add alt attribute
                new_img_tag = img_tag + f' alt="{new_alt}"'
            
            return f'<img{new_img_tag}>'
        
        # Apply improvements
        content = re.sub(img_pattern, improve_alt_tag, content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"Error optimizing {os.path.basename(file_path)}: {e}")
        return False

def main():
    """Optimize alt tags in all HTML files"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("🖼️ Optimizing image alt tags for SEO and accessibility...")
    print("-" * 60)
    
    optimized_count = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html']:
            if optimize_image_alt_tags(file_path):
                print(f"✅ Optimized alt tags in {filename}")
                optimized_count += 1
    
    print(f"\\n📊 Alt tag optimization complete: {optimized_count} files processed")

if __name__ == "__main__":
    main()
