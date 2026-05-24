/**
 * LetterGlitch - A high-performance canvas-based matrix/glitch character effect.
 * Ported from React to Vanilla JS for seamless integration.
 */
class LetterGlitch {
  constructor(container, options = {}) {
    this.container = typeof container === 'string' ? document.querySelector(container) : container;
    if (!this.container) return;

    // Merge options with defaults (supporting both glitchColors/colors and various vignette naming schemes)
    const colors = options.colors || options.glitchColors || ['#2b4539', '#61dca3', '#61b3dc'];
    this.glitchColors = colors;
    this.glitchSpeed = options.glitchSpeed !== undefined ? options.glitchSpeed : 50;
    
    this.centerVignette = options.centerVignette !== undefined ? options.centerVignette : (options.showCenterVignette !== undefined ? options.showCenterVignette : false);
    this.outerVignette = options.outerVignette !== undefined ? options.outerVignette : (options.showOuterVignette !== undefined ? options.showOuterVignette : true);
    
    this.smooth = options.smooth !== undefined ? options.smooth : true;
    this.characters = options.characters || 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$&*()-_+=/[]{};:<>.,0123456789';
    this.backgroundColor = options.backgroundColor || '#000000';

    // Internal state
    this.canvas = null;
    this.ctx = null;
    this.animationId = null;
    this.letters = [];
    this.grid = { columns: 0, rows: 0 };
    this.lastGlitchTime = Date.now();
    this.resizeTimeout = null;

    this.lettersAndSymbols = Array.from(this.characters);
    this.fontSize = 16;
    this.charWidth = 10;
    this.charHeight = 20;

    this.init();
  }

  init() {
    // Style container
    this.container.style.position = 'relative';
    this.container.style.width = '100%';
    this.container.style.height = '100%';
    this.container.style.backgroundColor = this.backgroundColor;
    this.container.style.overflow = 'hidden';

    // Create canvas
    this.canvas = document.createElement('canvas');
    this.canvas.style.display = 'block';
    this.canvas.style.width = '100%';
    this.canvas.style.height = '100%';
    this.container.appendChild(this.canvas);

    this.ctx = this.canvas.getContext('2d');

    // Add Vignettes if configured
    if (this.outerVignette) {
      const outerVignetteDiv = document.createElement('div');
      outerVignetteDiv.style.position = 'absolute';
      outerVignetteDiv.style.top = '0';
      outerVignetteDiv.style.left = '0';
      outerVignetteDiv.style.width = '100%';
      outerVignetteDiv.style.height = '100%';
      outerVignetteDiv.style.pointerEvents = 'none';
      outerVignetteDiv.style.background = 'radial-gradient(circle, rgba(0,0,0,0) 60%, rgba(0,0,0,1) 100%)';
      this.container.appendChild(outerVignetteDiv);
    }

    if (this.centerVignette) {
      const centerVignetteDiv = document.createElement('div');
      centerVignetteDiv.style.position = 'absolute';
      centerVignetteDiv.style.top = '0';
      centerVignetteDiv.style.left = '0';
      centerVignetteDiv.style.width = '100%';
      centerVignetteDiv.style.height = '100%';
      centerVignetteDiv.style.pointerEvents = 'none';
      centerVignetteDiv.style.background = 'radial-gradient(circle, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0) 60%)';
      this.container.appendChild(centerVignetteDiv);
    }

    // Bind event listener
    this.handleResize = this.handleResize.bind(this);
    window.addEventListener('resize', this.handleResize);

    // Initial setup
    this.resizeCanvas();
    this.animate();
  }

  getRandomChar() {
    return this.lettersAndSymbols[Math.floor(Math.random() * this.lettersAndSymbols.length)];
  }

  getRandomColor() {
    return this.glitchColors[Math.floor(Math.random() * this.glitchColors.length)];
  }

  hexToRgb(hex) {
    if (hex.startsWith('rgb')) {
      const parts = hex.match(/\d+/g);
      return parts ? { r: parseInt(parts[0]), g: parseInt(parts[1]), b: parseInt(parts[2]) } : null;
    }
    const shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
    const cleanHex = hex.replace(shorthandRegex, (m, r, g, b) => r + r + g + g + b + b);

    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(cleanHex);
    return result ? {
      r: parseInt(result[1], 16),
      g: parseInt(result[2], 16),
      b: parseInt(result[3], 16)
    } : null;
  }

