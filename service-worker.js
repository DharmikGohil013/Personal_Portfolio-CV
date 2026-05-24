const CACHE_NAME = 'dharmik-portfolio-cache-v1';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './assets/css/main.css',
  './index.css',
  './assets/css/navigation.css',
  './assets/css/responsive-global.css',
  './assets/js/main.js',
  './assets/vendor/bootstrap/css/bootstrap.min.css',
  './assets/vendor/bootstrap/js/bootstrap.bundle.min.js',
  './assets/vendor/bootstrap-icons/bootstrap-icons.css',
  './assets/vendor/devicon/devicon.min.css'
];

// Install Event - Pre-cache critical static resources
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('[Service Worker] Pre-caching critical assets');
        return cache.addAll(ASSETS_TO_CACHE);
      })
      .then(() => self.skipWaiting())
  );
});

// Activate Event - Clean up old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheKeys => {
      return Promise.all(
        cacheKeys.map(cache => {
          if (cache !== CACHE_NAME) {
            console.log('[Service Worker] Removing old cache:', cache);
            return caches.delete(cache);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch Event - Handle assets caching strategy (Cache-First for Media/Fonts, Stale-While-Revalidate for CSS/JS/HTML)
self.addEventListener('fetch', event => {
  const requestUrl = new URL(event.request.url);
  
  // Cache check for identical origins or common font origins
  const isSameOrigin = requestUrl.origin === self.location.origin;
  const isCdn = requestUrl.hostname.includes('cdn.jsdelivr.net') || 
                requestUrl.hostname.includes('fonts.gstatic.com') || 
                requestUrl.hostname.includes('fonts.googleapis.com');
  
  if (!isSameOrigin && !isCdn) return;
  
  // Skip non-GET requests
  if (event.request.method !== 'GET') return;
  
  // Identify file types for Cache-First or Stale-While-Revalidate
  const urlPath = requestUrl.pathname.toLowerCase();
  const isImageOrFont = event.request.destination === 'image' || 
                        event.request.destination === 'font' || 
                        urlPath.endsWith('.woff2') || 
                        urlPath.endsWith('.woff') || 
                        urlPath.endsWith('.ttf') || 
                        urlPath.endsWith('.png') || 
                        urlPath.endsWith('.jpg') || 
                        urlPath.endsWith('.jpeg') || 
                        urlPath.endsWith('.webp') || 
                        urlPath.endsWith('.svg') || 
                        urlPath.endsWith('.ico');
  
  if (isImageOrFont) {
    // Cache-First strategy: Serve from cache if available, otherwise fetch and cache
    event.respondWith(
      caches.match(event.request).then(cachedResponse => {
        if (cachedResponse) {
          return cachedResponse;
        }
        return fetch(event.request).then(networkResponse => {
          if (!networkResponse || networkResponse.status !== 200) {
            return networkResponse;
          }
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then(cache => {
            cache.put(event.request, responseToCache);
          });
          return networkResponse;
        });
      })
    );
  } else {
    // Stale-While-Revalidate strategy for CSS, JS, HTML and other resources
    event.respondWith(
      caches.match(event.request).then(cachedResponse => {
        const fetchPromise = fetch(event.request).then(networkResponse => {
          if (networkResponse && networkResponse.status === 200) {
            const responseToCache = networkResponse.clone();
            caches.open(CACHE_NAME).then(cache => {
              cache.put(event.request, responseToCache);
            });
          }
          return networkResponse;
        }).catch(() => {
          // Silent catch for network connectivity offline scenarios
        });
        return cachedResponse || fetchPromise;
      })
    );
  }
});
