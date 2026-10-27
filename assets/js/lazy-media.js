// Portfolio previews only download and play when they enter the viewport.
(function () {
  function initPreviews() {
    var videos = document.querySelectorAll('video.lazy-preview-video');
    if (!videos.length) return;

    function start(video) {
      var source = video.querySelector('source[data-src]');
      if (source) {
        source.src = source.dataset.src;
        source.removeAttribute('data-src');
        video.load();
      }
      video.play().catch(function () {});
    }

    if (!('IntersectionObserver' in window)) {
      videos.forEach(start);
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) start(entry.target);
        else entry.target.pause();
      });
    }, { rootMargin: '200px 0px' });
    videos.forEach(function (video) { observer.observe(video); });
  }

  function initTechnologyIcons() {
    var showcase = document.querySelector('.logoloop__track');
    if (!showcase) return;
    function loadIcons() {
      if (document.getElementById('devicon-stylesheet')) return;
      var stylesheet = document.createElement('link');
      stylesheet.id = 'devicon-stylesheet';
      stylesheet.rel = 'stylesheet';
      stylesheet.href = 'assets/vendor/devicon/devicon.min.css';
      document.head.appendChild(stylesheet);
    }
    if (!('IntersectionObserver' in window)) {
      loadIcons();
      return;
    }
    var observer = new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting) {
        loadIcons();
        observer.disconnect();
      }
    }, { rootMargin: '400px 0px' });
    observer.observe(showcase);
  }

  function init() {
    initPreviews();
    initTechnologyIcons();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
