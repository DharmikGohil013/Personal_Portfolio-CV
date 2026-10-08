/* Motion system: kinetic type, reveals, hero field, tilt, magnetic buttons, pipeline.
   Everything is skipped when the user prefers reduced motion (no .motion-ok class). */
(function () {
  'use strict';
  var root = document.documentElement;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) { root.classList.remove('motion-ok'); return; }
  root.classList.add('motion-ok');
  window.__motionReady = true;

  var $ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var fine = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  /* ---------- Kinetic headline ---------- */
  function splitWords(el) {
    if (el.__split) return;
    el.__split = true;
    var i = 0;
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function (part) {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(' ')); return; }
            var w = document.createElement('span'); w.className = 'kw';
            var inner = document.createElement('span'); inner.style.setProperty('--i', i++); inner.textContent = part;
            w.appendChild(inner); frag.appendChild(w);
          });
          node.replaceChild(frag, n);
        } else if (n.nodeType === 1 && !/^(script|style)$/i.test(n.tagName)) walk(n);
      });
    })(el);
    el.classList.add('kinetic-ready');
    requestAnimationFrame(function () { requestAnimationFrame(function () { el.classList.add('kinetic-in'); }); });
  }
  $('[data-kinetic], .hero-editorial-headline, .post-title').forEach(function (el) {
    if (!el.hasAttribute('data-kinetic')) el.setAttribute('data-kinetic', '');
    splitWords(el);
  });

  /* ---------- Reveal on scroll ---------- */
  var AUTO = '.post-card, .hub-link, .aside-card, .aside-cta, .takeaways, .byline-box, .faq, .related, .post-nav, .link-hub, .cta-bar, .gallery-item, .stat-box, .team-member, .feature-card, .event-highlight, .tip-box, .orbit-copy, .pipeline li, .journal-head, .topic-nav';
  $(AUTO).forEach(function (el) { if (!el.hasAttribute('data-reveal')) el.setAttribute('data-reveal', ''); });
  $('[data-reveal]').forEach(function (el) {
    var sibs = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
    el.style.setProperty('--d', Math.min(sibs % 6, 5));
  });
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    $('[data-reveal]').forEach(function (el) { io.observe(el); });
    // titles: draw their rule when the section enters
    var tio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); tio.unobserve(en.target); } });
    }, { threshold: 0.4 });
    $('.section-title').forEach(function (el) { tio.observe(el); });
  } else {
    $('[data-reveal], .section-title').forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------- Hero field: drifting node graph that reacts to the cursor ---------- */
  var hero = document.getElementById('hero');
  if (hero) {
    var canvas = document.createElement('canvas');
    canvas.className = 'hero-field'; canvas.setAttribute('aria-hidden', 'true');
    hero.insertBefore(canvas, hero.firstChild);
    var ctx = canvas.getContext('2d');
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var W = 0, H = 0, nodes = [], mouse = { x: -999, y: -999, on: false }, running = false, raf = 0, inView = true;
    var small = window.innerWidth < 700;

    var resize = function () {
      var r = hero.getBoundingClientRect();
      W = r.width; H = r.height;
      canvas.width = W * dpr; canvas.height = H * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var count = Math.max(18, Math.min(small ? 34 : 72, Math.round((W * H) / 14000)));
      nodes = [];
      for (var i = 0; i < count; i++) {
        nodes.push({ x: Math.random() * W, y: Math.random() * H, vx: (Math.random() - .5) * .22, vy: (Math.random() - .5) * .22, r: Math.random() < .12 ? 3.2 : 1.8, hot: Math.random() < .12 });
      }
    };
    var LINK = small ? 90 : 130;
    var frame = function () {
      ctx.clearRect(0, 0, W, H);
      var i, j, a, b, dx, dy, d;
      for (i = 0; i < nodes.length; i++) {
        a = nodes[i];
        a.x += a.vx; a.y += a.vy;
        if (a.x < 0 || a.x > W) a.vx *= -1;
        if (a.y < 0 || a.y > H) a.vy *= -1;
        if (mouse.on) {
          dx = a.x - mouse.x; dy = a.y - mouse.y; d = Math.sqrt(dx * dx + dy * dy);
          if (d < 150 && d > 1) { a.x += (dx / d) * (150 - d) * 0.012; a.y += (dy / d) * (150 - d) * 0.012; }
        }
      }
      ctx.lineWidth = 1;
      for (i = 0; i < nodes.length; i++) {
        a = nodes[i];
        for (j = i + 1; j < nodes.length; j++) {
          b = nodes[j]; dx = a.x - b.x; dy = a.y - b.y; d = dx * dx + dy * dy;
          if (d < LINK * LINK) {
            ctx.strokeStyle = 'rgba(13,13,11,' + (0.16 * (1 - Math.sqrt(d) / LINK)).toFixed(3) + ')';
            ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
          }
        }
        if (mouse.on) {
          dx = a.x - mouse.x; dy = a.y - mouse.y; d = Math.sqrt(dx * dx + dy * dy);
          if (d < 190) {
            ctx.strokeStyle = 'rgba(200,0,26,' + (0.5 * (1 - d / 190)).toFixed(3) + ')';
            ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(mouse.x, mouse.y); ctx.stroke();
          }
        }
      }
      for (i = 0; i < nodes.length; i++) {
        a = nodes[i];
        ctx.fillStyle = a.hot ? 'rgba(200,0,26,.85)' : 'rgba(13,13,11,.42)';
        ctx.fillRect(a.x - a.r, a.y - a.r, a.r * 2, a.r * 2);
      }
      if (running) raf = requestAnimationFrame(frame);
    };
    var start = function () { if (!running && inView && !document.hidden) { running = true; raf = requestAnimationFrame(frame); } };
    var stop = function () { running = false; cancelAnimationFrame(raf); };
    resize();
    canvas.classList.add('on');
    start();
    var rt;
    window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(function () { small = window.innerWidth < 700; resize(); }, 200); });
    document.addEventListener('visibilitychange', function () { document.hidden ? stop() : start(); });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) { inView = es[0].isIntersecting; inView ? start() : stop(); }).observe(hero);
    }
    if (fine) {
      hero.addEventListener('pointermove', function (e) {
        var r = hero.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; mouse.on = true;
      });
      hero.addEventListener('pointerleave', function () { mouse.on = false; });
    }
  }

  /* ---------- Tilt + spotlight ---------- */
  if (fine) {
    $('.work-card, .post-card, .review-clip, .hub-link, .team-member, .feature-card').forEach(function (el) {
      el.classList.add('tilt');
      var pending = false, ev;
      el.addEventListener('pointermove', function (e) {
        ev = e;
        if (pending) return; pending = true;
        requestAnimationFrame(function () {
          pending = false;
          var r = el.getBoundingClientRect();
          var px = (ev.clientX - r.left) / r.width, py = (ev.clientY - r.top) / r.height;
          el.classList.add('tilting');
          el.style.setProperty('--ry', ((px - .5) * 7).toFixed(2) + 'deg');
          el.style.setProperty('--rx', ((.5 - py) * 6).toFixed(2) + 'deg');
          el.style.setProperty('--mx', (px * 100).toFixed(1) + '%');
          el.style.setProperty('--my', (py * 100).toFixed(1) + '%');
        });
      });
      el.addEventListener('pointerleave', function () {
        el.classList.remove('tilting');
        el.style.setProperty('--rx', '0deg'); el.style.setProperty('--ry', '0deg');
      });
    });

    /* ---------- Magnetic buttons ---------- */
    $('.cta-link, .btn-editorial-submit, .cta-btn, .aside-cta a, .journal-all').forEach(function (el) {
      el.classList.add('magnetic');
      el.addEventListener('pointermove', function (e) {
        var r = el.getBoundingClientRect();
        el.style.transform = 'translate(' + ((e.clientX - (r.left + r.width / 2)) * .18).toFixed(1) + 'px,' + ((e.clientY - (r.top + r.height / 2)) * .28).toFixed(1) + 'px)';
      });
      el.addEventListener('pointerleave', function () { el.style.transform = ''; });
    });
  }

  /* ---------- Pipeline: line fills with scroll, steps light up ---------- */
  var pipes = $('.pipeline');
  if (pipes.length) {
    var onScroll = function () {
      pipes.forEach(function (p) {
        var r = p.getBoundingClientRect(), vh = window.innerHeight;
        var prog = Math.min(1, Math.max(0, (vh * .72 - r.top) / (r.height + vh * .25)));
        p.style.setProperty('--p', prog.toFixed(3));
        var steps = $('li', p);
        steps.forEach(function (li, i) { li.classList.toggle('lit', prog >= (i + .15) / steps.length); });
      });
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    onScroll();
  }
})();
