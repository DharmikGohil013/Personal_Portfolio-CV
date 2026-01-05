#!/usr/bin/env python3
"""
Aggressive SEO Optimization for Dharmik Gohil Portfolio
Targeting keywords: dharmik, dharmikgohil, game developer, unity developer, XR developer, etc.
"""

import os
import glob
import re
from datetime import datetime

portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

# Aggressive keyword-rich meta configurations for each page
seo_configs = {
    'index.html': {
        'title': 'Dharmik Gohil | Professional Game Developer | Unity XR Developer | CHARUSAT University Graduate',
        'description': 'Dharmik Gohil - Expert Game Developer & Unity XR Developer from CHARUSAT University, DEPSTAR College. Specializing in Unity development, mobile games, VR/AR experiences, and backend development. Top game developer portfolio.',
        'keywords': 'Dharmik Gohil, dharmik, gohil dharmik, dharmikgohil, game developer, unity developer, unity XR developer, XR developer, gameplay engineer, backend developer, CHARUSAT University, DEPSTAR College, .fun game, mobile game developer, VR developer, AR developer, Surat game developer, Gujarat game developer, Unity expert',
        'h1': 'Dharmik Gohil - Professional Game Developer & Unity XR Expert',
        'focus_keywords': ['dharmik gohil', 'game developer', 'unity developer', 'XR developer', 'CHARUSAT University']
    },
    'about.html': {
        'title': 'About Dharmik Gohil | Unity Game Developer | CHARUSAT University | DEPSTAR College Graduate',
        'description': 'Meet Dharmik Gohil, professional game developer and Unity XR specialist from CHARUSAT University, DEPSTAR College. Expert in mobile game development, VR/AR experiences, and interactive gameplay engineering.',
        'keywords': 'About Dharmik Gohil, dharmik bio, gohil dharmik profile, Unity game developer, CHARUSAT University student, DEPSTAR College, game development skills, Unity XR expertise, mobile game developer profile, backend developer skills',
        'h1': 'About Dharmik Gohil | Game Developer Profile',
        'focus_keywords': ['dharmik gohil', 'CHARUSAT University', 'DEPSTAR College', 'game developer', 'Unity developer']
    },
    'portfolio.html': {
        'title': 'Dharmik Gohil Game Portfolio | Unity Projects | Mobile Games | XR Experiences',
        'description': 'Explore Dharmik Gohil\'s complete game development portfolio featuring Unity mobile games, VR/AR projects, .fun games, and interactive experiences. Professional game developer showcase.',
        'keywords': 'Dharmik Gohil portfolio, dharmik games, unity projects, mobile games, .fun game, VR games, AR projects, XR experiences, game developer portfolio, Unity game showcase, interactive games',
        'h1': 'Dharmik Gohil - Game Development Portfolio',
        'focus_keywords': ['dharmik gohil portfolio', '.fun game', 'unity projects', 'mobile games', 'game developer']
    },
    'resume.html': {
        'title': 'Dharmik Gohil Resume | Game Developer CV | Unity XR Developer | CHARUSAT Graduate',
        'description': 'Download Dharmik Gohil\'s professional resume. Experienced game developer and Unity XR specialist from CHARUSAT University with expertise in mobile games, VR/AR development, and backend engineering.',
        'keywords': 'Dharmik Gohil resume, dharmik CV, game developer resume, Unity developer CV, XR developer resume, CHARUSAT University graduate, DEPSTAR College, gameplay engineer resume, backend developer CV',
        'h1': 'Dharmik Gohil - Professional Resume',
        'focus_keywords': ['dharmik gohil resume', 'game developer resume', 'Unity developer', 'CHARUSAT University']
    },
    'contact.html': {
        'title': 'Contact Dharmik Gohil | Hire Game Developer | Unity XR Developer Services',
        'description': 'Contact Dharmik Gohil for professional game development services. Unity XR developer available for mobile games, VR/AR projects, and custom game development. Get in touch for game development consultation.',
        'keywords': 'Contact Dharmik Gohil, hire dharmik, game developer contact, Unity developer services, XR developer hire, mobile game development services, VR AR development, gameplay engineering services',
        'h1': 'Contact Dharmik Gohil - Game Developer',
        'focus_keywords': ['contact dharmik gohil', 'hire game developer', 'Unity developer services', 'game development']
    },
    'services.html': {
        'title': 'Dharmik Gohil Services | Game Development | Unity XR | Mobile Games | Backend Development',
        'description': 'Professional game development services by Dharmik Gohil. Unity XR development, mobile games, VR/AR experiences, backend development, and gameplay engineering. Expert developer services.',
        'keywords': 'Dharmik Gohil services, game development services, Unity XR development, mobile game development, VR AR development, backend development services, gameplay engineering, Unity developer services, XR developer services',
        'h1': 'Professional Game Development Services by Dharmik Gohil',
        'focus_keywords': ['dharmik gohil services', 'game development services', 'Unity XR development', 'developer services']
    },
    'Achivemtn.html': {
        'title': 'Dharmik Gohil Achievements | Game Developer Awards | Unity Projects | CHARUSAT Success',
        'description': 'Discover Dharmik Gohil\'s achievements in game development. Unity project successes, mobile game accomplishments, VR/AR milestones, and recognition from CHARUSAT University and industry.',
        'keywords': 'Dharmik Gohil achievements, dharmik awards, game developer accomplishments, Unity project success, CHARUSAT University achievements, DEPSTAR College recognition, mobile game awards, XR development milestones',
        'h1': 'Dharmik Gohil - Achievements & Recognition',
        'focus_keywords': ['dharmik gohil achievements', 'game developer awards', 'Unity projects', 'CHARUSAT University']
    },
    'vr.html': {
        'title': 'Dharmik Gohil VR/AR Projects | Unity XR Developer | Virtual Reality Games | Augmented Reality',
        'description': 'Explore Dharmik Gohil\'s VR/AR projects and XR experiences. Professional Unity XR developer creating immersive virtual reality games and augmented reality applications.',
        'keywords': 'Dharmik Gohil VR, dharmik AR projects, Unity XR developer, VR games, AR applications, virtual reality developer, augmented reality expert, XR experiences, immersive games, VR AR portfolio',
        'h1': 'Dharmik Gohil - VR/AR & XR Development',
        'focus_keywords': ['dharmik gohil VR', 'Unity XR developer', 'VR games', 'AR projects', 'XR developer']
    },
    'logo.html': {
        'title': 'Dharmik Gohil UI/UX Design | Game Interface Design | Logo Design Portfolio',
        'description': 'Dharmik Gohil\'s UI/UX design portfolio featuring game interface designs, logos, and visual elements. Professional game developer with design expertise.',
        'keywords': 'Dharmik Gohil design, dharmik UI UX, game interface design, logo design, visual design portfolio, game developer designer, Unity UI design',
        'h1': 'Dharmik Gohil - UI/UX Design Portfolio',
        'focus_keywords': ['dharmik gohil design', 'game interface design', 'UI UX design', 'logo design']
    },
    'game1.html': {
        'title': 'Floppy Bird Game by Dharmik Gohil | Unity Mobile Game | .fun Game Download',
        'description': 'Play Floppy Bird, an exciting mobile game developed by Dharmik Gohil using Unity engine. Download this addictive .fun game and experience professional game development.',
        'keywords': 'Floppy Bird game, Dharmik Gohil game, dharmik mobile game, Unity mobile game, .fun game, Android game download, casual mobile game, bird game Unity, game developer project',
        'h1': 'Floppy Bird - Mobile Game by Dharmik Gohil',
        'focus_keywords': ['floppy bird', 'dharmik gohil game', '.fun game', 'Unity mobile game', 'mobile game']
    },
    'game2.html': {
        'title': 'Cross Out Game by Dharmik Gohil | Unity Puzzle Game | Strategic Mobile Game',
        'description': 'Experience Cross Out, a strategic puzzle game by Dharmik Gohil. Built with Unity engine, this mobile game showcases advanced gameplay mechanics and engaging user experience.',
        'keywords': 'Cross Out game, Dharmik Gohil puzzle game, dharmik strategy game, Unity puzzle game, mobile strategy game, brain game, logic game Unity, game developer showcase',
        'h1': 'Cross Out - Strategic Puzzle Game by Dharmik Gohil',
        'focus_keywords': ['cross out game', 'dharmik gohil puzzle', 'Unity puzzle game', 'strategy game', 'mobile game']
    },
    'game3.html': {
        'title': 'Memory Game by Dharmik Gohil | Unity Brain Game | Cognitive Mobile Game',
        'description': 'Challenge your memory with this innovative memory game by Dharmik Gohil. Developed using Unity, featuring advanced cognitive gameplay and brain training mechanics.',
        'keywords': 'Memory game, Dharmik Gohil brain game, dharmik memory game, Unity memory game, cognitive game, brain training game, educational mobile game, memory challenge Unity',
        'h1': 'Memory Game - Brain Training by Dharmik Gohil',
        'focus_keywords': ['memory game', 'dharmik gohil brain game', 'Unity memory game', 'cognitive game', 'brain training']
    },
    'game4.html': {
        'title': 'Puzzle Adventure by Dharmik Gohil | Unity Adventure Game | Mobile Puzzle Game',
        'description': 'Embark on a puzzle adventure created by Dharmik Gohil. This Unity-powered mobile game combines adventure elements with challenging puzzle mechanics.',
        'keywords': 'Puzzle adventure game, Dharmik Gohil adventure, dharmik puzzle game, Unity adventure game, mobile puzzle adventure, adventure puzzle Unity, game developer portfolio',
        'h1': 'Puzzle Adventure - Unity Game by Dharmik Gohil',
        'focus_keywords': ['puzzle adventure', 'dharmik gohil adventure', 'Unity adventure game', 'mobile puzzle', 'adventure game']
    },
    'game5.html': {
        'title': 'Action Game by Dharmik Gohil | Unity Action Game | High-Speed Mobile Gaming',
        'description': 'Experience intense action gaming with Dharmik Gohil\'s latest Unity action game. Fast-paced mobile gaming with professional-grade gameplay mechanics and visual effects.',
        'keywords': 'Action game, Dharmik Gohil action game, dharmik fast game, Unity action game, mobile action game, fast-paced game, action mobile Unity, intense gaming experience',
        'h1': 'Action Game - High-Speed Gaming by Dharmik Gohil',
        'focus_keywords': ['action game', 'dharmik gohil action', 'Unity action game', 'mobile action', 'fast-paced game']
    }
}

