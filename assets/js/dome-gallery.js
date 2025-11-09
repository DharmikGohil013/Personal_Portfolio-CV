/**
 * Dome Gallery - Vanilla JavaScript Implementation
 * A 3D spherical photo gallery with interactive rotation
 */

const DEFAULT_IMAGES = [
  // Code Arena 1.0 - Darshan University
  { src: 'assets/img/memories/events/event-code-arena-01.jpg', alt: 'Code Arena 1.0 - Darshan University' },
  
  // Hackron Hackathon 2025 Memories
  { src: 'assets/img/memories/events/event-hackron-06.jpg', alt: 'Hackron Hackathon - Team Collaboration' },
  { src: 'assets/img/memories/events/event-hackron-07.jpg', alt: 'Hackron Hackathon - Coding Session' },
  { src: 'assets/img/memories/events/event-hackron-08.jpg', alt: 'Hackron Hackathon - Innovation Hub' },
  { src: 'assets/img/memories/events/event-hackron-10.jpg', alt: 'Hackron Hackathon - Development Phase' },
  { src: 'assets/img/memories/events/event-hackron-11.jpg', alt: 'Hackron Hackathon - Team Discussion' },
  { src: 'assets/img/memories/events/event-hackron-12.jpg', alt: 'Hackron Hackathon - Project Building' },
  { src: 'assets/img/memories/events/event-hackron-13.jpg', alt: 'Hackron Hackathon - Code & Coffee' },
  { src: 'assets/img/memories/events/event-hackron-14.jpg', alt: 'Hackron Hackathon - Late Night Coding' },
  { src: 'assets/img/memories/events/event-hackron-15.jpg', alt: 'Hackron Hackathon - Team Spirit' },
  { src: 'assets/img/memories/events/event-hackron-16.jpg', alt: 'Hackron Hackathon - Innovation Time' },
  { src: 'assets/img/memories/events/event-hackron-17.jpg', alt: 'Hackron Hackathon - Brainstorming' },
  { src: 'assets/img/memories/events/event-hackron-18.jpg', alt: 'Hackron Hackathon - Tech Talk' },
  { src: 'assets/img/memories/events/event-hackron-19.jpg', alt: 'Hackron Hackathon - Development Zone' },
  { src: 'assets/img/memories/events/event-hackron-20.jpg', alt: 'Hackron Hackathon - Collaboration' },
  { src: 'assets/img/memories/events/event-hackron-21.jpg', alt: 'Hackron Hackathon - Presentation Prep' },
  { src: 'assets/img/memories/events/event-hackron-22.jpg', alt: 'Hackron Hackathon - Final Sprint' },
  { src: 'assets/img/memories/events/event-hackron-23.jpg', alt: 'Hackron Hackathon - Team Victory' },
  { src: 'assets/img/memories/events/event-hackron-24.jpg', alt: 'Hackron Hackathon - Success Moment' },
  { src: 'assets/img/memories/events/event-hackron-25.jpg', alt: 'Hackron Hackathon - Achievement' },
  { src: 'assets/img/memories/events/event-hackron-26.jpg', alt: 'Hackron Hackathon - Winning Team' },
  { src: 'assets/img/memories/events/event-hackron-27.jpg', alt: 'Hackron Hackathon - Champions' },
  { src: 'assets/img/memories/events/event-hackron-28.jpg', alt: 'Hackron Hackathon - Celebration' },
  { src: 'assets/img/memories/events/event-hackron-29.jpg', alt: 'Hackron Hackathon - Memorable Moments' },
  { src: 'assets/img/memories/events/event-hackron-30.jpg', alt: 'Hackron Hackathon - Group Photo' },
  { src: 'assets/img/memories/events/event-hackron-31.jpg', alt: 'Hackron Hackathon - Team Together' },
  { src: 'assets/img/memories/events/event-hackron-32.jpg', alt: 'Hackron Hackathon - Final Demo' },
  { src: 'assets/img/memories/events/event-hackron-33.jpg', alt: 'Hackron Hackathon - Project Showcase' },
  { src: 'assets/img/memories/events/event-hackron-34.jpg', alt: 'Hackron Hackathon - Innovation Award' },
  { src: 'assets/img/memories/events/event-hackron-35.jpg', alt: 'Hackron Hackathon - Tech Excellence' },
  { src: 'assets/img/memories/events/event-hackron-36.jpg', alt: 'Hackron Hackathon - Winners Circle' },
  { src: 'assets/img/memories/events/event-hackron-37.jpg', alt: 'Hackron Hackathon - Achievement Unlocked' },
  { src: 'assets/img/memories/events/event-hackron-38.jpg', alt: 'Hackron Hackathon - Victory Pose' },
  { src: 'assets/img/memories/events/event-hackron-39.jpg', alt: 'Hackron Hackathon - Final Celebration' },
  { src: 'assets/img/memories/events/event-hackron-40.jpg', alt: 'Hackron Hackathon - Team Success' },
  
  // IIT Bombay TechFest 2024
  { src: 'assets/img/memories/events/event-techfest-15.jpg', alt: 'IIT Bombay TechFest - Campus Visit' },
  { src: 'assets/img/memories/events/event-techfest-17.jpg', alt: 'IIT Bombay TechFest - Tech Exhibition' },
  { src: 'assets/img/memories/events/event-techfest-20.jpg', alt: 'IIT Bombay TechFest - Innovation Fair' },
  
  // Odoo x CHARUSAT 2025
  { src: 'assets/img/memories/events/event-odoo-03.JPG', alt: 'Odoo CHARUSAT - Tech Workshop' },
  { src: 'assets/img/memories/events/event-odoo-07.jpg', alt: 'Odoo CHARUSAT - Development Session' }
];

