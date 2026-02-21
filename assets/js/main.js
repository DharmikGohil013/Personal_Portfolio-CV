/**
* Template Name: Kelly
* Template URL: https://bootstrapmade.com/kelly-free-bootstrap-cv-resume-html-template/
* Updated: Aug 07 2024 with Bootstrap v5.3.3
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function() {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');
  const mobileNavOverlay = document.querySelector('.mobile-nav-overlay');
  const navMenu = document.querySelector('.navmenu');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    if (mobileNavToggleBtn) {
      mobileNavToggleBtn.classList.toggle('active');
    }
    if (mobileNavOverlay) {
      mobileNavOverlay.classList.toggle('active');
    }
  }
  
  if (mobileNavToggleBtn) {
    mobileNavToggleBtn.addEventListener('click', mobileNavToogle);
  }

  // Close menu when clicking overlay or outside menu area
  document.addEventListener('click', function(event) {
    const isMenuActive = document.querySelector('body').classList.contains('mobile-nav-active');
    const isClickInsideMenu = navMenu && navMenu.contains(event.target);
    const isClickOnToggle = mobileNavToggleBtn && mobileNavToggleBtn.contains(event.target);
    
    if (isMenuActive && !isClickInsideMenu && !isClickOnToggle) {
      mobileNavToogle();
    }
  });

  // Close menu when clicking overlay
  if (mobileNavOverlay) {
    mobileNavOverlay.addEventListener('click', function() {
      if (document.querySelector('body').classList.contains('mobile-nav-active')) {
        mobileNavToogle();
      }
    });
  }

  // Close menu when clicking a link (except dropdowns)
  if (navMenu) {
    navMenu.querySelectorAll('a:not(.toggle-dropdown)').forEach(link => {
      link.addEventListener('click', function() {
        if (document.querySelector('body').classList.contains('mobile-nav-active')) {
          mobileNavToogle();
        }
      });
    });
  }

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });

  /**
   * Toggle mobile nav dropdowns
   */
  const toggleDropdowns = document.querySelectorAll('.navmenu .toggle-dropdown');
  console.log('Found', toggleDropdowns.length, 'dropdown toggles');
  
  toggleDropdowns.forEach(toggleBtn => {
    toggleBtn.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      
      console.log('Dropdown clicked');
      
      // Get the parent dropdown li element
      const dropdownLi = this.closest('.dropdown');
      
      if (dropdownLi) {
        console.log('Toggling dropdown:', dropdownLi);
        
        // Close other dropdowns at the same level
        const parentUl = dropdownLi.parentElement;
        const siblings = parentUl.querySelectorAll(':scope > .dropdown.active');
        siblings.forEach(sibling => {
          if (sibling !== dropdownLi) {
            sibling.classList.remove('active');
          }
        });
        
        // Toggle current dropdown
        dropdownLi.classList.toggle('active');
        console.log('Dropdown is now:', dropdownLi.classList.contains('active') ? 'OPEN' : 'CLOSED');
      }
    });
  });

  /**
   * Preloader
   * Note: When cinematic intro is active, preloader is handled by the intro script
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      // If cinematic intro exists, let it handle preloader removal
      if (document.getElementById('cinematic-intro')) return;
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  /**
   * Animate the skills items on reveal
   */
  let skillsAnimation = document.querySelectorAll('.skills-animation');
  skillsAnimation.forEach((item) => {
    new Waypoint({
      element: item,
      offset: '80%',
      handler: function(direction) {
        let progress = item.querySelectorAll('.progress .progress-bar');
        progress.forEach(el => {
          el.style.width = el.getAttribute('aria-valuenow') + '%';
        });
      }
    });
  });

  /**
   * Initiate Pure Counter
   */
  new PureCounter();

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);

  /**
   * Initiate glightbox
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Init isotope layout and filters
   */
  document.querySelectorAll('.isotope-layout').forEach(function(isotopeItem) {
    let layout = isotopeItem.getAttribute('data-layout') ?? 'masonry';
    let filter = isotopeItem.getAttribute('data-default-filter') ?? '*';
    let sort = isotopeItem.getAttribute('data-sort') ?? 'original-order';

    let initIsotope;
    imagesLoaded(isotopeItem.querySelector('.isotope-container'), function() {
      initIsotope = new Isotope(isotopeItem.querySelector('.isotope-container'), {
        itemSelector: '.isotope-item',
        layoutMode: layout,
        filter: filter,
        sortBy: sort
      });
    });

    isotopeItem.querySelectorAll('.isotope-filters li').forEach(function(filters) {
      filters.addEventListener('click', function() {
        isotopeItem.querySelector('.isotope-filters .filter-active').classList.remove('filter-active');
        this.classList.add('filter-active');
        initIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        if (typeof aosInit === 'function') {
          aosInit();
        }
      }, false);
    });

  });

})();