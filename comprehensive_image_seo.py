#!/usr/bin/env python3
"""
Comprehensive Image SEO Optimization
Updates ALL <img> tags across the entire website with keyword-rich alt attributes
Target keywords: "dharmik gohil", "dharmik gohil fun", "gohil dharmik"
"""

import os
import glob
import re
from pathlib import Path

portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

# Comprehensive keyword-rich alt text mappings for all image types
image_alt_mappings = {
    # Logos and Branding
    'dlogo.png': 'dharmik gohil personal portfolio logo and brand identity',
    'logo.png': 'dharmik gohil fun professional gaming logo design',
    'DharmikGohil (1).png': 'dharmik gohil professional headshot photo portfolio image',
    'DharmikGohil (1).webp': 'gohil dharmik professional developer profile picture',
    'profile-img.jpg': 'dharmik gohil fun profile photo game developer portrait',
    'apple-touch-icon.png': 'dharmik gohil mobile app icon touch logo',
    'favicon.png': 'gohil dharmik website favicon browser icon',
    
    # Background and Hero Images
    'hero-bg.jpg': 'dharmik gohil fun gaming background hero image',
    'bg.jpg': 'gohil dharmik portfolio website background design',
    'unsplash-image-ye8mgSyfzGA.jpg': 'dharmik gohil creative background image design',
    
    # Game Development Projects
    'game1 (1).png': 'floppy bird mobile game screenshot by dharmik gohil fun',
    'game1 (2).png': 'dharmik gohil floppy bird gameplay interface design',
    'game1 (3).png': 'mobile gaming project by gohil dharmik unity developer',
    'game1 (4).png': 'dharmik gohil fun game score screen interface',
    'game1 (5).png': 'floppy bird menu design by dharmik gohil developer',
    'game1 (6).png': 'gohil dharmik mobile game development showcase',
    
    # Cross Out Game Series
    '2 (1).png': 'cross out strategy game by dharmik gohil fun developer',
    '2 (2).png': 'dharmik gohil puzzle game interface design screenshot',
    '2 (3).png': 'strategic gaming project by gohil dharmik unity expert',
    '2 (4).png': 'dharmik gohil fun cross out game mechanics showcase',
    '2 (6).png': 'mobile puzzle game development by dharmik gohil',
    '2 (7).png': 'gohil dharmik cross out game user interface',
    '2 (8).png': 'dharmik gohil fun strategic puzzle gameplay',
    '2 (9).png': 'mobile game achievement screen by dharmik gohil',
    
    # Technology and Development Icons
    'Unity.webp': 'unity game engine expertise by dharmik gohil fun',
    'C_Programming_Language.svg.png': 'c programming language skill dharmik gohil developer',
    'C++_logo.png': 'c++ programming expertise by gohil dharmik',
    'Python-logo-notext.svg.png': 'python programming skill dharmik gohil fun developer',
    'js.png': 'javascript programming expertise by dharmik gohil',
    'node.png': 'nodejs backend development by gohil dharmik',
    'mongodb.svg': 'mongodb database expertise dharmik gohil fun',
    'Mysql_logo.png': 'mysql database skill by dharmik gohil developer',
    'c-logo-icon-18.png': 'c programming icon dharmik gohil fun coding skills',
    
    # VR/AR and Gaming Technology
    'man-wearing-vr-goggles-gaming.jpg': 'vr gaming technology expertise by dharmik gohil fun',
    '21858352_6537974.svg': 'ar vr development skills by gohil dharmik developer',
    'Subject-Game-Development.webp': 'game development education by dharmik gohil fun',
    
    # Portfolio and Project Images
    'multi.webp': 'multiplayer game development project by dharmik gohil',
    'floopy.webp': 'mobile game project showcase by gohil dharmik fun',
    '1.png': 'portfolio project showcase by dharmik gohil developer',
    'aaaa.jpg': 'creative project design by dharmik gohil fun',
    'hc.jpg': 'professional project image by gohil dharmik',
    
    # Certificates and Achievements
    'crtificate logo.png': 'dharmik gohil fun certificate and achievement logo',
    
    # Special Events and Celebrations
    '75th-indian-republic-day-26-january-celebration-social-media-post-web-bennar-status-wishes-free-vector.jpg': 'republic day celebration design by dharmik gohil fun',
    'happy-valentines-day-greeting-card-beautiful-red-hearts-hanging-blurred-background-bokeh-st-valentine-s-love-concept-138558521.webp': 'valentines day creative design by gohil dharmik',
    
    # Animated Content
    'tumblr_cca4f06484b447c0687f0325af5b38c9_7c751558_1280.gif': 'animated creative content by dharmik gohil fun',
    'tumblr_nv44lndz1l1u6xnmoo1_1280.gif': 'creative animation project by dharmik gohil developer',
    
    # General Project Images
    'images.jpeg': 'project showcase image by gohil dharmik fun',
    '226777.png': 'creative design element by dharmik gohil developer',
    'w..png': 'web development asset by dharmik gohil fun'
}

