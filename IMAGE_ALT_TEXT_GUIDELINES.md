# Image Alt Text & SEO Guidelines — dharmikgohil.art

## Alt Text Formula

```
[Subject] — [Context/Action] [Location/Event] [Keyword]
```

### Examples

| Image | Alt Text |
|-------|----------|
| Profile headshot | `Dharmik Gohil — freelance Unity game developer in Surat, Gujarat, India` |
| Casual photo | `Dharmik Gohil casual photo — young game developer from Gujarat, India` |
| Mavericks Battlegrounds screenshot | `Mavericks Battlegrounds gameplay — 10-player multiplayer game built with Unity and Photon PUN` |
| Hackron team photo | `Dharmik Gohil with Team Bug Busters at Hackron 2025, DY Patil University Pune` |
| IIT Bombay Techfest | `Dharmik Gohil — IIT Bombay Techfest 2025 winner, game development competition` |
| CHARUSAT Expo demo | `Mavericks Battlegrounds demo at CHARUSAT Expo 3.0 — live multiplayer game showcase` |
| Certificate image | `NPTEL DSA with Java certification — Dharmik Gohil, CHARUSAT University` |
| Game thumbnail (2D) | `[Game Name] — Unity 2D mobile game by Dharmik Gohil` |
| Game thumbnail (3D) | `[Game Name] — Unity 3D game with [feature] by Dharmik Gohil` |
| AR/VR project | `AR/VR experience — [Project Name] built with Unity AR Foundation by Dharmik Gohil` |
| Web project screenshot | `[Project Name] — full-stack web application (React, Node.js) by Dharmik Gohil` |

## Rules

1. **Every `<img>` must have an `alt` attribute** — never leave it empty unless purely decorative
2. **Include 1-2 keywords naturally** — "Unity game developer", "multiplayer", "Surat Gujarat"
3. **Keep under 125 characters** — screen readers truncate beyond this
4. **Describe the image, don't keyword-stuff** — Google penalises unnatural alt text
5. **Use `title` attribute** for additional hover context on important images
6. **Decorative images** (borders, bullets, backgrounds) get `alt=""`
7. **Icons** don't need alt text if accompanied by visible label text
8. **Always add `width` and `height`** attributes to prevent CLS

## File Naming Convention

```
dharmik-gohil-[context]-[year].[webp|jpg]
```

Examples:
- `dharmik-gohil-professional-headshot-2026.webp`
- `mavericks-battlegrounds-gameplay-screenshot.webp`
- `hackron-2025-team-bug-busters.webp`
- `unity-ar-vr-project-demo.webp`

## Internal Linking from Images

Where possible, wrap project images in `<a>` tags linking to the relevant page:

```html
<a href="portfolio.html" title="View Dharmik Gohil's game development portfolio">
  <img src="assets/img/project.webp" 
       alt="Mavericks Battlegrounds — Unity multiplayer game" 
       width="600" height="400" loading="lazy">
</a>
```
