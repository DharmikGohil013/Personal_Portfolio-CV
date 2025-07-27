#!/usr/bin/env python3
"""
Add structured data JSON-LD to all HTML files
"""

import os
import glob
import re

portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

def add_structured_data(file_path):
    """Add structured data to HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(file_path)
        
        # Skip if already has structured data
        if 'application/ld+json' in content:
            return True
        
        # Determine appropriate structured data
        if filename == 'index.html':
            structured_data = '''{
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Dharmik Gohil",
    "url": "https://dharmikgohil.github.io/",
    "image": "https://dharmikgohil.github.io/assets/img/DharmikGohil%20(1).png",
    "sameAs": [
      "https://github.com/dharmikgohil"
    ],
    "jobTitle": "Game Developer",
    "worksFor": {
      "@type": "Organization",
      "name": "Freelance"
    },
    "alumniOf": {
      "@type": "EducationalOrganization",
      "name": "Government Engineering College"
    },
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Surat",
      "addressRegion": "Gujarat",
      "addressCountry": "India"
    },
    "description": "Professional game developer specializing in Unity development, mobile games, and interactive experiences."
  }'''
        elif filename in ['game1.html', 'game2.html', 'game3.html', 'game4.html', 'game5.html']:
            game_titles = {
                'game1.html': 'Floppy Bird',
                'game2.html': 'Cross Out',
                'game3.html': 'Memory Game',
                'game4.html': 'Puzzle Game',
                'game5.html': 'Action Game'
            }
            game_title = game_titles.get(filename, 'Unity Game')
            structured_data = f'''{{
    "@context": "https://schema.org",
    "@type": "VideoGame",
    "name": "{game_title}",
    "url": "https://dharmikgohil.github.io/{filename}",
    "description": "{game_title} is an innovative mobile game developed using Unity engine, featuring engaging gameplay and smooth controls.",
    "gamePlatform": ["Android", "Mobile"],
    "genre": "Casual Game",
    "author": {{
      "@type": "Person",
      "name": "Dharmik Gohil",
      "url": "https://dharmikgohil.github.io/"
    }},
    "datePublished": "2024",
    "inLanguage": "en"
  }}'''
        else:
            structured_data = '''{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "Dharmik Gohil Portfolio",
    "url": "https://dharmikgohil.github.io/''' + filename + '''",
    "description": "Professional portfolio page showcasing game development projects and technical expertise by Dharmik Gohil.",
    "author": {
      "@type": "Person",
      "name": "Dharmik Gohil"
    },
    "inLanguage": "en"
  }'''
        
        # Create the script tag
        script_tag = f'''
  <script type="application/ld+json">
  {structured_data}
  </script>'''
        
        # Add before closing head tag
        content = re.sub(r'(\s*</head>)', script_tag + r'\\n\\1', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        return False

def main():
    """Add structured data to all HTML files"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("📊 Adding Structured Data (JSON-LD)...")
    print("-" * 50)
    
    success_count = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html']:
            if add_structured_data(file_path):
                print(f"✅ Added structured data to {filename}")
                success_count += 1
    
    print(f"\\n📊 Structured data complete: {success_count} files processed")

if __name__ == "__main__":
    main()
