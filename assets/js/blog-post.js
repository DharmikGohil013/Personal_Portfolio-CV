/* Blog pages: mobile drawer, reading progress, TOC scroll-spy, copy-link, lightbox. */
(function () {
  'use strict';

  /* ---------- Mobile drawer ---------- */
  var drawer = document.getElementById('mobileDrawer');
  var overlay = document.getElementById('drawerOverlay');
  var toggle = document.getElementById('menuToggleBtn');
  var closeBtn = document.getElementById('closeDrawerBtn');
  function setDrawer(open) {
    if (!drawer || !overlay) return;
    drawer.classList.toggle('open', open);
    overlay.classList.toggle('active', open);
    document.body.style.overflow = open ? 'hidden' : '';
  }
  if (toggle) toggle.addEventListener('click', function (e) { e.preventDefault(); setDrawer(true); });
  if (closeBtn) closeBtn.addEventListener('click', function () { setDrawer(false); });
  if (overlay) overlay.addEventListener('click', function () { setDrawer(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setDrawer(false); });
  document.querySelectorAll('.drawer-accordion-trigger').forEach(function (t) {
    t.addEventListener('click', function (e) {
      e.stopPropagation();
      var p = t.parentElement;
      document.querySelectorAll('.drawer-accordion').forEach(function (a) { if (a !== p) a.classList.remove('active'); });
      p.classList.toggle('active');
    });
  });

  /* ---------- Reading progress ---------- */
  var bar = document.querySelector('.read-progress > i');
  var article = document.querySelector('.article-body') || document.querySelector('.post-shell');
  if (bar && article) {
    var ticking = false;
    var update = function () {
      var r = article.getBoundingClientRect();
      var total = r.height - window.innerHeight * 0.6;
      var done = Math.min(Math.max(-r.top + window.innerHeight * 0.2, 0), total);
      bar.style.transform = 'scaleX(' + (total > 0 ? done / total : 0) + ')';
      ticking = false;
    };
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    window.addEventListener('resize', update);
    update();
  }

  /* ---------- TOC scroll-spy ---------- */
  var heads = Array.prototype.slice.call(document.querySelectorAll('.article-body h2[id]'));
  var links = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  if (heads.length && links.length && 'IntersectionObserver' in window) {
    var byId = {};
    links.forEach(function (a) { var id = a.getAttribute('href').slice(1); (byId[id] = byId[id] || []).push(a); });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          links.forEach(function (a) { a.classList.remove('is-active'); });
          (byId[en.target.id] || []).forEach(function (a) { a.classList.add('is-active'); });
        }
      });
    }, { rootMargin: '-10% 0px -75% 0px' });
    heads.forEach(function (h) { spy.observe(h); });
  }

  /* ---------- Copy link ---------- */
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var label = btn.querySelector('span');
      var url = btn.getAttribute('data-copy');
      var done = function () { if (label) { var old = label.textContent; label.textContent = 'Copied!'; setTimeout(function () { label.textContent = old; }, 1800); } };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(url).then(done, done);
      else { var ta = document.createElement('textarea'); ta.value = url; document.body.appendChild(ta); ta.select(); try { document.execCommand('copy'); } catch (e) {} ta.remove(); done(); }
    });
  });

  /* ---------- Lightbox ---------- */
  window.addEventListener('load', function () {
    if (window.GLightbox && document.querySelector('.glightbox')) GLightbox({ selector: '.glightbox', touchNavigation: true, loop: true });
  });
})();
