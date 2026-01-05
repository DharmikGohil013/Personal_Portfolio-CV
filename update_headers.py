#!/usr/bin/env python3
"""
Script to standardize the header across all HTML files
"""

import os
import glob
import re

# Define the directory containing the HTML files
portfolio_dir = r"d:\Git Hub\Web Applications\Portfolio"

# The standardized header HTML from index.html
standard_header = '''  <header id="header" class="header d-flex align-items-center sticky-top">
    <div class="container-fluid position-relative d-flex align-items-center justify-content-between">
      <a href="index.html" class="logo d-flex align-items-center me-auto me-xl-0">
        <img src="assets/img/dlogo.png" alt="">
        <h1 class="sitename">DHARMIK</h1>
      </a>
      <nav id="navmenu" class="navmenu">
        <ul>
          <li><a href="https://dharmikgohil.art" class="active">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#resume">Resume</a></li>
          <li><a href="services.html">Abilities</a></li>
          <li class="dropdown"><a href="https://dharmikgohil.art/portfolio.html"><span>Projects</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
            <ul>
              <li><a href="portfolio.html">Games</a></li>
              </li>
              <li class="dropdown"><a href="#"><span>Flutter App</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
                <ul>
                  <li><a href="assets/Fit Sync.apk">Fit Sync</a></li>
                </ul>
              </li>
              <li class="dropdown"><a href="logo.html"><span>Ui/ux</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
                <ul>
                  <li><a href="logo.html">Designs</a></li>
                </ul>
              </li>
              <li class="dropdown"><a href="#"><span>Websites</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
                <ul>
                  <li><a href="http://gdgs.dharmikgohil.art/">GDGS Games</a></li>
                  <!-- <li><a href="https://dharmikgohil013.github.io/DHARMIK-GOHIL-FILMS/">Film industry</a></li> -->
                  <li><a href="http://flipcart.dharmikgohil.art/">Flipkart Clone</a></li>
                  <li><a href="http://krishna.dharmikgohil.art/">Krishna Construction</a></li>
                  <!-- <li><a href="#">MedCare</a></li> -->
                </ul>
              
              <li class="dropdown"><a href="#"><span>Java</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
                <ul>
                  <li class="dropdown"><a href="#"><span>CampusAdminPro</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
                    <ul>
                       
                      <li><a href="https://drive.google.com/file/d/15YNf77gERCt2LYfRYSdXiYU3yAkx7EvC/view?usp=drive_link">Report</a></li>
                    </ul>
                  </li>
                    
                </ul>
              </li>
              <li class="dropdown"><a href="#"><span>Node Js</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
                <ul>
                  <li><a href="https://indianturijam.dharmikgohil.art/">IndianTurijam</a></li>
                  <li><a href="contact.html">Contact Page</a></li>
                </ul>
              </li>
              <li class="dropdown"><a href="#"><span>C & C++</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
                <ul>
                  <li><a href="https://github.com/DharmikGohil013/Hostel_Menegment_System_iDGAWS-">Hostel Management</a></li>
                  <li><a href="https://github.com/DharmikGohil013/Bank_Mangemnt_System">Bank Management</a></li>
                </ul>
              </li>
            </ul>
          </li>
          <li><a href="Achivemtn.html">Milestones</a></li>
          <li><a href="#contact">Contact</a></li>
          <li class="dropdown"><a href="#"><span>Time to Fun</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
            <ul>
              <li><a href="https://dharmik086.itch.io/floppy-bird-860" target="_blank">Floppy Bird</a></li>
              <li><a href="https://dharmik086.itch.io/minimario" target="_blank">MiniMario</a></li>
              <li><a href="https://dharmikgohil.itch.io/mavericks-battlegrounds" target="_blank">MAVERICKS BATTLEGROUNDS</a></li> 
            </ul>
          </li>
          <li class="dropdown">
  <a href="#"><span style="color: #15ff00;">Services</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
  <ul>
    <li><a href="https://actify.dharmikgohil.art/" target="_blank">Actify</a></li> <!-- ✅ NEW ENTRY -->
    <li><a href="https://fkm.vercel.app/" target="_blank">Wifi Service</a></li>
    <li><a href="assets/Fit Sync.apk" target="_blank">Fit Sync</a></li>
    <li><a href="https://learnlink.dharmikgohil.art" target="_blank">Learn Link</a></li>
    
  </ul>
</li>

        </ul>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </nav>
      <div class="header-social-links">
        <a href="https://github.com/DharmikGohil013" target="_blank"><i class="bi bi-github"></i></a>
        <a href="https://www.linkedin.com/in/dharmikgohil086/" target="_blank"><i class="bi bi-linkedin"></i></a>
        <a href="https://www.instagram.com/dharmik.086/?next=%2F" target="_blank"><i class="bi bi-instagram"></i></a>
        <a href="https://x.com/Dharmik086" target="_blank"><i class="bi bi-twitter"></i></a>
        <a href="https://play.google.com/store/apps/details?id=com.dharmikgohilfun.crossout" target="_blank"><i class="bi bi-google-play"></i></a>
        <a href="assets/img/GOHIL DHARMIKBHAI GHANSHYAMBHAI Resume.pdf" class="download-resume" download><i class="bi bi-download"></i></a>
      </div>
    </div>
  </header>'''

def update_header_in_file(file_path):
    """Update the header in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match the entire header section
        header_pattern = r'<header[^>]*id="header"[^>]*>.*?</header>'
        
        # Check if header exists
        if re.search(header_pattern, content, re.DOTALL | re.IGNORECASE):
            # Replace the existing header with the standard one
            content = re.sub(header_pattern, standard_header, content, flags=re.DOTALL | re.IGNORECASE)
            
            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Updated header in {os.path.basename(file_path)}")
            return True
        else:
            print(f"⚠ No header found in {os.path.basename(file_path)}")
            return False
        
    except Exception as e:
        print(f"✗ Error updating {os.path.basename(file_path)}: {e}")
        return False

def main():
    """Main function to update headers in all HTML files"""
    # Get all HTML files in the directory
    html_files = glob.glob(os.path.join(portfolio_dir, "*.html"))
    
    updated_count = 0
    skipped_count = 0
    
    print("Standardizing headers across all HTML files...")
    print("-" * 50)
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        
        # Skip certain files that might not need headers
        if filename in ['loader-test.html', 'premium-loader-template.html']:
            print(f"⚬ Skipped {filename} (test/template file)")
            skipped_count += 1
            continue
        
        if update_header_in_file(file_path):
            updated_count += 1
        else:
            skipped_count += 1
    
    print("-" * 50)
    print(f"Summary: {updated_count} files updated, {skipped_count} files skipped")
    print("Header standardization complete!")

if __name__ == "__main__":
    main()