const DEFAULTS = {
  maxVerticalRotationDeg: 5,
  dragSensitivity: 20,
  enlargeTransitionMs: 300,
  segments: 35
};

class DomeGallery {
  constructor(containerId, options = {}) {
    console.log('🔧 DomeGallery Constructor: Starting initialization for', containerId);
    
    this.containerId = containerId;
    this.options = {
      images: options.images || DEFAULT_IMAGES,
      fit: options.fit || 0.5,
      fitBasis: options.fitBasis || 'auto',
      minRadius: options.minRadius || 600,
      maxRadius: options.maxRadius || Infinity,
      padFactor: options.padFactor || 0.25,
      overlayBlurColor: options.overlayBlurColor || '#060010',
      maxVerticalRotationDeg: options.maxVerticalRotationDeg || DEFAULTS.maxVerticalRotationDeg,
      dragSensitivity: options.dragSensitivity || DEFAULTS.dragSensitivity,
      enlargeTransitionMs: options.enlargeTransitionMs || DEFAULTS.enlargeTransitionMs,
      segments: options.segments || DEFAULTS.segments,
      dragDampening: options.dragDampening || 2,
      openedImageWidth: options.openedImageWidth || '250px',
      openedImageHeight: options.openedImageHeight || '350px',
      imageBorderRadius: options.imageBorderRadius || '30px',
      openedImageBorderRadius: options.openedImageBorderRadius || '30px',
      grayscale: options.grayscale !== undefined ? options.grayscale : true
    };
    
    console.log(`📊 DomeGallery: Images count: ${this.options.images.length}, Segments: ${this.options.segments}`);

    this.rotation = { x: 0, y: 0 };
    this.startRot = { x: 0, y: 0 };
    this.startPos = null;
    this.dragging = false;
    this.moved = false;
    this.inertiaRAF = null;
    this.opening = false;
    this.openStartedAt = 0;
    this.lastDragEndAt = 0;
    this.focusedEl = null;
    this.originalTilePosition = null;
    this.scrollLocked = false;
    this.lockedRadius = null;

    this.init();
  }

  clamp(v, min, max) {
    return Math.min(Math.max(v, min), max);
  }

  normalizeAngle(d) {
    return ((d % 360) + 360) % 360;
  }

  wrapAngleSigned(deg) {
    const a = (((deg + 180) % 360) + 360) % 360;
    return a - 180;
  }

