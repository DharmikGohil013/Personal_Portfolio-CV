#!/usr/bin/env python3
"""
Comprehensive SEO Optimization Script for Dharmik Gohil Portfolio
Implements on-page SEO best practices across all HTML files
"""

import os
import glob
import re
from datetime import datetime

# Define the directory containing the HTML files
portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

# SEO configurations for each page
seo_config = {
    'index.html': {
        'title': 'Dharmik Gohil - Professional Game Developer | Unity & Web Development Portfolio',
        'description': 'Explore Dharmik Gohil\'s portfolio featuring innovative game development, Unity projects, web applications, and interactive experiences. Based in Surat, Gujarat, specializing in mobile and PC game development.',
        'keywords': 'Dharmik Gohil, game developer, Unity developer, web developer, mobile games, PC games, portfolio, Surat, Gujarat, India, game design, interactive experiences',
        'h1': 'Dharmik Gohil - Game Developer & Interactive Experience Designer',
        'canonical': 'https://dharmikgohil.art/',
        'og_type': 'website'
    },
    'about.html': {
        'title': 'About Dharmik Gohil - Game Developer, Designer & Innovator | Portfolio',
        'description': 'Learn about Dharmik Gohil, an 18-year-old passionate game developer from Surat, Gujarat. Discover his journey, skills, education, and commitment to creating immersive gaming experiences.',
        'keywords': 'Dharmik Gohil about, game developer biography, Unity developer background, web developer profile, Surat game developer, student developer',
        'h1': 'About Dharmik Gohil',
        'canonical': 'https://dharmikgohil.art/about.html',
        'og_type': 'profile'
    },
    'contact.html': {
        'title': 'Contact Dharmik Gohil - Game Developer | Get in Touch for Projects',
        'description': 'Contact Dharmik Gohil for game development projects, collaborations, and inquiries. Based in Surat, Gujarat. Available for freelance work and exciting opportunities.',
        'keywords': 'contact Dharmik Gohil, game developer contact, hire game developer, Unity developer contact, web developer Surat, freelance game developer',
        'h1': 'Contact Dharmik Gohil',
        'canonical': 'https://dharmikgohil.art/contact.html',
        'og_type': 'website'
    },
    'resume.html': {
        'title': 'Dharmik Gohil Resume - Game Developer Skills, Experience & Education',
        'description': 'View Dharmik Gohil\'s professional resume showcasing game development skills, programming languages, projects, education, and technical expertise in Unity, C#, JavaScript, and more.',
        'keywords': 'Dharmik Gohil resume, game developer CV, Unity developer resume, programming skills, technical skills, education, projects, portfolio resume',
        'h1': 'Dharmik Gohil - Professional Resume',
        'canonical': 'https://dharmikgohil.art/resume.html',
        'og_type': 'profile'
    },
    'portfolio.html': {
        'title': 'Game Portfolio - Dharmik Gohil\'s Unity Games & Interactive Projects',
        'description': 'Explore Dharmik Gohil\'s game development portfolio featuring Unity games, mobile apps, web applications, and interactive experiences. See live demos and project details.',
        'keywords': 'Dharmik Gohil portfolio, Unity games, mobile games, web games, game portfolio, interactive projects, game development showcase',
        'h1': 'Game Development Portfolio',
        'canonical': 'https://dharmikgohil.art/portfolio.html',
        'og_type': 'website'
    },
    'services.html': {
        'title': 'Game Development Services - Dharmik Gohil | Unity, Web & Mobile Development',
        'description': 'Professional game development services by Dharmik Gohil. Specializing in Unity game development, web applications, mobile apps, UI/UX design, and interactive experiences.',
        'keywords': 'game development services, Unity development services, web development services, mobile app development, UI UX design, freelance game developer services',
        'h1': 'Professional Development Services',
        'canonical': 'https://dharmikgohil.art/services.html',
        'og_type': 'service'
    },
    'Achivemtn.html': {
        'title': 'Achievements & Milestones - Dharmik Gohil Game Developer Success Stories',
        'description': 'Discover Dharmik Gohil\'s achievements, milestones, certifications, and recognition in game development, programming competitions, and educational accomplishments.',
        'keywords': 'Dharmik Gohil achievements, game developer milestones, programming achievements, certifications, awards, recognition, success stories',
        'h1': 'Achievements & Milestones',
        'canonical': 'https://dharmikgohil.art/Achivemtn.html',
        'og_type': 'website'
    },
    'game1.html': {
        'title': 'Floppy Bird Game - Unity Mobile Game by Dharmik Gohil',
        'description': 'Play Floppy Bird, an addictive mobile game developed by Dharmik Gohil using Unity. Features challenging gameplay, smooth controls, and engaging mechanics.',
        'keywords': 'Floppy Bird game, Unity mobile game, casual game, mobile gaming, Unity game development, Dharmik Gohil games',
        'h1': 'Floppy Bird - Mobile Unity Game',
        'canonical': 'https://dharmikgohil.art/game1.html',
        'og_type': 'website'
    },
    'game2.html': {
        'title': 'Cross Out Game - Strategic Unity Game by Dharmik Gohil',
        'description': 'Experience Cross Out, a strategic puzzle game developed with Unity by Dharmik Gohil. Features innovative gameplay mechanics and challenging levels.',
        'keywords': 'Cross Out game, Unity puzzle game, strategy game, puzzle mechanics, Unity game development, Dharmik Gohil games',
        'h1': 'Cross Out - Strategic Puzzle Game',
        'canonical': 'https://dharmikgohil.art/game2.html',
        'og_type': 'website'
    },
    'game3.html': {
        'title': 'Mini Mario Game - Platform Adventure by Dharmik Gohil',
        'description': 'Play Mini Mario, a classic platformer game developed by Dharmik Gohil. Features traditional Mario-style gameplay with modern Unity engine.',
        'keywords': 'Mini Mario game, platform game, Unity platformer, classic gameplay, Mario clone, Unity game development',
        'h1': 'Mini Mario - Platform Adventure Game',
        'canonical': 'https://dharmikgohil.art/game3.html',
        'og_type': 'website'
    },
    'game4.html': {
        'title': 'Mavericks Battlegrounds - Multiplayer Unity Game by Dharmik Gohil',
        'description': 'Experience Mavericks Battlegrounds, an exciting multiplayer game developed by Dharmik Gohil. Features real-time multiplayer gameplay and competitive mechanics.',
        'keywords': 'Mavericks Battlegrounds, multiplayer game, Unity multiplayer, online gaming, competitive game, Dharmik Gohil games',
        'h1': 'Mavericks Battlegrounds - Multiplayer Game',
        'canonical': 'https://dharmikgohil.art/game4.html',
        'og_type': 'website'
    },
    'game5.html': {
        'title': 'Hotel Management Game - Business Simulation by Dharmik Gohil',
        'description': 'Manage your virtual hotel in this business simulation game developed by Dharmik Gohil. Features resource management, customer service, and strategic gameplay.',
        'keywords': 'Hotel Management game, business simulation, management game, Unity simulation, strategy game, Dharmik Gohil games',
        'h1': 'Hotel Management - Business Simulation Game',
        'canonical': 'https://dharmikgohil.art/game5.html',
        'og_type': 'website'
    },
    'vr.html': {
        'title': 'AR/VR Projects - Immersive Technology by Dharmik Gohil',
        'description': 'Explore Dharmik Gohil\'s AR/VR projects showcasing cutting-edge immersive technology, virtual reality experiences, and augmented reality applications.',
        'keywords': 'AR VR projects, virtual reality, augmented reality, immersive technology, VR development, AR development, Unity VR, Unity AR',
        'h1': 'AR/VR Projects & Immersive Experiences',
        'canonical': 'https://dharmikgohil.art/vr.html',
        'og_type': 'website'
    },
    'logo.html': {
        'title': 'UI/UX Design Portfolio - Creative Designs by Dharmik Gohil',
        'description': 'Explore Dharmik Gohil\'s UI/UX design portfolio featuring creative logos, user interface designs, and visual identity projects for games and applications.',
        'keywords': 'UI UX design, logo design, graphic design, user interface, user experience, visual design, creative portfolio, Dharmik Gohil design',
        'h1': 'UI/UX Design Portfolio',
        'canonical': 'https://dharmikgohil.art/logo.html',
        'og_type': 'website'
    }
}