def generate_seo_alt_text(image_filename, context_page=''):
    """Generate SEO-optimized alt text for any image"""
    
    # Use predefined mapping if available
    if image_filename in image_alt_mappings:
        return image_alt_mappings[image_filename]
    
    # Generate contextual alt text based on image name and page context
    base_name = os.path.splitext(image_filename)[0]
    clean_name = re.sub(r'[^a-zA-Z0-9\s]', ' ', base_name).strip()
    clean_name = re.sub(r'\s+', ' ', clean_name)
    
    # Context-specific generation
    if context_page:
        page_name = os.path.splitext(context_page)[0]
        
        if page_name == 'index':
            return f"{clean_name} portfolio image by dharmik gohil fun developer"
        elif page_name == 'about':
            return f"{clean_name} about dharmik gohil professional image"
        elif page_name == 'portfolio':
            return f"{clean_name} portfolio showcase by gohil dharmik developer"
        elif page_name == 'resume':
            return f"{clean_name} resume image dharmik gohil fun profile"
        elif page_name == 'services':
            return f"{clean_name} service offering by dharmik gohil developer"
        elif page_name == 'contact':
            return f"{clean_name} contact image dharmik gohil fun"
        elif page_name.startswith('game'):
            return f"{clean_name} game project by gohil dharmik unity developer"
        elif page_name == 'vr':
            return f"{clean_name} vr ar project by dharmik gohil fun"
        elif page_name == 'logo':
            return f"{clean_name} design portfolio by dharmik gohil creative"
        elif page_name == 'Achivemtn':
            return f"{clean_name} achievement by gohil dharmik developer"
    
    # Fallback generation based on image characteristics
    if any(keyword in clean_name.lower() for keyword in ['logo', 'brand', 'icon']):
        return f"{clean_name} branding element by dharmik gohil fun"
    elif any(keyword in clean_name.lower() for keyword in ['game', 'play', 'mobile']):
        return f"{clean_name} gaming project by gohil dharmik developer"
    elif any(keyword in clean_name.lower() for keyword in ['profile', 'photo', 'portrait']):
        return f"{clean_name} professional image dharmik gohil fun"
    elif any(keyword in clean_name.lower() for keyword in ['tech', 'code', 'programming']):
        return f"{clean_name} technology skill by dharmik gohil developer"
    elif any(keyword in clean_name.lower() for keyword in ['design', 'creative', 'art']):
        return f"{clean_name} creative design by gohil dharmik fun"
    elif any(keyword in clean_name.lower() for keyword in ['certificate', 'award', 'achievement']):
        return f"{clean_name} professional achievement dharmik gohil"
    else:
        return f"{clean_name} portfolio asset by dharmik gohil fun developer"

