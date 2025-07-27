#!/usr/bin/env python3
"""
Add missing Twitter Cards and Structured Data to all HTML files
"""

import os
import glob
import re

portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

# Twitter Card templates for different page types
twitter_cards = {
    'index': '''  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="https://dharmikgohil.github.io/">
  <meta property="twitter:title" content="Dharmik Gohil - Professional Game Developer | Unity & Web Development Portfolio">
  <meta property="twitter:description" content="Explore Dharmik Gohil's portfolio featuring innovative game development, Unity projects, web applications, and interactive experiences. Based in Surat, Gujarat, specializing in mobile and PC game development.">
  <meta property="twitter:image" content="https://dharmikgohil.github.io/assets/img/DharmikGohil%20(1).png">''',
    
    'about': '''  <!-- Twitter -->
  <meta property="twitter:card" content="summary">
  <meta property="twitter:url" content="https://dharmikgohil.github.io/about.html">
  <meta property="twitter:title" content="About Dharmik Gohil - Game Developer & Tech Enthusiast">
  <meta property="twitter:description" content="Learn about Dharmik Gohil's journey in game development, technical skills, and passion for creating innovative gaming experiences using Unity, C#, and modern web technologies.">
  <meta property="twitter:image" content="https://dharmikgohil.github.io/assets/img/DharmikGohil%20(1).png">''',
    
    'portfolio': '''  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="https://dharmikgohil.github.io/portfolio.html">
  <meta property="twitter:title" content="Game Development Portfolio - Dharmik Gohil's Projects">
  <meta property="twitter:description" content="Discover Dharmik Gohil's comprehensive portfolio of game development projects, including Unity games, web applications, and innovative interactive experiences.">
  <meta property="twitter:image" content="https://dharmikgohil.github.io/assets/img/game1%20(1).png">''',
    
    'game': '''  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="https://dharmikgohil.github.io/{filename}">
  <meta property="twitter:title" content="{game_title} - Unity Game by Dharmik Gohil">
  <meta property="twitter:description" content="Experience {game_title}, an innovative mobile game developed by Dharmik Gohil using Unity engine. Featuring engaging gameplay, smooth controls, and immersive gaming experience.">
  <meta property="twitter:image" content="https://dharmikgohil.github.io/assets/img/game1%20(1).png">'''
}

# Structured data templates
structured_data = {
    'person': '''{
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Dharmik Gohil",
    "url": "https://dharmikgohil.github.io/",
    "image": "https://dharmikgohil.github.io/assets/img/DharmikGohil%20(1).png",
    "sameAs": [
      "https://github.com/dharmikgohil",
      "https://linkedin.com/in/dharmikgohil"
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
  }''',
    
    'website': '''{
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Dharmik Gohil Portfolio",
    "url": "https://dharmikgohil.github.io/",
    "description": "Professional portfolio showcasing game development projects, Unity games, and web applications by Dharmik Gohil.",
    "author": {
      "@type": "Person",
      "name": "Dharmik Gohil"
    }
  }''',
    
    'game': '''{
    "@context": "https://schema.org",
    "@type": "VideoGame",
    "name": "{game_title}",
    "url": "https://dharmikgohil.github.io/{filename}",
    "description": "{game_title} is an innovative mobile game developed using Unity engine, featuring engaging gameplay and smooth controls.",
    "gamePlatform": ["Android", "Mobile"],
    "genre": "Casual Game",
    "author": {
      "@type": "Person",
      "name": "Dharmik Gohil",
      "url": "https://dharmikgohil.github.io/"
    },
    "datePublished": "2024",
    "inLanguage": "en"
  }'''
}

def add_twitter_and_structured_data(file_path):
    """Add Twitter cards and structured data to HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(file_path)
        base_name = os.path.splitext(filename)[0]
        
        # Skip if already has Twitter cards
        if 'twitter:card' in content:
            return True
        
        # Determine page type and get appropriate templates
        if filename == 'index.html':
            twitter_template = twitter_cards['index']
            structured_template = structured_data['person']
        elif filename == 'about.html':
            twitter_template = twitter_cards['about']
            structured_template = structured_data['person']
        elif filename == 'portfolio.html':
            twitter_template = twitter_cards['portfolio']
            structured_template = structured_data['website']
        elif filename.startswith('game'):
            game_titles = {
                'game1.html': 'Floppy Bird',
                'game2.html': 'Cross Out',
                'game3.html': 'Memory Game',
                'game4.html': 'Puzzle Game',
                'game5.html': 'Action Game'
            }
            game_title = game_titles.get(filename, 'Unity Game')
            twitter_template = twitter_cards['game'].format(filename=filename, game_title=game_title)
            structured_template = structured_data['game'].format(filename=filename, game_title=game_title)
        else:
            # Default templates for other pages
            twitter_template = twitter_cards['about'].replace('about.html', filename).replace('About Dharmik Gohil', f'{base_name.title()} - Dharmik Gohil')
            structured_template = structured_data['website']
        
        # Find insertion point for Twitter cards (after Open Graph tags)
        og_pattern = r'(<meta property="og:image"[^>]*>)'
        twitter_insertion = twitter_template + '\\n'
        
        if re.search(og_pattern, content):
            content = re.sub(og_pattern, r'\\1\\n' + twitter_insertion, content)
        else:
            # Fallback: add after head tag
            content = re.sub(r'(<head[^>]*>)', r'\\1\\n' + twitter_insertion, content)
        
        # Add structured data before closing head tag
        structured_script = f'''\\n  <script type="application/ld+json">
  {structured_template}
  </script>'''
        
        content = re.sub(r'(</head>)', structured_script + '\\n\\1', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        return False

def main():
    """Add Twitter cards and structured data to all HTML files"""
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    print("🐦 Adding Twitter Cards and Structured Data...")
    print("-" * 60)
    
    success_count = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename not in ['loader-test.html', 'premium-loader-template.html']:
            if add_twitter_and_structured_data(file_path):
                print(f"✅ Enhanced {filename}")
                success_count += 1
    
    print(f"\\n📊 Enhancement complete: {success_count} files processed")
    print("🔍 Running verification...")

if __name__ == "__main__":
    main()
