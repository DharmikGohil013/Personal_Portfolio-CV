#!/usr/bin/env python3
"""
Final SEO Enhancement - Complete Missing Elements
"""

import os
import glob
import re

portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

def fix_missing_seo_elements(file_path):
    """Fix missing canonical URLs and meta keywords"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(file_path)
        
        # Add canonical URL if missing
        if 'rel="canonical"' not in content:
            canonical_tag = f'\\n  <link rel="canonical" href="https://dharmikgohil.art/{filename}">'
            # Add after author meta tag
            author_pattern = r'(<meta name="author"[^>]*>)'
            if re.search(author_pattern, content):
                content = re.sub(author_pattern, r'\\1' + canonical_tag, content)
        
        # Add meta keywords if missing
        if 'name="keywords"' not in content:
            # Get keyword configuration based on filename
            keyword_configs = {
                'index.html': 'Dharmik Gohil, dharmik, gohil dharmik, dharmikgohil, game developer, unity developer, unity XR developer, XR developer, gameplay engineer, backend developer, CHARUSAT University, DEPSTAR College, .fun game, mobile game developer, VR developer, AR developer, Surat game developer, Gujarat game developer, Unity expert',
                'about.html': 'About Dharmik Gohil, dharmik bio, gohil dharmik profile, Unity game developer, CHARUSAT University student, DEPSTAR College, game development skills, Unity XR expertise, mobile game developer profile, backend developer skills',
                'portfolio.html': 'Dharmik Gohil portfolio, dharmik games, unity projects, mobile games, .fun game, VR games, AR projects, XR experiences, game developer portfolio, Unity game showcase, interactive games',
                'resume.html': 'Dharmik Gohil resume, dharmik CV, game developer resume, Unity developer CV, XR developer resume, CHARUSAT University graduate, DEPSTAR College, gameplay engineer resume, backend developer CV',
                'contact.html': 'Contact Dharmik Gohil, hire dharmik, game developer contact, Unity developer services, XR developer hire, mobile game development services, VR AR development, gameplay engineering services',
                'services.html': 'Dharmik Gohil services, game development services, Unity XR development, mobile game development, VR AR development, backend development services, gameplay engineering, Unity developer services, XR developer services',
                'Achivemtn.html': 'Dharmik Gohil achievements, dharmik awards, game developer accomplishments, Unity project success, CHARUSAT University achievements, DEPSTAR College recognition, mobile game awards, XR development milestones',
                'vr.html': 'Dharmik Gohil VR, dharmik AR projects, Unity XR developer, VR games, AR applications, virtual reality developer, augmented reality expert, XR experiences, immersive games, VR AR portfolio',
                'logo.html': 'Dharmik Gohil design, dharmik UI UX, game interface design, logo design, visual design portfolio, game developer designer, Unity UI design',
                'game1.html': 'Floppy Bird game, Dharmik Gohil game, dharmik mobile game, Unity mobile game, .fun game, Android game download, casual mobile game, bird game Unity, game developer project',
                'game2.html': 'Cross Out game, Dharmik Gohil puzzle game, dharmik strategy game, Unity puzzle game, mobile strategy game, brain game, logic game Unity, game developer showcase',
                'game3.html': 'Memory game, Dharmik Gohil brain game, dharmik memory game, Unity memory game, cognitive game, brain training game, educational mobile game, memory challenge Unity',
                'game4.html': 'Puzzle adventure game, Dharmik Gohil adventure, dharmik puzzle game, Unity adventure game, mobile puzzle adventure, adventure puzzle Unity, game developer portfolio',
                'game5.html': 'Action game, Dharmik Gohil action game, dharmik fast game, Unity action game, mobile action game, fast-paced game, action mobile Unity, intense gaming experience'
            }
            
            keywords = keyword_configs.get(filename, 'Dharmik Gohil, game developer, Unity developer')
            keywords_tag = f'\\n  <meta name="keywords" content="{keywords}">'
            
            # Add after description meta tag
            desc_pattern = r'(<meta name="description"[^>]*>)'
            if re.search(desc_pattern, content):
                content = re.sub(desc_pattern, r'\\1' + keywords_tag, content)
        
        # Add JSON-LD structured data if missing
        if 'application/ld+json' not in content:
            if filename == 'index.html':
                structured_data = '''
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Dharmik Gohil",
    "url": "https://dharmikgohil.art/",
    "image": "https://dharmikgohil.art/assets/img/DharmikGohil%20(1).png",
    "sameAs": [
      "https://github.com/dharmikgohil013"
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
                page_titles = {
                    'about.html': 'About Dharmik Gohil - Game Developer Profile',
                    'portfolio.html': 'Dharmik Gohil - Game Development Portfolio',
                    'resume.html': 'Dharmik Gohil - Professional Resume',
                    'contact.html': 'Contact Dharmik Gohil - Game Developer',
                    'services.html': 'Professional Game Development Services by Dharmik Gohil',
                    'Achivemtn.html': 'Dharmik Gohil - Achievements & Recognition',
                    'vr.html': 'Dharmik Gohil - VR/AR & XR Development',
                    'logo.html': 'Dharmik Gohil - UI/UX Design Portfolio'
                }
                
                if filename.startswith('game'):
                    game_titles = {
                        'game1.html': 'Floppy Bird - Mobile Game by Dharmik Gohil',
                        'game2.html': 'Cross Out - Strategic Puzzle Game by Dharmik Gohil',
                        'game3.html': 'Memory Game - Brain Training by Dharmik Gohil',
                        'game4.html': 'Puzzle Adventure - Unity Game by Dharmik Gohil',
                        'game5.html': 'Action Game - High-Speed Gaming by Dharmik Gohil'
                    }
                    page_title = game_titles.get(filename, 'Game by Dharmik Gohil')
                    
                    structured_data = f'''
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "VideoGame",
    "name": "{page_title}",
    "url": "https://dharmikgohil.art/{filename}",
    "description": "Professional mobile game developed by Dharmik Gohil using Unity engine",
    "gamePlatform": ["Android", "Mobile"],
    "genre": "Mobile Game",
    "author": {{
      "@type": "Person",
      "name": "Dharmik Gohil",
      "jobTitle": "Game Developer",
      "url": "https://dharmikgohil.art/"
    }},
    "datePublished": "2024",
    "inLanguage": "en"
  }}
  </script>'''
                else:
                    page_title = page_titles.get(filename, 'Dharmik Gohil Professional Page')
                    structured_data = f'''
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "{page_title}",
    "url": "https://dharmikgohil.art/{filename}",
    "description": "Professional page by Dharmik Gohil, expert game developer from CHARUSAT University",
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
    "inLanguage": "en"
  }}
  </script>'''
            
            # Add before closing head tag
            head_close_pattern = r'(</head>)'
            content = re.sub(head_close_pattern, structured_data + '\\n\\1', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"Error fixing {filename}: {e}")
        return False

def main():
    """Fix missing SEO elements across all pages"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("🔧 FIXING MISSING SEO ELEMENTS...")
    print("-" * 50)
    
    fixed_count = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html']:
            if fix_missing_seo_elements(file_path):
                print(f"✅ Fixed missing elements in {filename}")
                fixed_count += 1
    
    print(f"\\n🏆 COMPLETE! Fixed {fixed_count} pages")
    print("🚀 All pages now have maximum SEO optimization!")

if __name__ == "__main__":
    main()