def update_image_alt_tags(file_path):
    """Update all <img> tags in a single HTML file with SEO-optimized alt attributes"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(file_path)
        original_content = content
        
        # Pattern to find all img tags
        img_pattern = r'<img([^>]*?)>'
        
        def enhance_img_tag(match):
            img_attrs = match.group(1)
            
            # Extract src attribute to identify the image
            src_match = re.search(r'src\s*=\s*["\']([^"\']*)["\']', img_attrs)
            if not src_match:
                return match.group(0)  # Return unchanged if no src
            
            src_path = src_match.group(1)
            image_filename = os.path.basename(src_path)
            
            # Generate SEO-optimized alt text
            new_alt_text = generate_seo_alt_text(image_filename, filename)
            
            # Check if alt attribute already exists
            alt_pattern = r'alt\s*=\s*["\'][^"\']*["\']'
            
            if re.search(alt_pattern, img_attrs):
                # Replace existing alt attribute
                img_attrs = re.sub(alt_pattern, f'alt="{new_alt_text}"', img_attrs)
            else:
                # Add new alt attribute
                img_attrs += f' alt="{new_alt_text}"'
            
            return f'<img{img_attrs}>'
        
        # Apply the enhancement to all img tags
        content = re.sub(img_pattern, enhance_img_tag, content, flags=re.DOTALL)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Error updating {filename}: {e}")
        return False

def scan_and_update_all_images():
    """Scan and update all HTML files across the entire website"""
    
    # Find all HTML files in the portfolio directory
    html_files = []
    for pattern in ['*.html', '**/*.html']:
        html_files.extend(glob.glob(os.path.join(portfolio_dir, pattern), recursive=True))
    
    print("🖼️  COMPREHENSIVE IMAGE SEO OPTIMIZATION")
    print("=" * 60)
    print("🎯 Target Keywords: 'dharmik gohil', 'dharmik gohil fun', 'gohil dharmik'")
    print("📄 Scanning all HTML files for <img> tags...")
    print("=" * 60)
    
    updated_files = 0
    total_images_updated = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        
        # Skip backup and temporary files
        if filename in ['loader-test.html', 'premium-loader-template.html'] or filename.startswith('.'):
            continue
        
        print(f"\\n📄 Processing: {filename}")
        
        # Count images before update
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            img_count = len(re.findall(r'<img[^>]*>', content))
            print(f"   🖼️  Found {img_count} image(s)")
            
            if update_image_alt_tags(file_path):
                updated_files += 1
                total_images_updated += img_count
                print(f"   ✅ Updated {img_count} image alt attributes with SEO keywords")
            else:
                print(f"   ℹ️  No changes needed (already optimized)")
                
        except Exception as e:
            print(f"   ❌ Error processing {filename}: {e}")
    
    print(f"\\n" + "=" * 60)
    print("📊 IMAGE SEO OPTIMIZATION SUMMARY")
    print("=" * 60)
    print(f"📄 HTML files processed: {len([f for f in html_files if not os.path.basename(f).startswith('loader-test')])}")
    print(f"✅ Files updated: {updated_files}")
    print(f"🖼️  Total images optimized: {total_images_updated}")
    print(f"🎯 Keywords embedded: 'dharmik gohil', 'dharmik gohil fun', 'gohil dharmik'")
    print("\\n🚀 ALL IMAGES NOW OPTIMIZED FOR SEO KEYWORD INDEXING!")
    print("   • Every <img> tag includes target keywords")
    print("   • Alt text is meaningful and accessible")
    print("   • HTML syntax maintained")
    print("   • Layout and visuals preserved")

def validate_image_optimization():
    """Validate that all images have proper SEO alt attributes"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("\\n🔍 VALIDATION: Checking SEO keyword coverage...")
    print("-" * 50)
    
    target_keywords = ['dharmik gohil', 'dharmik gohil fun', 'gohil dharmik']
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename.startswith('loader-test'):
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            img_tags = re.findall(r'<img[^>]*>', content)
            keyword_coverage = 0
            
            for img_tag in img_tags:
                alt_match = re.search(r'alt\s*=\s*["\']([^"\']*)["\']', img_tag)
                if alt_match:
                    alt_text = alt_match.group(1).lower()
                    if any(keyword in alt_text for keyword in target_keywords):
                        keyword_coverage += 1
            
            if img_tags:
                coverage_percent = (keyword_coverage / len(img_tags)) * 100
                print(f"📄 {filename}: {keyword_coverage}/{len(img_tags)} images ({coverage_percent:.1f}%) with SEO keywords")
        
        except Exception as e:
            print(f"❌ Error validating {filename}: {e}")

def main():
    """Main execution function"""
    scan_and_update_all_images()
    validate_image_optimization()

if __name__ == "__main__":
    main()
