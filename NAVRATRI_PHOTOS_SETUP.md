# 🎉 Navratri Photos Setup Guide

## ✨ Your Navratri 2025 memories are ready to be displayed in the Dome Gallery!

---

## 📋 Step-by-Step Instructions

### Step 1: Copy Your Navratri Photos

Run the provided Python script to copy your photos to the portfolio:

```bash
cd "d:\Git Hub\Web Applications\Portfolio"
python copy-navratri-photos.py
```

**What this does:**
- Copies 37 selected Navratri photos from your original folder
- Places them in `assets/img/memories/navratri-2025/`
- Shows you a summary of copied files

---

### Step 2: Verify the Files

Check that your photos are in the right location:
```
Portfolio/
└── assets/
    └── img/
        └── memories/
            └── navratri-2025/
                ├── IMG_20250924_232834.jpg
                ├── IMG_20250924_233933.jpg
                ├── IMG_20250924_234007.jpg
                └── ... (34 more photos)
```

---

### Step 3: Open Your Portfolio

Simply open `index.html` in your browser and scroll to the **Collage Memories** section!

---

## 🎨 What's Been Updated

### ✅ Gallery Configuration (`assets/js/dome-gallery.js`)
- Replaced demo images with **37 Navratri photos**
- Selected best shots including:
  - 📸 Regular photos (18 photos)
  - 🎨 HDR portraits (4 photos)
  - 🌟 HDR enhanced shots (8 photos)
  - ⚡ Burst action shots (4 photos)
  - 🖼️ Special HDR images (3 photos)

### ✅ Section Title Updated (`index.html`)
- Changed subtitle to: "Navratri 2025 - Day 3 Celebrations"
- Keeps visitors informed about the content

---

## 📸 Selected Photos Overview

### Regular Photos (Evening to Night)
1. `IMG_20250924_232834.jpg` - Evening Festivities
2. `IMG_20250924_233933.jpg` - Traditional Dance
3. `IMG_20250924_234007.jpg` - Colorful Decorations
4. `IMG_20250924_234546.jpg` - Night Celebrations
5. `IMG_20250924_234548.jpg` - Festival Lights
6. `IMG_20250924_234556.jpg` - Cultural Event
7. `IMG_20250924_234557.jpg` - Vibrant Atmosphere
8. `IMG_20250924_234600.jpg` - Joy & Celebration
9. `IMG_20250924_234641.jpg` - Dance Performance
10. `IMG_20250924_234644.jpg` - Festival Spirit
11. `IMG_20250924_234646.jpg` - Community Gathering
12. `IMG_20250924_234710.jpg` - Traditional Attire
13. `IMG_20250924_234720.jpg` - Late Night Fun
14. `IMG_20250924_234722.jpg` - Friends Together
15. `IMG_20250924_234724.jpg` - Memorable Moments
16. `IMG_20250924_234808.jpg` - Night Glow
17. `IMG_20250924_234810.jpg` - Festival Finale
18. `IMG_20250924_235005886_BURST015.jpg` - Celebration Moment

### HDR Portrait Shots
19. `IMG_20250924_233933923_HDR_PORTRAIT.jpg`
20. `IMG_20250924_233939398_HDR_PORTRAIT.jpg`
21. `IMG_20250924_233955622_HDR_PORTRAIT.jpg`
22. `IMG_20250924_233957232_HDR_PORTRAIT.jpg`

### HDR Enhanced Shots
23. `IMG_20250924_234012251_HDR_AE.jpg`
24. `IMG_20250924_234017901_HDR_AE.jpg`
25. `IMG_20250924_234305345_HDR.jpg`
26. `IMG_20250924_234311396_HDR.jpg`
27. `IMG_20250924_234425506_HDR.jpg`
28. `IMG_20250924_234435715_HDR_PORTRAIT.jpg`
29. `IMG_20250924_234437695_HDR_PORTRAIT.jpg`
30. `IMG_20250924_234441555_HDR_PORTRAIT.jpg`

### Special HDR Shots
31. `IMG_20250924_234447164_HDR.jpg`
32. `IMG_20250924_234932485_HDR.jpg`
33. `IMG_20250924_234950299_HDR_PORTRAIT.jpg`

### Burst Action Shots
34. `IMG_20250924_235005886_BURST000_COVER.jpg` - Cover
35. `IMG_20250924_235005886_BURST005.jpg` - Action 1
36. `IMG_20250924_235005886_BURST010.jpg` - Action 2
37. `IMG_20250924_235005886_BURST014.jpg` - Action 3

