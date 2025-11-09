import os
import shutil
from pathlib import Path

# Source files with their paths
source_files = [
    r"d:\Events\Darshan University\Code Arena 1.0\WhatsApp Image 2025-07-19 at 19.17.06_28cfa1b2.jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (40).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (6).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (7).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (8).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (9).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (10).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (11).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (12).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (13).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (14).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (15).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (16).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (17).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (18).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (19).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (20).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (21).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (22).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (23).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (24).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (25).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (26).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (27).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (28).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (29).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (30).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (31).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (32).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (33).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (34).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (35).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (36).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (37).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (38).jpg",
    r"d:\Events\Hackron Hackathon 25\Images\Hckron Hackathone (39).jpg",
    r"d:\Events\IIT Bombay\TechFest 24\TechFest'24\TechFest'24 Images\TechFest'24(DHARMIKGOHIL) (20).jpg",
    r"d:\Events\IIT Bombay\TechFest 24\TechFest'24\TechFest'24 Images\TechFest'24(DHARMIKGOHIL) (15).jpg",
    r"d:\Events\IIT Bombay\TechFest 24\TechFest'24\TechFest'24 Images\TechFest'24(DHARMIKGOHIL) (17).jpg",
    r"d:\Events\Odoo\Odoo CHARUSAT 25\Odoo x CHARUSAT (7).jpg",
    r"d:\Events\Odoo\Odoo CHARUSAT 25\Odoo x CHARUSAT (3).JPG",
]

# Destination directory
dest_dir = Path(r"d:\Git Hub\Web Applications\Portfolio\assets\img\memories\events")

# Create destination directory if it doesn't exist
dest_dir.mkdir(parents=True, exist_ok=True)

print("Starting to copy event photos...")
print(f"Destination: {dest_dir}")
print("-" * 60)

copied_count = 0
skipped_count = 0
file_mapping = []

for i, source_path in enumerate(source_files, 1):
    source = Path(source_path)
    
    if not source.exists():
        print(f"⚠️  Skipped (not found): {source.name}")
        skipped_count += 1
        continue
    
    # Create a clean filename
    if "Code Arena" in str(source):
        new_name = f"event-code-arena-01.jpg"
    elif "Hackathone" in source.name:
        num = source.stem.split('(')[-1].split(')')[0]
        new_name = f"event-hackron-{num.zfill(2)}.jpg"
    elif "TechFest" in source.name:
        num = source.stem.split('(')[-1].split(')')[0]
        new_name = f"event-techfest-{num.zfill(2)}.jpg"
    elif "Odoo" in source.name:
        num = source.stem.split('(')[-1].split(')')[0]
        new_name = f"event-odoo-{num.zfill(2)}.{source.suffix[1:]}"
    else:
        new_name = source.name
    
    dest_path = dest_dir / new_name
    
    try:
        shutil.copy2(source, dest_path)
        print(f"✅ Copied: {new_name}")
        file_mapping.append(new_name)
        copied_count += 1
    except Exception as e:
        print(f"❌ Error copying {source.name}: {e}")
        skipped_count += 1

print("-" * 60)
print(f"\n📊 Summary:")
print(f"   ✅ Successfully copied: {copied_count} photos")
print(f"   ⚠️  Skipped: {skipped_count} photos")
print(f"   📁 Location: {dest_dir}")
print("\n✨ Photos are now ready to use in your gallery!")
print(f"\n📝 Total files for gallery: {len(file_mapping)}")
