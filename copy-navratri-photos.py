"""
Script to copy Navratri photos to the portfolio assets folder
Run this script to copy your Navratri photos to the correct location
"""

import shutil
import os
from pathlib import Path

# Source directory (your Navratri photos)
SOURCE_DIR = r"d:\Images\Navratri 25\Day 3"

# Destination directory (portfolio assets)
DEST_DIR = r"d:\Git Hub\Web Applications\Portfolio\assets\img\memories\navratri-2025"

# List of photos to copy (selected best ones for gallery)
PHOTOS_TO_COPY = [
    "IMG_20250924_235005886_BURST015.jpg",
    "IMG_20250924_232834.jpg",
    "IMG_20250924_233933.jpg",
    "IMG_20250924_234007.jpg",
    "IMG_20250924_234546.jpg",
    "IMG_20250924_234548.jpg",
    "IMG_20250924_234556.jpg",
    "IMG_20250924_234557.jpg",
    "IMG_20250924_234600.jpg",
    "IMG_20250924_234641.jpg",
    "IMG_20250924_234644.jpg",
    "IMG_20250924_234646.jpg",
    "IMG_20250924_234710.jpg",
    "IMG_20250924_234720.jpg",
    "IMG_20250924_234722.jpg",
    "IMG_20250924_234724.jpg",
    "IMG_20250924_234808.jpg",
    "IMG_20250924_234810.jpg",
    "IMG_20250924_233933923_HDR_PORTRAIT.jpg",
    "IMG_20250924_233939398_HDR_PORTRAIT.jpg",
    "IMG_20250924_233955622_HDR_PORTRAIT.jpg",
    "IMG_20250924_233957232_HDR_PORTRAIT.jpg",
    "IMG_20250924_234012251_HDR_AE.jpg",
    "IMG_20250924_234017901_HDR_AE.jpg",
    "IMG_20250924_234305345_HDR.jpg",
    "IMG_20250924_234311396_HDR.jpg",
    "IMG_20250924_234425506_HDR.jpg",
    "IMG_20250924_234435715_HDR_PORTRAIT.jpg",
    "IMG_20250924_234437695_HDR_PORTRAIT.jpg",
    "IMG_20250924_234441555_HDR_PORTRAIT.jpg",
    "IMG_20250924_234447164_HDR.jpg",
    "IMG_20250924_234932485_HDR.jpg",
    "IMG_20250924_234950299_HDR_PORTRAIT.jpg",
    "IMG_20250924_235005886_BURST000_COVER.jpg",
    "IMG_20250924_235005886_BURST001.jpg",
    "IMG_20250924_235005886_BURST002.jpg",
    "IMG_20250924_235005886_BURST003.jpg",
    "IMG_20250924_235005886_BURST004.jpg",
    "IMG_20250924_235005886_BURST005.jpg",
    "IMG_20250924_235005886_BURST006.jpg",
    "IMG_20250924_235005886_BURST007.jpg",
    "IMG_20250924_235005886_BURST008.jpg",
    "IMG_20250924_235005886_BURST009.jpg",
    "IMG_20250924_235005886_BURST010.jpg",
    "IMG_20250924_235005886_BURST011.jpg",
    "IMG_20250924_235005886_BURST012.jpg",
    "IMG_20250924_235005886_BURST013.jpg",
    "IMG_20250924_235005886_BURST014.jpg"
]

def copy_photos():
    """Copy selected Navratri photos to portfolio assets"""
    
    # Create destination directory if it doesn't exist
    os.makedirs(DEST_DIR, exist_ok=True)
    
    copied_count = 0
    skipped_count = 0
    
    print("Starting to copy Navratri photos...")
    print(f"Source: {SOURCE_DIR}")
    print(f"Destination: {DEST_DIR}")
    print("-" * 60)
    
    for photo in PHOTOS_TO_COPY:
        source_path = os.path.join(SOURCE_DIR, photo)
        dest_path = os.path.join(DEST_DIR, photo)
        
        # Check if source file exists
        if not os.path.exists(source_path):
            print(f"⚠️  Not found: {photo}")
            skipped_count += 1
            continue
        
        # Copy the file
        try:
            shutil.copy2(source_path, dest_path)
            print(f"✅ Copied: {photo}")
            copied_count += 1
        except Exception as e:
            print(f"❌ Error copying {photo}: {str(e)}")
            skipped_count += 1
    
    print("-" * 60)
    print(f"\n📊 Summary:")
    print(f"   ✅ Successfully copied: {copied_count} photos")
    print(f"   ⚠️  Skipped: {skipped_count} photos")
    print(f"\n✨ Photos are now ready to use in your gallery!")
    print(f"📁 Location: {DEST_DIR}")

if __name__ == "__main__":
    try:
        copy_photos()
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("\nPlease check:")
        print("1. Source directory exists")
        print("2. You have permission to read/write files")
        print("3. Path separators are correct for your OS")
