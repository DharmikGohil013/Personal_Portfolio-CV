import json

with open('languages.json', 'r', encoding='utf-8') as f:
    langs = json.load(f)

langs_js = json.dumps(langs, ensure_ascii=False)

js_content = f'''/**
 * Global Multilingual & Geo SEO Engine
 * Provides instant real-time translation for 200+ world languages
 * Powered by Google Translate API & International Geo Routing
 * Website: https://dharmikgohil.art
 */

(function () {{
  'use strict';

  var ALL_LANGUAGES = {langs_js};

  var TOP_LANG_CODES = ['en', 'es', 'fr', 'de', 'ja', 'zh-CN', 'hi', 'gu', 'ar', 'pt', 'ru', 'it', 'ko', 'nl', 'tr', 'vi', 'id', 'pl', 'sv', 'uk'];

  // Initialize Google Translate Element Callback
  window.googleTranslateElementInit = function () {{
    if (window.google && window.google.translate) {{
      new window.google.translate.TranslateElement({{
        pageLanguage: 'en',
        autoDisplay: false,
        layout: window.google.translate.TranslateElement.InlineLayout.SIMPLE
      }}, 'google_translate_element');
    }}
    checkAndApplyInitialLanguage();
  }};

  // Load Google Translate script asynchronously
  function loadGoogleTranslateScript() {{
    if (document.getElementById('google-translate-script')) return;
    var div = document.createElement('div');
    div.id = 'google_translate_element';
    div.style.display = 'none';
    document.body.appendChild(div);

    var script = document.createElement('script');
    script.id = 'google-translate-script';
    script.src = '//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
    script.async = true;
    document.head.appendChild(script);
  }}

  // Set Google Translate Cookie and trigger translation
  function setLanguage(langCode) {{
    if (!langCode) return;
    var gtCode = langCode;
    if (gtCode === 'en' || gtCode === 'en-US' || gtCode === 'en-GB' || gtCode === 'en-CA' || gtCode === 'en-AU' || gtCode === 'en-IN') {{
      gtCode = 'en';
    }}

    localStorage.setItem('portfolio_target_lang', langCode);

    try {{
      var url = new URL(window.location.href);
      if (langCode === 'en') {{
        url.searchParams.delete('lang');
      }} else {{
        url.searchParams.set('lang', langCode);
      }}
      window.history.replaceState({{}}, '', url.toString());
    }} catch (e) {{}}

    var hostname = window.location.hostname;
    var cookieVal = (langCode === 'en') ? '' : '/en/' + gtCode;
    
    if (langCode === 'en') {{
      document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
      document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=' + hostname + ';';
    }} else {{
      document.cookie = 'googtrans=' + cookieVal + '; path=/;';
      document.cookie = 'googtrans=' + cookieVal + '; path=/; domain=' + hostname + ';';
    }}

    var select = document.querySelector('.goog-te-combo');
    if (select) {{
      select.value = gtCode;
      select.dispatchEvent(new Event('change'));
    }} else {{
      var attempts = 0;
      var interval = setInterval(function() {{
        attempts++;
        var sel = document.querySelector('.goog-te-combo');
        if (sel) {{
          clearInterval(interval);
          sel.value = gtCode;
          sel.dispatchEvent(new Event('change'));
        }} else if (attempts > 5) {{
          clearInterval(interval);
          location.reload();
        }}
      }}, 150);
    }}

    updateActiveButtonDisplay(langCode);
    closeLanguageModal();
  }}

  function updateActiveButtonDisplay(langCode) {{
    var found = ALL_LANGUAGES.find(function(l) {{ return l.code === langCode; }});
    var currentBadge = document.getElementById('currentLangBadge');
    if (currentBadge && found) {{
      currentBadge.textContent = found.code.toUpperCase();
    }}
  }}

  function checkAndApplyInitialLanguage() {{
    var urlParams = new URLSearchParams(window.location.search);
    var langParam = urlParams.get('lang');
    var savedLang = localStorage.getItem('portfolio_target_lang');
    var target = langParam || savedLang;

    if (target && target !== 'en') {{
      var checkCombo = setInterval(function() {{
        var select = document.querySelector('.goog-te-combo');
        if (select) {{
          clearInterval(checkCombo);
          select.value = target;
          select.dispatchEvent(new Event('change'));
          updateActiveButtonDisplay(target);
        }}
      }}, 200);

      setTimeout(function() {{
        clearInterval(checkCombo);
      }}, 4000);
    }}
  }}

  function initLanguageUI() {{
    if (!document.getElementById('globalLangFloatingBtn')) {{
      var floatBtn = document.createElement('button');
      floatBtn.id = 'globalLangFloatingBtn';
      floatBtn.className = 'global-lang-floating-btn';
      floatBtn.setAttribute('aria-label', 'Change Language (200+ Available)');
      floatBtn.setAttribute('title', 'Select from 200+ World Languages');
      floatBtn.innerHTML = '<span class="lang-btn-globe">🌐</span> <span id="currentLangBadge">EN</span> <span class="lang-btn-badge">200+</span>';
      floatBtn.onclick = openLanguageModal;
      document.body.appendChild(floatBtn);
    }}

    document.querySelectorAll('.masthead-lang-trigger').forEach(function(el) {{
      el.onclick = openLanguageModal;
    }});

    if (!document.getElementById('globalLangModalOverlay')) {{
      var modalOverlay = document.createElement('div');
      modalOverlay.id = 'globalLangModalOverlay';
      modalOverlay.className = 'global-lang-modal-overlay';
      modalOverlay.onclick = function(e) {{
        if (e.target === modalOverlay) closeLanguageModal();
      }};

      var quickPillsHtml = TOP_LANG_CODES.map(function(code) {{
        var found = ALL_LANGUAGES.find(function(l) {{ return l.code === code; }});
        if (!found) return '';
        return '<button type="button" class="quick-lang-tag" data-code="' + found.code + '">' + found.flag + ' ' + found.name + '</button>';
      }}).join('');

      var langItemsHtml = ALL_LANGUAGES.map(function(lang) {{
        return '<div class="global-lang-item" data-code="' + lang.code + '" data-name="' + lang.name.toLowerCase() + '" data-native="' + lang.native.toLowerCase() + '">' +
          '<div class="global-lang-item-left">' +
            '<span class="global-lang-flag">' + lang.flag + '</span>' +
            '<div>' +
              '<div class="global-lang-name">' + lang.name + '</div>' +
              '<small class="global-lang-native">' + lang.native + '</small>' +
            '</div>' +
          '</div>' +
          '<span class="global-lang-code">' + lang.code + '</span>' +
        '</div>';
      }}).join('');

      modalOverlay.innerHTML = 
        '<div class="global-lang-modal" role="dialog" aria-modal="true" aria-labelledby="globalLangTitle">' +
          '<div class="global-lang-modal-header">' +
            '<h3 class="global-lang-modal-title" id="globalLangTitle">' +
              '<span>🌐 Select Language</span>' +
              '<span class="badge-200">' + ALL_LANGUAGES.length + ' Languages</span>' +
            '</h3>' +
            '<button type="button" class="global-lang-close-btn" id="globalLangCloseBtn" aria-label="Close">&times;</button>' +
          '</div>' +
          '<div class="global-lang-search-wrapper">' +
            '<input type="text" class="global-lang-search-input" id="globalLangSearchInput" placeholder="Search language by name, script, or country code (e.g., Spanish, 日本語, Hindi, ar)..." autocomplete="off">' +
          '</div>' +
          '<div class="global-lang-quick-bar">' +
            '<span style="color:#777;font-size:11px;font-family:IBM Plex Mono, monospace;">POPULAR:</span>' +
            quickPillsHtml +
          '</div>' +
          '<div class="global-lang-grid" id="globalLangGrid">' +
            langItemsHtml +
          '</div>' +
          '<div class="global-lang-modal-footer">' +
            '<span>🌍 Serving Clients Across 100+ Countries Globally</span>' +
            '<button type="button" class="global-lang-reset-btn" id="globalLangResetBtn">Reset to English (Default)</button>' +
          '</div>' +
        '</div>';

      document.body.appendChild(modalOverlay);

      document.getElementById('globalLangCloseBtn').onclick = closeLanguageModal;
      document.getElementById('globalLangResetBtn').onclick = function() {{
        setLanguage('en');
      }};

      var searchInput = document.getElementById('globalLangSearchInput');
      searchInput.oninput = function() {{
        var q = this.value.trim().toLowerCase();
        var items = document.querySelectorAll('.global-lang-item');
        items.forEach(function(item) {{
          var code = item.getAttribute('data-code').toLowerCase();
          var name = item.getAttribute('data-name');
          var native = item.getAttribute('data-native');
          if (!q || code.indexOf(q) !== -1 || name.indexOf(q) !== -1 || native.indexOf(q) !== -1) {{
            item.style.display = 'flex';
          }} else {{
            item.style.display = 'none';
          }}
        }});
      }};

      document.getElementById('globalLangGrid').onclick = function(e) {{
        var target = e.target.closest('.global-lang-item');
        if (target) {{
          var code = target.getAttribute('data-code');
          setLanguage(code);
        }}
      }};

      modalOverlay.querySelector('.global-lang-quick-bar').onclick = function(e) {{
        var target = e.target.closest('.quick-lang-tag');
        if (target) {{
          var code = target.getAttribute('data-code');
          setLanguage(code);
        }}
      }};
    }}
  }}

  function openLanguageModal() {{
    var overlay = document.getElementById('globalLangModalOverlay');
    if (overlay) {{
      overlay.classList.add('active');
      var searchInput = document.getElementById('globalLangSearchInput');
      if (searchInput) {{
        searchInput.value = '';
        searchInput.focus();
        document.querySelectorAll('.global-lang-item').forEach(function(i) {{ i.style.display = 'flex'; }});
      }}
    }}
  }}

  function closeLanguageModal() {{
    var overlay = document.getElementById('globalLangModalOverlay');
    if (overlay) overlay.classList.remove('active');
  }}

  document.addEventListener('keydown', function(e) {{
    if (e.key === 'Escape') closeLanguageModal();
  }});

  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', function() {{
      loadGoogleTranslateScript();
      initLanguageUI();
    }});
  }} else {{
    loadGoogleTranslateScript();
    initLanguageUI();
  }}

}})();
'''

with open('assets/js/global-multilingual.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print('Generated assets/js/global-multilingual.js successfully!')
