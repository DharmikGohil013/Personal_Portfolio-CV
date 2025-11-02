# 📸 TechFest'24 Blog - Image Upload Guide

## 🎯 Overview
This guide will help you add your TechFest'24 images to the newly created blog post.

## 📁 Image Organization

### Step 1: Create Image Folder
Create this folder structure in your workspace:
```
d:\Git Hub\Web Applications\Portfolio\assets\img\blog\techfest\
```

### Step 2: Copy Images from Event Folder
Copy images from:
```
d:\Events\IIT Bombay\TechFest 24\TechFest'24\TechFest'24 Images
```

To:
```
d:\Git Hub\Web Applications\Portfolio\assets\img\blog\techfest\
```

## 🗂️ Image Categories & Naming Convention

### 1. **Main TechFest Image** (Header)
- **Location in blog**: Top banner image
- **Suggested name**: `techfest-main.jpg`
- **Use**: Main entrance/banner/crowd shot of TechFest

### 2. **Game Development Workshop Images** (3-6 images)
- **Suggested names**: 
  - `workshop-1.jpg` (Workshop session)
  - `workshop-2.jpg` (Participants learning)
  - `workshop-3.jpg` (Hands-on coding)
  - `workshop-4.jpg` (Instructor teaching)
  - `workshop-5.jpg` (Team collaboration)
  - `workshop-6.jpg` (Workshop certificate/completion)

### 3. **Robotics Exhibition Images** (3-6 images)
- **Suggested names**:
  - `robot-1.jpg` (Autonomous robot)
  - `robot-2.jpg` (Humanoid robot)
  - `robot-3.jpg` (Industrial robot)
  - `robot-4.jpg` (Robot demonstration)
  - `robot-5.jpg` (Robot close-up)
  - `robot-6.jpg` (Robotic arm/mechanism)

### 4. **Robot Dogs Images** (3-5 images)
- **Suggested names**:
  - `robotdog-1.jpg` (Robot dog walking)
  - `robotdog-2.jpg` (Robot dog demonstration)
  - `robotdog-3.jpg` (Robot dog close-up)
  - `robotdog-4.jpg` (Robot dog obstacle course)
  - `robotdog-5.jpg` (Robot dog sensors/tech)

### 5. **Drone Technology Images** (3-6 images)
- **Suggested names**:
  - `drone-1.jpg` (Drone in flight)
  - `drone-2.jpg` (Racing drone)
  - `drone-3.jpg` (Drone swarm)
  - `drone-4.jpg` (Delivery drone)
  - `drone-5.jpg` (Drone exhibition booth)
  - `drone-6.jpg` (Drone close-up/tech)

### 6. **Defense/Weapons Technology Images** (3-4 images)
- **Suggested names**:
  - `defense-1.jpg` (Defense systems)
  - `defense-2.jpg` (Weapons display)
  - `defense-3.jpg` (Security technology)
  - `defense-4.jpg` (Tactical equipment)

### 7. **General TechFest Event Images** (4-8 images)
- **Suggested names**:
  - `event-1.jpg` (Crowd/atmosphere)
  - `event-2.jpg` (Exhibition halls)
  - `event-3.jpg` (Interactive demos)
  - `event-4.jpg` (Night events/cultural)
  - `event-5.jpg` (Food/recreation area)
  - `event-6.jpg` (Startup showcase)
  - `event-7.jpg` (Competitions)
  - `event-8.jpg` (You with friends/attendees)

## 🔧 How to Update the Blog File

Open: `d:\Git Hub\Web Applications\Portfolio\blog\iit-bombay-techfest-2024-experience.html`

### Replace Placeholder Images:

#### 1. Main Header Image (Line ~236)
**Find:**
```html
<img src="../assets/img/blog/techfest-main.jpg" alt="IIT Bombay TechFest 2024 Main Entrance" class="img-fluid">
```

**Ensure the image exists at:**
```
assets/img/blog/techfest-main.jpg
```

#### 2. Workshop Images (Around line ~320)
**Find this section:**
```html
<!-- ADD WORKSHOP IMAGES HERE -->
<div class="gallery-item">
  <img src="../assets/img/blog/techfest/workshop-placeholder.jpg" alt="Game Development Workshop">
```