  getDataNumber(el, name, fallback) {
    const attr = el.dataset[name] || el.getAttribute(`data-${name}`);
    const n = attr == null ? NaN : parseFloat(attr);
    return Number.isFinite(n) ? n : fallback;
  }

  buildItems(pool, seg) {
    const xCols = Array.from({ length: seg }, (_, i) => -37 + i * 2);
    const evenYs = [-4, -2, 0, 2, 4];
    const oddYs = [-3, -1, 1, 3, 5];

    const coords = xCols.flatMap((x, c) => {
      const ys = c % 2 === 0 ? evenYs : oddYs;
      return ys.map(y => ({ x, y, sizeX: 2, sizeY: 2 }));
    });

    const totalSlots = coords.length;
    if (pool.length === 0) {
      return coords.map(c => ({ ...c, src: '', alt: '' }));
    }

    const normalizedImages = pool.map(image => {
      if (typeof image === 'string') {
        return { src: image, alt: '' };
      }
      return { src: image.src || '', alt: image.alt || '' };
    });

    const usedImages = Array.from({ length: totalSlots }, (_, i) => normalizedImages[i % normalizedImages.length]);

    for (let i = 1; i < usedImages.length; i++) {
      if (usedImages[i].src === usedImages[i - 1].src) {
        for (let j = i + 1; j < usedImages.length; j++) {
          if (usedImages[j].src !== usedImages[i].src) {
            const tmp = usedImages[i];
            usedImages[i] = usedImages[j];
            usedImages[j] = tmp;
            break;
          }
        }
      }
    }

    return coords.map((c, i) => ({
      ...c,
      src: usedImages[i].src,
      alt: usedImages[i].alt
    }));
  }

  computeItemBaseRotation(offsetX, offsetY, sizeX, sizeY, segments) {
    const unit = 360 / segments / 2;
    const rotateY = unit * (offsetX + (sizeX - 1) / 2);
    const rotateX = unit * (offsetY - (sizeY - 1) / 2);
    return { rotateX, rotateY };
  }

  applyTransform(xDeg, yDeg) {
    if (this.sphereRef) {
      this.sphereRef.style.transform = `translateZ(calc(var(--radius) * -1)) rotateX(${xDeg}deg) rotateY(${yDeg}deg)`;
    }
  }

  lockScroll() {
    if (this.scrollLocked) return;
    this.scrollLocked = true;
    document.body.classList.add('dg-scroll-lock');
  }

  unlockScroll() {
    if (!this.scrollLocked) return;
    if (this.rootRef?.getAttribute('data-enlarging') === 'true') return;
    this.scrollLocked = false;
    document.body.classList.remove('dg-scroll-lock');
  }

  stopInertia() {
    if (this.inertiaRAF) {
      cancelAnimationFrame(this.inertiaRAF);
      this.inertiaRAF = null;
    }
  }

  startInertia(vx, vy) {
    const MAX_V = 1.4;
    let vX = this.clamp(vx, -MAX_V, MAX_V) * 80;
    let vY = this.clamp(vy, -MAX_V, MAX_V) * 80;
    let frames = 0;
    const d = this.clamp(this.options.dragDampening ?? 0.6, 0, 1);
    const frictionMul = 0.94 + 0.055 * d;
    const stopThreshold = 0.015 - 0.01 * d;
    const maxFrames = Math.round(90 + 270 * d);
    
    const step = () => {
      vX *= frictionMul;
      vY *= frictionMul;
      if (Math.abs(vX) < stopThreshold && Math.abs(vY) < stopThreshold) {
        this.inertiaRAF = null;
        return;
      }
      if (++frames > maxFrames) {
        this.inertiaRAF = null;
        return;
      }
      const nextX = this.clamp(this.rotation.x - vY / 200, -this.options.maxVerticalRotationDeg, this.options.maxVerticalRotationDeg);
      const nextY = this.wrapAngleSigned(this.rotation.y + vX / 200);
      this.rotation = { x: nextX, y: nextY };
      this.applyTransform(nextX, nextY);
      this.inertiaRAF = requestAnimationFrame(step);
    };
    
    this.stopInertia();
    this.inertiaRAF = requestAnimationFrame(step);
  }

