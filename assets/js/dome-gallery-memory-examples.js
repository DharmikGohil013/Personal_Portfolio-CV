/**
 * EXAMPLE: How to add your own memory photos to the Dome Gallery
 * 
 * Replace the DEFAULT_IMAGES array in assets/js/dome-gallery.js with this example
 */

// Example with your portfolio images
const MY_MEMORIES = [
  // Game Development Memories
  {
    src: 'assets/img/portfolio/mavericks-battleground-thumbnail.jpg',
    alt: 'Mavericks Battlegrounds - My First Multiplayer Game'
  },
  {
    src: 'assets/img/flappy-bird-thumbnail.jpg',
    alt: 'Floppy Ball - First Unity Game'
  },
  {
    src: 'assets/img/masonry-portfolio/dharmik-gohil-mario-clone-game-project.png',
    alt: 'MiniMario - Learning Game Development'
  },
  
  // University Memories
  {
    src: 'assets/img/dharmik-gohil-professional-headshot-photo.png',
    alt: 'Professional Headshot'
  },
  
  // Event Memories
  {
    src: 'assets/img/blog/techfest-event-photo.jpg', // Add your actual photos
    alt: 'IIT Bombay Techfest 2024'
  },
  {
    src: 'assets/img/blog/hackathon-team-photo.jpg', // Add your actual photos
    alt: 'Hackron Hackathon 2025'
  },
  
  // Personal Projects
  {
    src: 'assets/img/portfolio/dharmik-gohil-industry-game-project.jpg',
    alt: 'Hotel H - Industry Game Project'
  },
  {
    src: 'assets/img/portfolio/dharmik-gohil-creative-design-portfolio-showcase.jpg',
    alt: 'Trash In Pro - Environmental Game'
  },
  
  // VR/AR Projects
  {
    src: 'assets/dharmik-gohil-vr-gaming-expertise-showcase.jpg',
    alt: 'Space Explorer VR Project'
  },
  {
    src: 'assets/img/ar-explorer-thumbnail.jpg',
    alt: 'AR Explorer Application'
  },
  
  // Community Work
  {
    src: 'assets/img/indian-developer-community-logo.png',
    alt: 'Indian Developer Community - Co-Founder'
  },
  
  // Add more memories...
];

/**
 * STEP-BY-STEP GUIDE TO ADD YOUR OWN PHOTOS:
 * 
 * 1. Prepare Your Images:
 *    - Recommended size: 800x600px or similar aspect ratio
 *    - Format: JPG, PNG, or WebP
 *    - Location: Save in assets/img/memories/ folder (create if doesn't exist)
 * 
 * 2. Add Image to Array:
 *    {
 *      src: 'path/to/your/image.jpg',
 *      alt: 'Description for accessibility'
 *    }
 * 
 * 3. Categories to Consider:
 *    - Game Development Milestones
 *    - University Events
 *    - Hackathons & Competitions
 *    - Team Photos
 *    - Personal Projects
 *    - Awards & Achievements
 *    - Community Events
 *    - Technical Workshops
 * 
 * 4. Best Practices:
 *    - Use descriptive alt text for accessibility
 *    - Keep image file sizes optimized (< 500KB)
 *    - Use consistent image dimensions when possible
 *    - Name files descriptively (e.g., techfest-2024-team.jpg)
 * 
 * 5. Replace in dome-gallery.js:
 *    - Open: assets/js/dome-gallery.js
 *    - Find: const DEFAULT_IMAGES = [...]
 *    - Replace with: const DEFAULT_IMAGES = MY_MEMORIES (from this file)
 */

// Quick Test Array (7 images minimum recommended)
const QUICK_TEST_MEMORIES = [
  { src: 'assets/img/dharmik-gohil-professional-headshot-photo.png', alt: 'Me' },
  { src: 'assets/img/portfolio/mavericks-battleground-thumbnail.jpg', alt: 'Game 1' },
  { src: 'assets/img/flappy-bird-thumbnail.jpg', alt: 'Game 2' },
  { src: 'assets/img/masonry-portfolio/dharmik-gohil-mario-clone-game-project.png', alt: 'Game 3' },
  { src: 'assets/dharmik-gohil-vr-gaming-expertise-showcase.jpg', alt: 'VR Project' },
  { src: 'assets/img/indian-developer-community-logo.png', alt: 'Community' },
  { src: 'assets/img/portfolio/dharmik-gohil-industry-game-project.jpg', alt: 'Industry Game' }
];
