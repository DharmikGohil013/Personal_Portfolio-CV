// Let the page paint before requesting the optional auto ads runtime.
(function () {
  var loaded = false;
  function loadAds() {
    if (loaded) return;
    loaded = true;
    window.removeEventListener('scroll', loadAds);
    window.removeEventListener('pointerdown', loadAds);
    var script = document.createElement('script');
    script.async = true;
    script.crossOrigin = 'anonymous';
    script.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4658801537271443';
    document.head.appendChild(script);
  }
  window.addEventListener('scroll', loadAds, { once: true, passive: true });
  window.addEventListener('pointerdown', loadAds, { once: true, passive: true });
  setTimeout(loadAds, 20000);
})();