def enhance_page_seo(file_path):
    """Apply aggressive SEO enhancements to a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(file_path)
        config = seo_configs.get(filename, {})
        
        if not config:
            return False
        
        # 1. Update title tag with aggressive keywords
        if 'title' in config:
            title_pattern = r'<title>[^<]*</title>'
            new_title = f'<title>{config["title"]}</title>'
            content = re.sub(title_pattern, new_title, content)
        
        # 2. Update meta description with keyword density
        if 'description' in config:
            desc_pattern = r'<meta name="description" content="[^"]*"[^>]*/?>'
            new_desc = f'<meta name="description" content="{config["description"]}">'
            content = re.sub(desc_pattern, new_desc, content)
        
        # 3. Update meta keywords for aggressive targeting
        if 'keywords' in config:
            keywords_pattern = r'<meta name="keywords" content="[^"]*"[^>]*/?>'
            new_keywords = f'<meta name="keywords" content="{config["keywords"]}">'
            if re.search(keywords_pattern, content):
                content = re.sub(keywords_pattern, new_keywords, content)
            else:
                # Add keywords after description
                desc_insertion = r'(<meta name="description"[^>]*>)'
                content = re.sub(desc_insertion, r'\\1\\n  ' + new_keywords, content)
        
        # 4. Add aggressive SEO meta tags
        additional_meta = f'''
  <!-- Advanced SEO Meta Tags -->
  <meta name="author" content="Dharmik Gohil">
  <meta name="creator" content="Dharmik Gohil">
  <meta name="publisher" content="Dharmik Gohil">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <meta name="googlebot" content="index, follow">
  <meta name="bingbot" content="index, follow">
  <meta name="revisit-after" content="1 days">
  <meta name="rating" content="general">
  <meta name="distribution" content="global">
  <meta name="language" content="en">
  <meta name="geo.region" content="IN-GJ">
  <meta name="geo.placename" content="Surat, Gujarat, India">
  <meta name="geo.position" content="21.1702;72.8311">
  <meta name="ICBM" content="21.1702, 72.8311">
  
  <!-- Educational Institution Tags -->
  <meta name="institution" content="CHARUSAT University">
  <meta name="college" content="DEPSTAR College">
  <meta name="university" content="Charotar University of Science and Technology">
  
  <!-- Professional Tags -->
  <meta name="profession" content="Game Developer">
  <meta name="specialization" content="Unity XR Developer">
  <meta name="expertise" content="Mobile Game Development, VR/AR, Backend Development">
  
  <!-- Canonical URL -->
  <link rel="canonical" href="https://dharmikgohil.art/{filename}">'''
        
        # Add after existing meta tags
        meta_insertion = r'(<meta name="keywords"[^>]*>)'
        if re.search(meta_insertion, content):
            content = re.sub(meta_insertion, r'\\1' + additional_meta, content)
        
        # 5. Add Open Graph and Twitter Cards for social SEO
        social_meta = f'''
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://dharmikgohil.art/{filename}">
  <meta property="og:title" content="{config.get('title', 'Dharmik Gohil - Game Developer')}">
  <meta property="og:description" content="{config.get('description', 'Professional Game Developer')}">
  <meta property="og:image" content="https://dharmikgohil.art/assets/img/DharmikGohil%20(1).png">
  <meta property="og:locale" content="en_US">
  <meta property="og:site_name" content="Dharmik Gohil Portfolio">
  
  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="https://dharmikgohil.art/{filename}">
  <meta property="twitter:title" content="{config.get('title', 'Dharmik Gohil - Game Developer')}">
  <meta property="twitter:description" content="{config.get('description', 'Professional Game Developer')}">
  <meta property="twitter:image" content="https://dharmikgohil.art/assets/img/DharmikGohil%20(1).png">
  <meta property="twitter:creator" content="@dharmikgohil">'''
        
        # Add social meta after canonical link
        canonical_insertion = r'(<link rel="canonical"[^>]*>)'
        content = re.sub(canonical_insertion, r'\\1' + social_meta, content)
        
        # 6. Add JSON-LD structured data for rich snippets
        if filename == 'index.html':
            structured_data = '''
  
  <!-- JSON-LD Structured Data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Dharmik Gohil",
    "url": "https://dharmikgohil.art/",
    "image": "https://dharmikgohil.art/assets/img/DharmikGohil%20(1).png",
    "sameAs": [
      "https://github.com/dharmikgohil013",
      "https://linkedin.com/in/dharmikgohil"
    ],
    "jobTitle": "Professional Game Developer",
    "description": "Expert Game Developer and Unity XR Developer from CHARUSAT University specializing in mobile games, VR/AR experiences, and backend development",
    "worksFor": {
      "@type": "Organization",
      "name": "Freelance Game Developer"
    },
    "alumniOf": [
      {
        "@type": "EducationalOrganization",
        "name": "CHARUSAT University",
        "alternateName": "Charotar University of Science and Technology",
        "department": "DEPSTAR College"
      }
    ],
    "knowsAbout": [
      "Game Development",
      "Unity Engine",
      "XR Development",
      "Mobile Game Development",
      "VR/AR Development",
      "Backend Development",
      "Gameplay Engineering"
    ],
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Surat",
      "addressRegion": "Gujarat",
      "addressCountry": "India"
    },
    "expertise": "Unity XR Developer, Mobile Game Developer, VR/AR Specialist"
  }
  </script>'''
        else:
            structured_data = f'''
  
  <!-- JSON-LD Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "{config.get('title', 'Dharmik Gohil Page')}",
    "url": "https://dharmikgohil.art/{filename}",
    "description": "{config.get('description', 'Dharmik Gohil professional page')}",
    "author": {{
      "@type": "Person",
      "name": "Dharmik Gohil",
      "jobTitle": "Professional Game Developer",
      "alumniOf": "CHARUSAT University"
    }},
    "publisher": {{
      "@type": "Person",
      "name": "Dharmik Gohil"
    }},
    "inLanguage": "en",
    "isPartOf": {{
      "@type": "WebSite",
      "name": "Dharmik Gohil Portfolio",
      "url": "https://dharmikgohil.art/"
    }}
  }}
  </script>'''
        
        # Add structured data before closing head tag
        head_close_pattern = r'(</head>)'
        content = re.sub(head_close_pattern, structured_data + '\\n\\1', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"Error enhancing {filename}: {e}")
        return False

def optimize_images_alt_tags(file_path):
    """Add aggressive keyword-rich alt tags to images"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(file_path)
        
        # Define keyword-rich alt text mappings
        alt_mappings = {
            'dlogo.png': 'Dharmik Gohil Logo - Professional Game Developer and Unity XR Expert',
            'DharmikGohil (1).png': 'Dharmik Gohil Professional Profile - Game Developer from CHARUSAT University',
            'DharmikGohil (1).webp': 'Dharmik Gohil Portfolio Photo - Unity XR Developer and Mobile Game Specialist',
            'profile-img.jpg': 'Dharmik Gohil Professional Headshot - Expert Game Developer and Unity Specialist',
            'hero-bg.jpg': 'Game Development Background - Dharmik Gohil Professional Gaming Environment',
            'game1 (1).png': 'Floppy Bird Mobile Game by Dharmik Gohil - Unity Game Development Showcase',
            'game1 (2).png': 'Floppy Bird Gameplay Screenshot - Mobile Gaming by Dharmik Gohil',
            'game1 (3).png': 'Floppy Bird Game Interface - Unity Mobile Game Development',
            'game1 (4).png': 'Floppy Bird High Score - Gaming Achievement by Dharmik Gohil',
            'game1 (5).png': 'Floppy Bird Game Menu - Professional UI Design by Dharmik Gohil',
            'game1 (6).png': 'Floppy Bird Game Features - Advanced Mobile Game Development',
            '2 (1).png': 'Cross Out Strategy Game by Dharmik Gohil - Unity Puzzle Game Development',
            '2 (2).png': 'Cross Out Game Interface - Strategic Mobile Gaming by Dharmik Gohil',
            '2 (3).png': 'Cross Out Puzzle Mechanics - Advanced Game Development by Dharmik Gohil',
            'Unity.webp': 'Unity Game Engine Expertise - Dharmik Gohil Professional Development Platform',
            'man-wearing-vr-goggles-gaming.jpg': 'VR Gaming Experience - Dharmik Gohil XR Development Expertise'
        }
        
        # Pattern to find all img tags
        img_pattern = r'<img([^>]+)>'
        
        def enhance_img_alt(match):
            img_attrs = match.group(1)
            
            # Extract src attribute
            src_match = re.search(r'src="([^"]*)"', img_attrs)
            if not src_match:
                return match.group(0)
            
            src = src_match.group(1)
            img_filename = os.path.basename(src)
            
            # Get keyword-rich alt text
            if img_filename in alt_mappings:
                new_alt = alt_mappings[img_filename]
            else:
                # Generate SEO-optimized alt text
                base_name = os.path.splitext(img_filename)[0]
                new_alt = f"{base_name.replace('-', ' ').replace('_', ' ').title()} - Dharmik Gohil Game Developer Portfolio"
            
            # Update or add alt attribute
            alt_pattern = r'alt="[^"]*"'
            if re.search(alt_pattern, img_attrs):
                img_attrs = re.sub(alt_pattern, f'alt="{new_alt}"', img_attrs)
            else:
                img_attrs += f' alt="{new_alt}"'
            
            return f'<img{img_attrs}>'
        
        content = re.sub(img_pattern, enhance_img_alt, content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"Error optimizing images in {os.path.basename(file_path)}: {e}")
        return False

def main():
    """Execute aggressive SEO optimization"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("🚀 AGGRESSIVE SEO OPTIMIZATION STARTING...")
    print("=" * 70)
    print("Target Keywords: dharmik, dharmikgohil, gohil dharmik, game developer,")
    print("unity developer, XR developer, CHARUSAT University, DEPSTAR College")
    print("=" * 70)
    
    enhanced_count = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename in seo_configs:
            print(f"\\n🎯 Optimizing {filename}...")
            
            # Apply SEO enhancements
            if enhance_page_seo(file_path):
                print(f"  ✅ Meta tags and structured data added")
            
            # Optimize image alt tags
            if optimize_images_alt_tags(file_path):
                print(f"  ✅ Image alt tags optimized")
            
            enhanced_count += 1
            print(f"  🚀 {filename} fully optimized for search rankings!")
    
    print(f"\\n🏆 AGGRESSIVE SEO COMPLETE!")
    print(f"📊 {enhanced_count} pages optimized for maximum search visibility")
    print(f"🎯 Targeting {len(seo_configs)} strategic keyword groups")
    print(f"🌟 Portfolio ready to dominate search results!")

if __name__ == "__main__":
    main()