  handleDragStart(e) {
    if (this.focusedEl) return;
    this.stopInertia();
    this.dragging = true;
    this.moved = false;
    this.startRot = { ...this.rotation };
    this.startPos = { x: e.clientX, y: e.clientY };
  }

  handleDragMove(e) {
    if (this.focusedEl || !this.dragging || !this.startPos) return;
    
    const dxTotal = e.clientX - this.startPos.x;
    const dyTotal = e.clientY - this.startPos.y;
    
    if (!this.moved) {
      const dist2 = dxTotal * dxTotal + dyTotal * dyTotal;
      if (dist2 > 16) this.moved = true;
    }
    
    const nextX = this.clamp(
      this.startRot.x - dyTotal / this.options.dragSensitivity,
      -this.options.maxVerticalRotationDeg,
      this.options.maxVerticalRotationDeg
    );
    const nextY = this.wrapAngleSigned(this.startRot.y + dxTotal / this.options.dragSensitivity);
    
    if (this.rotation.x !== nextX || this.rotation.y !== nextY) {
      this.rotation = { x: nextX, y: nextY };
      this.applyTransform(nextX, nextY);
    }
  }

  handleDragEnd(e) {
    if (!this.dragging) return;
    this.dragging = false;
    
    const dxTotal = e.clientX - this.startPos.x;
    const dyTotal = e.clientY - this.startPos.y;
    
    const vx = this.clamp((dxTotal / this.options.dragSensitivity) * 0.02, -1.2, 1.2);
    const vy = this.clamp((dyTotal / this.options.dragSensitivity) * 0.02, -1.2, 1.2);
    
    if (Math.abs(vx) > 0.005 || Math.abs(vy) > 0.005) {
      this.startInertia(vx, vy);
    }
    
    if (this.moved) {
      this.lastDragEndAt = performance.now();
    }
    this.moved = false;
  }

  openItemFromElement(el) {
    if (this.opening) return;
    this.opening = true;
    this.openStartedAt = performance.now();
    this.lockScroll();
    
    const parent = el.parentElement;
    this.focusedEl = el;
    el.setAttribute('data-focused', 'true');
    
    const offsetX = this.getDataNumber(parent, 'offsetX', 0);
    const offsetY = this.getDataNumber(parent, 'offsetY', 0);
    const sizeX = this.getDataNumber(parent, 'sizeX', 2);
    const sizeY = this.getDataNumber(parent, 'sizeY', 2);
    
    const parentRot = this.computeItemBaseRotation(offsetX, offsetY, sizeX, sizeY, this.options.segments);
    const parentY = this.normalizeAngle(parentRot.rotateY);
    const globalY = this.normalizeAngle(this.rotation.y);
    
    let rotY = -(parentY + globalY) % 360;
    if (rotY < -180) rotY += 360;
    const rotX = -parentRot.rotateX - this.rotation.x;
    
    parent.style.setProperty('--rot-y-delta', `${rotY}deg`);
    parent.style.setProperty('--rot-x-delta', `${rotX}deg`);
    
    const refDiv = document.createElement('div');
    refDiv.className = 'item__image item__image--reference';
    refDiv.style.opacity = '0';
    refDiv.style.transform = `rotateX(${-parentRot.rotateX}deg) rotateY(${-parentRot.rotateY}deg)`;
    parent.appendChild(refDiv);
    
    void refDiv.offsetHeight;
    
    const tileR = refDiv.getBoundingClientRect();
    const mainR = this.mainRef?.getBoundingClientRect();
    const frameR = this.frameRef?.getBoundingClientRect();
    
    if (!mainR || !frameR || tileR.width <= 0 || tileR.height <= 0) {
      this.opening = false;
      this.focusedEl = null;
      parent.removeChild(refDiv);
      this.unlockScroll();
      return;
    }
    
    this.originalTilePosition = { 
      left: tileR.left, 
      top: tileR.top, 
      width: tileR.width, 
      height: tileR.height 
    };
    
    el.style.visibility = 'hidden';
    el.style.zIndex = 0;
    
    const overlay = document.createElement('div');
    overlay.className = 'enlarge';
    overlay.style.position = 'absolute';
    overlay.style.left = frameR.left - mainR.left + 'px';
    overlay.style.top = frameR.top - mainR.top + 'px';
    overlay.style.width = frameR.width + 'px';
    overlay.style.height = frameR.height + 'px';
    overlay.style.opacity = '0';
    overlay.style.zIndex = '30';
    overlay.style.willChange = 'transform, opacity';
    overlay.style.transformOrigin = 'top left';
    overlay.style.transition = `transform ${this.options.enlargeTransitionMs}ms ease, opacity ${this.options.enlargeTransitionMs}ms ease`;
    
    const rawSrc = parent.dataset.src || el.querySelector('img')?.src || '';
    const img = document.createElement('img');
    img.src = rawSrc;
    overlay.appendChild(img);
    this.viewerRef.appendChild(overlay);
    
    const tx0 = tileR.left - frameR.left;
    const ty0 = tileR.top - frameR.top;
    const sx0 = tileR.width / frameR.width;
    const sy0 = tileR.height / frameR.height;
    
    const validSx0 = isFinite(sx0) && sx0 > 0 ? sx0 : 1;
    const validSy0 = isFinite(sy0) && sy0 > 0 ? sy0 : 1;
    
    overlay.style.transform = `translate(${tx0}px, ${ty0}px) scale(${validSx0}, ${validSy0})`;
    
    setTimeout(() => {
      if (!overlay.parentElement) return;
      overlay.style.opacity = '1';
      overlay.style.transform = 'translate(0px, 0px) scale(1, 1)';
      this.rootRef?.setAttribute('data-enlarging', 'true');
    }, 16);
  }