  interpolateColor(start, end, factor) {
    const result = {
      r: Math.round(start.r + (end.r - start.r) * factor),
      g: Math.round(start.g + (end.g - start.g) * factor),
      b: Math.round(start.b + (end.b - start.b) * factor)
    };
    return `rgb(${result.r}, ${result.g}, ${result.b})`;
  }

  calculateGrid(width, height) {
    const columns = Math.ceil(width / this.charWidth);
    const rows = Math.ceil(height / this.charHeight);
    return { columns, rows };
  }

  initializeLetters(columns, rows) {
    this.grid = { columns, rows };
    const totalLetters = columns * rows;
    this.letters = Array.from({ length: totalLetters }, () => ({
      char: this.getRandomChar(),
      color: this.getRandomColor(),
      targetColor: this.getRandomColor(),
      colorProgress: 1
    }));
  }

  resizeCanvas() {
    if (!this.canvas) return;
    const parent = this.canvas.parentElement;
    if (!parent) return;

    const dpr = window.devicePixelRatio || 1;
    const rect = parent.getBoundingClientRect();

    this.canvas.width = rect.width * dpr;
    this.canvas.height = rect.height * dpr;

    this.canvas.style.width = `${rect.width}px`;
    this.canvas.style.height = `${rect.height}px`;

    if (this.ctx) {
      this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    const { columns, rows } = this.calculateGrid(rect.width, rect.height);
    this.initializeLetters(columns, rows);

    this.drawLetters();
  }

  drawLetters() {
    if (!this.ctx || this.letters.length === 0) return;
    const ctx = this.ctx;
    const { width, height } = this.canvas.getBoundingClientRect();
    ctx.clearRect(0, 0, width, height);
    ctx.font = `${this.fontSize}px monospace`;
    ctx.textBaseline = 'top';

    this.letters.forEach((letter, index) => {
      const x = (index % this.grid.columns) * this.charWidth;
      const y = Math.floor(index / this.grid.columns) * this.charHeight;
      ctx.fillStyle = letter.color;
      ctx.fillText(letter.char, x, y);
    });
  }

  updateLetters() {
    if (!this.letters || this.letters.length === 0) return;

    const updateCount = Math.max(1, Math.floor(this.letters.length * 0.05));

    for (let i = 0; i < updateCount; i++) {
      const index = Math.floor(Math.random() * this.letters.length);
      if (!this.letters[index]) continue;

      this.letters[index].char = this.getRandomChar();
      this.letters[index].targetColor = this.getRandomColor();

      if (!this.smooth) {
        this.letters[index].color = this.letters[index].targetColor;
        this.letters[index].colorProgress = 1;
      } else {
        this.letters[index].colorProgress = 0;
      }
    }
  }

  handleSmoothTransitions() {
    let needsRedraw = false;
    this.letters.forEach(letter => {
      if (letter.colorProgress < 1) {
        letter.colorProgress += 0.05;
        if (letter.colorProgress > 1) letter.colorProgress = 1;

        const startRgb = this.hexToRgb(letter.color);
        const endRgb = this.hexToRgb(letter.targetColor);
        if (startRgb && endRgb) {
          letter.color = this.interpolateColor(startRgb, endRgb, letter.colorProgress);
          needsRedraw = true;
        }
      }
    });

    if (needsRedraw) {
      this.drawLetters();
    }
  }

  animate() {
    const now = Date.now();
    if (now - this.lastGlitchTime >= this.glitchSpeed) {
      this.updateLetters();
      this.drawLetters();
      this.lastGlitchTime = now;
    }

    if (this.smooth) {
      this.handleSmoothTransitions();
    }

    this.animationId = requestAnimationFrame(() => this.animate());
  }

  handleResize() {
    clearTimeout(this.resizeTimeout);
    this.resizeTimeout = setTimeout(() => {
      cancelAnimationFrame(this.animationId);
      this.resizeCanvas();
      this.animate();
    }, 100);
  }

  destroy() {
    cancelAnimationFrame(this.animationId);
    window.removeEventListener('resize', this.handleResize);
    clearTimeout(this.resizeTimeout);
    if (this.canvas) {
      this.canvas.remove();
    }
  }
}

// Export for module systems and bind to window for global script usage
if (typeof window !== 'undefined') {
  window.LetterGlitch = LetterGlitch;
}
// Removed ES module 'export default' to prevent 'Unexpected token export' in standard non-module script tags.