def add_structured_data(filename):
    """Generate JSON-LD structured data for each page"""
    if filename == 'index.html':
        return '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Dharmik Gohil",
  "jobTitle": "Game Developer",
  "description": "Professional game developer specializing in Unity, web development, and interactive experiences",
  "url": "https://dharmikgohil.art",
  "image": "https://dharmikgohil.art/assets/img/DharmikGohil (1).png",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Surat",
    "addressRegion": "Gujarat",
    "addressCountry": "India"
  },
  "email": "dharmikgohil395003@gmail.com",
  "telephone": "+919624105887",
  "birthDate": "2006-06-12",
  "knowsAbout": ["Game Development", "Unity", "Web Development", "Mobile Development", "UI/UX Design"],
  "alumniOf": {
    "@type": "EducationalOrganization",
    "name": "Bachelor of Technology in Information Technology"
  },
  "sameAs": [
    "https://github.com/DharmikGohil013",
    "https://www.linkedin.com/in/dharmikgohil086/",
    "https://www.instagram.com/dharmik.086/",
    "https://x.com/Dharmik086"
  ]
}
</script>'''
    elif 'game' in filename:
        game_name = seo_config.get(filename, {}).get('h1', 'Game Project')
        return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "VideoGame",
  "name": "{game_name}",
  "author": {{
    "@type": "Person",
    "name": "Dharmik Gohil"
  }},
  "publisher": {{
    "@type": "Person",
    "name": "Dharmik Gohil"
  }},
  "description": "{seo_config.get(filename, {}).get('description', '')}",
  "url": "https://dharmikgohil.art/{filename}",
  "gamePlatform": ["Unity", "Mobile", "Web"],
  "genre": "Casual Game"
}}
</script>'''
    else:
        return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "{seo_config.get(filename, {}).get('title', '')}",
  "description": "{seo_config.get(filename, {}).get('description', '')}",
  "url": "https://dharmikgohil.art/{filename}",
  "author": {{
    "@type": "Person",
    "name": "Dharmik Gohil"
  }},
  "dateModified": "{datetime.now().isoformat()}"
}}
</script>'''

def optimize_seo_for_file(file_path):
    """Optimize SEO for a single HTML file"""
    filename = os.path.basename(file_path)
    
    # Skip template and test files
    if filename in ['loader-test.html', 'premium-loader-template.html']:
        return False
    
    if filename not in seo_config:
        print(f"⚠ No SEO config found for {filename}, skipping...")
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        config = seo_config[filename]
        
        # 1. Update title tag
        title_pattern = r'<title>.*?</title>'
        new_title = f'<title>{config["title"]}</title>'
        content = re.sub(title_pattern, new_title, content, flags=re.IGNORECASE)
        
        # 2. Update or add meta description
        desc_pattern = r'<meta name="description" content="[^"]*"[^>]*>'
        new_desc = f'<meta name="description" content="{config["description"]}">'
        if re.search(desc_pattern, content, re.IGNORECASE):
            content = re.sub(desc_pattern, new_desc, content, flags=re.IGNORECASE)
        else:
            # Add after viewport meta tag
            viewport_pattern = r'(<meta.*?viewport.*?>)'
            content = re.sub(viewport_pattern, r'\\1\\n  ' + new_desc, content, flags=re.IGNORECASE)
        
        # 3. Update or add meta keywords
        keywords_pattern = r'<meta name="keywords" content="[^"]*"[^>]*>'
        new_keywords = f'<meta name="keywords" content="{config["keywords"]}">'
        if re.search(keywords_pattern, content, re.IGNORECASE):
            content = re.sub(keywords_pattern, new_keywords, content, flags=re.IGNORECASE)
        else:
            # Add after description
            desc_insert_pattern = r'(<meta name="description"[^>]*>)'
            content = re.sub(desc_insert_pattern, r'\\1\\n  ' + new_keywords, content, flags=re.IGNORECASE)
        
        # 4. Add Open Graph and Twitter meta tags
        og_tags = f'''
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="{config["og_type"]}">
  <meta property="og:url" content="{config["canonical"]}">
  <meta property="og:title" content="{config["title"]}">
  <meta property="og:description" content="{config["description"]}">
  <meta property="og:image" content="https://dharmikgohil.art/assets/img/DharmikGohil (1).png">

  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="{config["canonical"]}">
  <meta property="twitter:title" content="{config["title"]}">
  <meta property="twitter:description" content="{config["description"]}">
  <meta property="twitter:image" content="https://dharmikgohil.art/assets/img/DharmikGohil (1).png">

  <!-- Additional SEO Meta Tags -->
  <meta name="robots" content="index, follow">
  <meta name="author" content="Dharmik Gohil">
  <meta name="creator" content="Dharmik Gohil">
  <meta name="publisher" content="Dharmik Gohil">
  <link rel="canonical" href="{config["canonical"]}">'''
        
        # Add OG tags before closing head tag
        if '<meta property="og:' not in content:
            head_close_pattern = r'(</head>)'
            content = re.sub(head_close_pattern, og_tags + r'\\n\\1', content, flags=re.IGNORECASE)
        
        # 5. Add lang attribute to html tag
        html_pattern = r'<html([^>]*)>'
        if 'lang=' not in content:
            content = re.sub(html_pattern, r'<html\\1 lang="en">', content, flags=re.IGNORECASE)
        
        # 6. Add structured data
        structured_data = add_structured_data(filename)
        if 'application/ld+json' not in content:
            head_close_pattern = r'(</head>)'
            content = re.sub(head_close_pattern, f'\\n  {structured_data}\\n\\1', content, flags=re.IGNORECASE)
        
        # 7. Optimize images with alt tags (basic check)
        # Find images without alt attributes and add generic ones
        img_pattern = r'<img([^>]*src="[^"]*")([^>]*?)>'
        def add_alt_tag(match):
            img_attrs = match.group(1) + match.group(2)
            if 'alt=' not in img_attrs:
                # Extract filename for alt text
                src_match = re.search(r'src="([^"]*)"', img_attrs)
                if src_match:
                    src = src_match.group(1)
                    alt_text = os.path.splitext(os.path.basename(src))[0].replace('-', ' ').replace('_', ' ').title()
                    return f'<img{img_attrs} alt="{alt_text}">'
            return match.group(0)
        
        content = re.sub(img_pattern, add_alt_tag, content)
        
        # Write the updated content back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ SEO optimized: {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Error optimizing {filename}: {e}")
        return False

def main():
    """Main function to optimize SEO for all HTML files"""
    print("🚀 Starting Comprehensive SEO Optimization...")
    print("=" * 60)
    
    # Get all HTML files
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    optimized_count = 0
    total_count = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        
        # Skip template files
        if filename in ['loader-test.html', 'premium-loader-template.html']:
            continue
        
        total_count += 1
        if optimize_seo_for_file(file_path):
            optimized_count += 1
    
    print("=" * 60)
    print(f"📊 SEO Optimization Summary:")
    print(f"   Files processed: {optimized_count}/{total_count}")
    print(f"   Success rate: {(optimized_count/total_count*100):.1f}%")
    
    if optimized_count == total_count:
        print("🎉 All files successfully optimized for SEO!")
    else:
        print(f"⚠ {total_count - optimized_count} files need manual attention")

if __name__ == "__main__":
    main()