  closeEnlarged() {
    if (performance.now() - this.openStartedAt < 250) return;
    const el = this.focusedEl;
    if (!el) return;
    
    const parent = el.parentElement;
    const overlay = this.viewerRef?.querySelector('.enlarge');
    if (!overlay) return;
    
    const refDiv = parent.querySelector('.item__image--reference');
    const originalPos = this.originalTilePosition;
    
    if (!originalPos) {
      overlay.remove();
      if (refDiv) refDiv.remove();
      parent.style.setProperty('--rot-y-delta', '0deg');
      parent.style.setProperty('--rot-x-delta', '0deg');
      el.style.visibility = '';
      el.style.zIndex = 0;
      this.focusedEl = null;
      this.rootRef?.removeAttribute('data-enlarging');
      this.opening = false;
      this.unlockScroll();
      return;
    }
    
    const currentRect = overlay.getBoundingClientRect();
    const rootRect = this.rootRef.getBoundingClientRect();
    
    const originalPosRelativeToRoot = {
      left: originalPos.left - rootRect.left,
      top: originalPos.top - rootRect.top,
      width: originalPos.width,
      height: originalPos.height
    };
    
    const overlayRelativeToRoot = {
      left: currentRect.left - rootRect.left,
      top: currentRect.top - rootRect.top,
      width: currentRect.width,
      height: currentRect.height
    };
    
    const animatingOverlay = document.createElement('div');
    animatingOverlay.className = 'enlarge-closing';
    animatingOverlay.style.cssText = `position:absolute;left:${overlayRelativeToRoot.left}px;top:${overlayRelativeToRoot.top}px;width:${overlayRelativeToRoot.width}px;height:${overlayRelativeToRoot.height}px;z-index:9999;border-radius: var(--enlarge-radius, 32px);overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,.35);transition:all ${this.options.enlargeTransitionMs}ms ease-out;pointer-events:none;margin:0;transform:none;`;
    
    const originalImg = overlay.querySelector('img');
    if (originalImg) {
      const img = originalImg.cloneNode();
      img.style.cssText = 'width:100%;height:100%;object-fit:cover;';
      animatingOverlay.appendChild(img);
    }
    
    overlay.remove();
    this.rootRef.appendChild(animatingOverlay);
    
    void animatingOverlay.getBoundingClientRect();
    
    requestAnimationFrame(() => {
      animatingOverlay.style.left = originalPosRelativeToRoot.left + 'px';
      animatingOverlay.style.top = originalPosRelativeToRoot.top + 'px';
      animatingOverlay.style.width = originalPosRelativeToRoot.width + 'px';
      animatingOverlay.style.height = originalPosRelativeToRoot.height + 'px';
      animatingOverlay.style.opacity = '0';
    });
    
    const cleanup = () => {
      animatingOverlay.remove();
      this.originalTilePosition = null;
      if (refDiv) refDiv.remove();
      parent.style.transition = 'none';
      el.style.transition = 'none';
      parent.style.setProperty('--rot-y-delta', '0deg');
      parent.style.setProperty('--rot-x-delta', '0deg');
      
      requestAnimationFrame(() => {
        el.style.visibility = '';
        el.style.opacity = '0';
        el.style.zIndex = 0;
        this.focusedEl = null;
        this.rootRef?.removeAttribute('data-enlarging');
        
        requestAnimationFrame(() => {
          parent.style.transition = '';
          el.style.transition = 'opacity 300ms ease-out';
          
          requestAnimationFrame(() => {
            el.style.opacity = '1';
            
            setTimeout(() => {
              el.style.transition = '';
              el.style.opacity = '';
              this.opening = false;
              if (!this.dragging && this.rootRef?.getAttribute('data-enlarging') !== 'true') {
                document.body.classList.remove('dg-scroll-lock');
              }
            }, 300);
          });
        });
      });
    };
    
    animatingOverlay.addEventListener('transitionend', cleanup, { once: true });
  }