**Replace with your actual images:**
```html
<div class="gallery-item">
  <img src="../assets/img/blog/techfest/workshop-1.jpg" alt="Game Development Workshop Session">
  <div class="gallery-caption">
    <p>Workshop Session - Learning Unity Game Development</p>
  </div>
</div>
<div class="gallery-item">
  <img src="../assets/img/blog/techfest/workshop-2.jpg" alt="Hands-on Coding Session">
  <div class="gallery-caption">
    <p>Hands-on Game Development Practice</p>
  </div>
</div>
<!-- Add more workshop images as needed -->
```

#### 3. Robotics Images (Around line ~380)
**Find:**
```html
<!-- ADD ROBOTICS IMAGES HERE -->
```

**Replace with:**
```html
<div class="gallery-item">
  <img src="../assets/img/blog/techfest/robot-1.jpg" alt="Advanced Robotics Display">
  <div class="gallery-caption">
    <p>Advanced Robotics Technology</p>
  </div>
</div>
<div class="gallery-item">
  <img src="../assets/img/blog/techfest/robot-2.jpg" alt="Humanoid Robot">
  <div class="gallery-caption">
    <p>Humanoid Robot Demonstration</p>
  </div>
</div>
<!-- Add more robot images -->
```

#### 4. Robot Dogs Images
**Find:**
```html
<!-- ADD ROBOT DOG IMAGES HERE -->
```

**Replace with your robot dog images following the same pattern**

#### 5. Drone Images
**Find:**
```html
<!-- ADD DRONE IMAGES HERE -->
```

**Replace with your drone images**

#### 6. Defense Technology Images
**Find:**
```html
<!-- ADD WEAPONS/DEFENSE IMAGES HERE -->
```

**Replace with your defense tech images**

#### 7. General Event Images
**Find:**
```html
<!-- ADD GENERAL TECHFEST IMAGES HERE -->
```

**Replace with general event images**

## 📝 Image Gallery Template

Use this template for each image:

```html
<div class="gallery-item">
  <img src="../assets/img/blog/techfest/YOUR-IMAGE-NAME.jpg" alt="Descriptive Alt Text">
  <div class="gallery-caption">
    <p>Short description of what's in the image</p>
  </div>
</div>
```

## ✅ Checklist

- [ ] Create `assets/img/blog/techfest/` folder
- [ ] Copy all TechFest images to the folder
- [ ] Rename images according to categories
- [ ] Add main header image
- [ ] Add workshop images (3-6)
- [ ] Add robotics images (3-6)
- [ ] Add robot dog images (3-5)
- [ ] Add drone images (3-6)
- [ ] Add defense tech images (3-4)
- [ ] Add general event images (4-8)
- [ ] Update image captions with relevant descriptions
- [ ] Test the blog page in browser
- [ ] Optimize image sizes (recommended: max 1920px width, 80% JPEG quality)

## 🎨 Image Optimization Tips

1. **Resize large images** to max 1920px width
2. **Compress images** to reduce file size (use tools like TinyPNG)
3. **Recommended format**: JPEG for photos, PNG for logos/graphics
4. **Target file size**: Under 500KB per image for faster loading

## 🔗 Blog Post Location

**Live Blog URL (after publishing):**
```
https://dharmikgohil.fun/blog/iit-bombay-techfest-2024-experience.html
```

**Blog Listed On:**
```
https://dharmikgohil.fun/blog.html
```

## 🎯 Blog Features

Your TechFest blog includes:
- ✨ Futuristic design with cyan/green color scheme
- 📱 Fully responsive layout
- 🖼️ Beautiful image galleries with hover effects
- 📊 Event statistics showcase
- 🎨 Section-wise image organization
- 💬 Social media integration
- 🔖 Tags and metadata for SEO
- 🎭 Smooth animations and transitions

## 🚀 Next Steps

1. Copy images to the folder
2. Update the HTML file with actual image paths
3. Add descriptive captions
4. Test in browser
5. Share your amazing TechFest experience! 🎉

---

**Need Help?** If you need assistance with image optimization or HTML editing, feel free to ask!

**Pro Tip:** Take screenshots of specific moments if you have more detailed images to add!
