// macOS Menubar Clock
(function updateMenubarClock() {
  var el = document.getElementById('menubar-clock');
  if (!el) return;
  var now = new Date();
  var h = now.getHours().toString().padStart(2,'0');
  var m = now.getMinutes().toString().padStart(2,'0');
  el.textContent = h + ':' + m;
  setTimeout(updateMenubarClock, 15000);
})();
