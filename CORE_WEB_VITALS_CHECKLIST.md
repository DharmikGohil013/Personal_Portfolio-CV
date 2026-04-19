# Core Web Vitals Checklist — dharmikgohil.art

## Current State Assessment

### Already Implemented ✅
- [x] `<meta content="width=device-width, initial-scale=1.0" name="viewport">` on all pages
- [x] `preconnect` to Google Fonts, Analytics, CDNs
- [x] `dns-prefetch` for external resources
- [x] `loading="lazy"` on below-fold images
- [x] `loading="eager"` on hero/above-fold images
- [x] Width/height attributes on key images (prevents CLS)
- [x] Minified CSS via vendor libraries
- [x] Async Google Analytics (`async` attribute on gtag)
- [x] Async Google AdSense
- [x] `theme-color` meta tag
- [x] Image sitemap (image-sitemap.xml)

---

## Action Items for 100% Core Web Vitals

### Largest Contentful Paint (LCP) — Target: < 2.5s
- [ ] **Preload hero image**: Add `<link rel="preload" as="image" href="assets/img/dharmik-profile-photo-2026.jpg">` in `<head>` of index.html
- [ ] **Convert images to WebP**: Convert all `.jpg`/`.png` to `.webp` format (50-80% smaller)
- [ ] **Use `<picture>` element**: Serve WebP with JPEG fallback for hero images
- [ ] **Optimise hero image size**: Resize to 400x400 max for the profile photo (currently may be oversized)
- [ ] **Compress all images**: Use TinyPNG or Squoosh to compress to <100KB each
- [ ] **Add `fetchpriority="high"`** to hero image for priority rendering

### First Input Delay (FID) / Interaction to Next Paint (INP) — Target: < 200ms
- [ ] **Defer non-critical JS**: Add `defer` to all `<script>` tags except gtag
- [ ] **Defer AOS.js**: Load after DOMContentLoaded
- [ ] **Minimise inline JS**: Move large inline scripts to external files
- [ ] **Reduce DOM size**: index.html has 5700+ lines — consider splitting CSS to external files

### Cumulative Layout Shift (CLS) — Target: < 0.1
- [ ] **Set width/height on ALL images**: Audit every `<img>` tag and add dimensions
- [ ] **Reserve space for fonts**: Use `font-display: swap` on all @font-face declarations
- [ ] **Fix AdSense CLS**: Wrap AdSense container in a fixed-height div
- [ ] **Avoid inserting content above fold dynamically**: Ensure no JS modifies above-fold layout

---

## Quick Performance Wins

### CSS Optimisation
- [ ] Extract inline `<style>` blocks (5700+ lines) into external CSS files
- [ ] Remove unused CSS with PurgeCSS
- [ ] Critical CSS: Inline only above-fold styles, defer rest

### JavaScript Optimisation
- [ ] Bundle and minify custom JS
- [ ] Remove console.log statements
- [ ] Use `IntersectionObserver` for scroll animations instead of scroll listeners

### Server/Hosting (GitHub Pages)
- [ ] Verify Cloudflare CDN or similar is active
- [ ] Enable browser caching headers
- [ ] Verify Brotli/Gzip compression is enabled
- [ ] Minimise redirects (ensure CNAME is clean)

---

## Testing Tools
1. **Google PageSpeed Insights**: https://pagespeed.web.dev
2. **Google Lighthouse**: Chrome DevTools → Lighthouse tab
3. **Web Vitals Chrome Extension**: Real-time CWV monitoring
4. **GTmetrix**: https://gtmetrix.com
5. **Google Search Console**: Core Web Vitals report (requires verification)
