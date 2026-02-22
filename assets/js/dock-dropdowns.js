// Dock Dropdown Menus - Games & Apps
document.addEventListener('DOMContentLoaded', function () {
  const gamesTrigger = document.querySelector('.games-menu-trigger');
  const gamesDropdown = document.getElementById('gamesDropdown');
  const appsTrigger = document.querySelector('.apps-menu-trigger');
  const appsDropdown = document.getElementById('appsDropdown');

  if (gamesTrigger && gamesDropdown) {
    gamesTrigger.addEventListener('click', function (e) {
      e.stopPropagation();
      if (appsDropdown) appsDropdown.classList.remove('show');
      gamesDropdown.classList.toggle('show');
    });
    document.addEventListener('click', function (e) {
      if (!gamesTrigger.contains(e.target)) {
        gamesDropdown.classList.remove('show');
      }
    });
    gamesDropdown.addEventListener('click', function (e) {
      e.stopPropagation();
    });
  }

  if (appsTrigger && appsDropdown) {
    appsTrigger.addEventListener('click', function (e) {
      e.stopPropagation();
      if (gamesDropdown) gamesDropdown.classList.remove('show');
      appsDropdown.classList.toggle('show');
    });
    document.addEventListener('click', function (e) {
      if (!appsTrigger.contains(e.target)) {
        appsDropdown.classList.remove('show');
      }
    });
    appsDropdown.addEventListener('click', function (e) {
      e.stopPropagation();
    });
  }
});