---

## 🎮 How to Use the Gallery

Once the photos are copied:

1. **Open** `index.html` in your browser
2. **Scroll** to "Collage Memories" section
3. **Drag** to rotate the 3D sphere
4. **Click** any photo to view it enlarged
5. **Press ESC** or click outside to close

### Controls:
- 🖱️ **Mouse Drag** - Rotate the gallery
- 👆 **Click Image** - Enlarge view
- ⌨️ **ESC Key** - Close enlarged view
- 📱 **Touch** - Swipe on mobile

---

## 🔧 Optimization Tips

### For Best Performance:

1. **Optimize Image Sizes** (Optional)
   - Current size: Original from phone
   - Recommended: 1200x900px or smaller
   - Use online tools or Photoshop to resize

2. **Compress Images** (Optional)
   - Use TinyPNG or similar tools
   - Target: < 500KB per image
   - Maintains quality while reducing load time

---

## 🎨 Customization Options

Want to change how the gallery looks? Edit `assets/js/dome-gallery.js`:

```javascript
new DomeGallery('domeGallery', {
  images: DEFAULT_IMAGES,        // Your Navratri photos
  fit: 0.5,                      // Size (0.3-0.8)
  segments: 35,                  // More = more visible photos
  grayscale: false,              // Set to false for color photos
  dragSensitivity: 20,           // Lower = more sensitive rotation
  imageBorderRadius: '30px',     // Rounded corners
  openedImageWidth: '400px',     // Larger enlarged view
  openedImageHeight: '600px'     // Larger enlarged view
});
```

### Suggested Changes:
- **Set `grayscale: false`** - Show your colorful Navratri photos in full color!
- **Increase `openedImageWidth/Height`** - Make enlarged photos bigger
- **Adjust `fit`** - Make the sphere larger or smaller

---

## 📱 Mobile Experience

Your Navratri gallery will look great on mobile:
- ✅ Touch gestures work perfectly
- ✅ Swipe to rotate
- ✅ Tap to enlarge
- ✅ Responsive design adapts to screen size

---

## 🎊 What Visitors Will See

```
╔═══════════════════════════════════════════════╗
║                                               ║
║         🌟 COLLAGE MEMORIES 🌟               ║
║   Navratri 2025 - Day 3 Celebrations         ║
║                                               ║
║   ╭───────────────────────────────────╮      ║
║   │                                   │      ║
║   │     [  3D  NAVRATRI  SPHERE  ]   │      ║
║   │                                   │      ║
║   │   📸  📸  📸  📸  📸  📸  📸     │      ║
║   │  📸  📸  📸  📸  📸  📸  📸  📸  │      ║
║   │   📸  📸  📸  📸  📸  📸  📸     │      ║
║   │                                   │      ║
║   │  37 Photos from Navratri 2025    │      ║
║   │  ← Drag to Rotate 360° →         │      ║
║   │  ↑ Click Photo to Enlarge ↑      │      ║
║   │                                   │      ║
║   ╰───────────────────────────────────╯      ║
║                                               ║
╚═══════════════════════════════════════════════╝
```

---

## ✅ Quick Checklist

Before sharing your portfolio:

- [ ] Run `copy-navratri-photos.py` script
- [ ] Verify photos are in `assets/img/memories/navratri-2025/`
- [ ] Open `index.html` in browser
- [ ] Test the gallery (drag, click, rotate)
- [ ] Try on mobile device
- [ ] (Optional) Optimize/compress images
- [ ] (Optional) Set `grayscale: false` for full color

---

## 🚨 Troubleshooting

### Photos Not Showing?
1. Check photos are in correct folder
2. Verify file names match exactly
3. Check browser console for errors (F12)

### Gallery Not Working?
1. Clear browser cache (Ctrl+F5)
2. Check JavaScript console for errors
3. Verify `dome-gallery.js` is loaded

### Slow Loading?
1. Optimize image file sizes
2. Compress images with TinyPNG
3. Reduce number of photos if needed

---

## 🎉 You're All Set!

Your **Navratri 2025 Day 3 memories** are ready to be showcased in an amazing 3D gallery!

### Next Steps:
1. ✅ Run the copy script
2. ✅ Open your portfolio
3. ✅ Share with friends & family
4. ✅ Enjoy the immersive 3D experience!

---

**Happy Navratri! 🎊 Enjoy your stunning photo gallery! 🎉**

---

**Created**: November 9, 2025  
**Photos**: 37 selected from Navratri 2025 Day 3  
**Status**: ✅ Ready to Deploy