  setupResizeObserver() {
    const root = this.rootRef;
    if (!root) return;
    
    const ro = new ResizeObserver(entries => {
      const cr = entries[0].contentRect;
      const w = Math.max(1, cr.width);
      const h = Math.max(1, cr.height);
      const minDim = Math.min(w, h);
      const maxDim = Math.max(w, h);
      const aspect = w / h;
      
      let basis;
      switch (this.options.fitBasis) {
        case 'min':
          basis = minDim;
          break;
        case 'max':
          basis = maxDim;
          break;
        case 'width':
          basis = w;
          break;
        case 'height':
          basis = h;
          break;
        default:
          basis = aspect >= 1.3 ? w : minDim;
      }
      
      let radius = basis * this.options.fit;
      const heightGuard = h * 1.35;
      radius = Math.min(radius, heightGuard);
      radius = this.clamp(radius, this.options.minRadius, this.options.maxRadius);
      this.lockedRadius = Math.round(radius);
      
      const viewerPad = Math.max(8, Math.round(minDim * this.options.padFactor));
      root.style.setProperty('--radius', `${this.lockedRadius}px`);
      root.style.setProperty('--viewer-pad', `${viewerPad}px`);
      root.style.setProperty('--overlay-blur-color', this.options.overlayBlurColor);
      root.style.setProperty('--tile-radius', this.options.imageBorderRadius);
      root.style.setProperty('--enlarge-radius', this.options.openedImageBorderRadius);
      root.style.setProperty('--image-filter', this.options.grayscale ? 'grayscale(1)' : 'none');
      
      this.applyTransform(this.rotation.x, this.rotation.y);
    });
    
    ro.observe(root);
    this.resizeObserver = ro;
  }

  render() {
    const items = this.buildItems(this.options.images, this.options.segments);
    
    const html = `
      <div class="sphere-root" style="--segments-x: ${this.options.segments}; --segments-y: ${this.options.segments};">
        <main class="sphere-main">
          <div class="stage">
            <div class="sphere">
              ${items.map((it, i) => `
                <div class="item" 
                     data-src="${it.src}"
                     data-offset-x="${it.x}"
                     data-offset-y="${it.y}"
                     data-size-x="${it.sizeX}"
                     data-size-y="${it.sizeY}"
                     style="--offset-x: ${it.x}; --offset-y: ${it.y}; --item-size-x: ${it.sizeX}; --item-size-y: ${it.sizeY};">
                  <div class="item__image" role="button" tabindex="0" aria-label="${it.alt || 'Open image'}">
                    <img src="${it.src}" draggable="false" alt="${it.alt}" />
                  </div>
                </div>
              `).join('')}
            </div>
          </div>
          <div class="overlay"></div>
          <div class="overlay overlay--blur"></div>
          <div class="edge-fade edge-fade--top"></div>
          <div class="edge-fade edge-fade--bottom"></div>
          <div class="viewer">
            <div class="scrim"></div>
            <div class="frame"></div>
          </div>
        </main>
      </div>
    `;
    
    const container = document.getElementById(this.containerId);
    if (container) {
      container.innerHTML = html;
    }
  }

