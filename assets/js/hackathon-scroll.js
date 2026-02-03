/**
 * Hackathon Section - Infinite Scroll Effect
 */
(function() {
  "use strict";

  window.addEventListener('load', function() {
    const scrollContainer = document.querySelector('.hackathon-scroll-container');
    
    if (scrollContainer) {
      // Clone all cards to create infinite scroll effect
      const cards = scrollContainer.querySelectorAll('.hackathon-card');
      
      // Clone each card and append to container for seamless looping
      cards.forEach(card => {
        const clone = card.cloneNode(true);
        scrollContainer.appendChild(clone);
      });
      
      // Optional: Pause animation on hover for better UX
      scrollContainer.addEventListener('mouseenter', function() {
        this.style.animationPlayState = 'paused';
      });
      
      scrollContainer.addEventListener('mouseleave', function() {
        this.style.animationPlayState = 'running';
      });
    }
  });

})();