  bindEvents() {
    this.rootRef = document.querySelector(`#${this.containerId} .sphere-root`);
    this.mainRef = this.rootRef?.querySelector('.sphere-main');
    this.sphereRef = this.rootRef?.querySelector('.sphere');
    this.frameRef = this.rootRef?.querySelector('.frame');
    this.viewerRef = this.rootRef?.querySelector('.viewer');
    this.scrimRef = this.rootRef?.querySelector('.scrim');
    
    if (!this.mainRef) return;
    
    // Mouse drag events
    this.mainRef.addEventListener('mousedown', (e) => this.handleDragStart(e));
    document.addEventListener('mousemove', (e) => this.handleDragMove(e));
    document.addEventListener('mouseup', (e) => this.handleDragEnd(e));
    
    // Touch drag events
    this.mainRef.addEventListener('touchstart', (e) => {
      const touch = e.touches[0];
      this.handleDragStart({ clientX: touch.clientX, clientY: touch.clientY });
    });
    document.addEventListener('touchmove', (e) => {
      if (e.touches.length > 0) {
        const touch = e.touches[0];
        this.handleDragMove({ clientX: touch.clientX, clientY: touch.clientY });
      }
    });
    document.addEventListener('touchend', (e) => {
      if (e.changedTouches.length > 0) {
        const touch = e.changedTouches[0];
        this.handleDragEnd({ clientX: touch.clientX, clientY: touch.clientY });
      }
    });
    
    // Click on tiles
    const tiles = this.rootRef.querySelectorAll('.item__image');
    tiles.forEach(tile => {
      tile.addEventListener('click', (e) => {
        if (this.dragging || this.moved) return;
        if (performance.now() - this.lastDragEndAt < 80) return;
        if (this.opening) return;
        this.openItemFromElement(e.currentTarget);
      });
    });
    
    // Click on scrim to close
    if (this.scrimRef) {
      this.scrimRef.addEventListener('click', () => this.closeEnlarged());
    }
    
    // ESC key to close
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') this.closeEnlarged();
    });
  }

  init() {
    console.log('🚀 DomeGallery.init(): Starting initialization sequence');
    this.render();
    console.log('✅ DomeGallery.init(): Render complete');
    this.bindEvents();
    console.log('✅ DomeGallery.init(): Events bound');
    this.setupResizeObserver();
    console.log('✅ DomeGallery.init(): ResizeObserver setup');
    this.applyTransform(0, 0);
    console.log('✅ DomeGallery.init(): Initial transform applied');
  }

  destroy() {
    if (this.resizeObserver) {
      this.resizeObserver.disconnect();
    }
    this.stopInertia();
    this.unlockScroll();
    const container = document.getElementById(this.containerId);
    if (container) {
      container.innerHTML = '';
    }
  }
}

// Initialize the gallery when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
  console.log('🎨 Dome Gallery: DOM loaded, initializing...');
  
  const galleryContainer = document.getElementById('domeGallery');
  
  if (!galleryContainer) {
    console.error('❌ Dome Gallery: Container #domeGallery not found!');
    return;
  }
  
  console.log('✅ Dome Gallery: Container found, creating gallery...');
  console.log(`📸 Dome Gallery: Loading ${DEFAULT_IMAGES.length} images`);
  
  try {
    new DomeGallery('domeGallery', {
      images: DEFAULT_IMAGES,
      fit: 0.5,
      segments: 35,
      grayscale: true,
      imageBorderRadius: '30px',
      openedImageBorderRadius: '30px'
    });
    console.log('🎉 Dome Gallery: Successfully initialized!');
  } catch (error) {
    console.error('❌ Dome Gallery Error:', error);
  }
});
