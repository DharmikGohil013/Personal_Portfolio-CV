/**
 * Global Multilingual & Geo SEO Engine
 * Provides instant real-time translation for 200+ world languages
 * Powered by Google Translate API & International Geo Routing
 * Website: https://dharmikgohil.art
 */

(function () {
  'use strict';

  var ALL_LANGUAGES = [{"code": "en", "name": "English", "native": "English", "flag": "🇺🇸"}, {"code": "en-US", "name": "English (US)", "native": "English (US)", "flag": "🇺🇸"}, {"code": "en-GB", "name": "English (UK)", "native": "English (UK)", "flag": "🇬🇧"}, {"code": "en-CA", "name": "English (Canada)", "native": "English (Canada)", "flag": "🇨🇦"}, {"code": "en-AU", "name": "English (Australia)", "native": "English (Australia)", "flag": "🇦🇺"}, {"code": "en-IN", "name": "English (India)", "native": "English (India)", "flag": "🇮🇳"}, {"code": "en-NZ", "name": "English (New Zealand)", "native": "English (New Zealand)", "flag": "🇳🇿"}, {"code": "en-IE", "name": "English (Ireland)", "native": "English (Ireland)", "flag": "🇮🇪"}, {"code": "en-SG", "name": "English (Singapore)", "native": "English (Singapore)", "flag": "🇸🇬"}, {"code": "en-ZA", "name": "English (South Africa)", "native": "English (South Africa)", "flag": "🇿🇦"}, {"code": "en-AE", "name": "English (UAE)", "native": "English (UAE)", "flag": "🇦🇪"}, {"code": "es", "name": "Spanish", "native": "Español", "flag": "🇪🇸"}, {"code": "es-ES", "name": "Spanish (Spain)", "native": "Español (España)", "flag": "🇪🇸"}, {"code": "es-MX", "name": "Spanish (Mexico)", "native": "Español (México)", "flag": "🇲🇽"}, {"code": "es-AR", "name": "Spanish (Argentina)", "native": "Español (Argentina)", "flag": "🇦🇷"}, {"code": "es-CO", "name": "Spanish (Colombia)", "native": "Español (Colombia)", "flag": "🇨🇴"}, {"code": "es-CL", "name": "Spanish (Chile)", "native": "Español (Chile)", "flag": "🇨🇱"}, {"code": "es-PE", "name": "Spanish (Peru)", "native": "Español (Perú)", "flag": "🇵🇪"}, {"code": "es-VE", "name": "Spanish (Venezuela)", "native": "Español (Venezuela)", "flag": "🇻🇪"}, {"code": "fr", "name": "French", "native": "Français", "flag": "🇫🇷"}, {"code": "fr-FR", "name": "French (France)", "native": "Français (France)", "flag": "🇫🇷"}, {"code": "fr-CA", "name": "French (Canada)", "native": "Français (Canada)", "flag": "🇨🇦"}, {"code": "fr-BE", "name": "French (Belgium)", "native": "Français (Belgique)", "flag": "🇧🇪"}, {"code": "fr-CH", "name": "French (Switzerland)", "native": "Français (Suisse)", "flag": "🇨🇭"}, {"code": "de", "name": "German", "native": "Deutsch", "flag": "🇩🇪"}, {"code": "de-DE", "name": "German (Germany)", "native": "Deutsch (Deutschland)", "flag": "🇩🇪"}, {"code": "de-AT", "name": "German (Austria)", "native": "Deutsch (Österreich)", "flag": "🇦🇹"}, {"code": "de-CH", "name": "German (Switzerland)", "native": "Deutsch (Schweiz)", "flag": "🇨🇭"}, {"code": "it", "name": "Italian", "native": "Italiano", "flag": "🇮🇹"}, {"code": "it-IT", "name": "Italian (Italy)", "native": "Italiano (Italia)", "flag": "🇮🇹"}, {"code": "it-CH", "name": "Italian (Switzerland)", "native": "Italiano (Svizzera)", "flag": "🇨🇭"}, {"code": "pt", "name": "Portuguese", "native": "Português", "flag": "🇵🇹"}, {"code": "pt-BR", "name": "Portuguese (Brazil)", "native": "Português (Brasil)", "flag": "🇧🇷"}, {"code": "pt-PT", "name": "Portuguese (Portugal)", "native": "Português (Portugal)", "flag": "🇵🇹"}, {"code": "ru", "name": "Russian", "native": "Русский", "flag": "🇷🇺"}, {"code": "ru-RU", "name": "Russian (Russia)", "native": "Русский (Россия)", "flag": "🇷🇺"}, {"code": "ja", "name": "Japanese", "native": "日本語", "flag": "🇯🇵"}, {"code": "ja-JP", "name": "Japanese (Japan)", "native": "日本語 (日本)", "flag": "🇯🇵"}, {"code": "zh", "name": "Chinese", "native": "中文", "flag": "🇨🇳"}, {"code": "zh-CN", "name": "Chinese (Simplified)", "native": "简体中文", "flag": "🇨🇳"}, {"code": "zh-TW", "name": "Chinese (Traditional)", "native": "繁體中文", "flag": "🇹🇼"}, {"code": "zh-HK", "name": "Chinese (Hong Kong)", "native": "香港繁體", "flag": "🇭🇰"}, {"code": "zh-SG", "name": "Chinese (Singapore)", "native": "简体中文 (新加坡)", "flag": "🇸🇬"}, {"code": "zh-Hans", "name": "Chinese (Simplified script)", "native": "简体中文", "flag": "🇨🇳"}, {"code": "zh-Hant", "name": "Chinese (Traditional script)", "native": "繁體中文", "flag": "🇹🇼"}, {"code": "ko", "name": "Korean", "native": "한국어", "flag": "🇰🇷"}, {"code": "ko-KR", "name": "Korean (South Korea)", "native": "한국어 (대한민국)", "flag": "🇰🇷"}, {"code": "ar", "name": "Arabic", "native": "العربية", "flag": "🇸🇦"}, {"code": "ar-SA", "name": "Arabic (Saudi Arabia)", "native": "العربية (السعودية)", "flag": "🇸🇦"}, {"code": "ar-AE", "name": "Arabic (UAE)", "native": "العربية (الإمارات)", "flag": "🇦🇪"}, {"code": "ar-EG", "name": "Arabic (Egypt)", "native": "العربية (مصر)", "flag": "🇪🇬"}, {"code": "ar-QA", "name": "Arabic (Qatar)", "native": "العربية (قطر)", "flag": "🇶🇦"}, {"code": "ar-KW", "name": "Arabic (Kuwait)", "native": "العربية (الكويت)", "flag": "🇰🇼"}, {"code": "hi", "name": "Hindi", "native": "हिन्दी", "flag": "🇮🇳"}, {"code": "hi-IN", "name": "Hindi (India)", "native": "हिन्दी (भारत)", "flag": "🇮🇳"}, {"code": "gu", "name": "Gujarati", "native": "ગુજરાતી", "flag": "🇮🇳"}, {"code": "gu-IN", "name": "Gujarati (India)", "native": "ગુજરાતી (ભારત)", "flag": "🇮🇳"}, {"code": "bn", "name": "Bengali", "native": "বাংলা", "flag": "🇧🇩"}, {"code": "bn-BD", "name": "Bengali (Bangladesh)", "native": "বাংলা (বাংলাদেশ)", "flag": "🇧🇩"}, {"code": "bn-IN", "name": "Bengali (India)", "native": "বাংলা (ভারত)", "flag": "🇮🇳"}, {"code": "pa", "name": "Punjabi", "native": "ਪੰਜਾਬੀ", "flag": "🇮🇳"}, {"code": "pa-IN", "name": "Punjabi (India)", "native": "ਪੰਜਾਬੀ (ਭਾਰਤ)", "flag": "🇮🇳"}, {"code": "pa-PK", "name": "Punjabi (Pakistan)", "native": "پنجابی (پاکستان)", "flag": "🇵🇰"}, {"code": "mr", "name": "Marathi", "native": "मराठी", "flag": "🇮🇳"}, {"code": "mr-IN", "name": "Marathi (India)", "native": "मराठी (भारत)", "flag": "🇮🇳"}, {"code": "te", "name": "Telugu", "native": "తెలుగు", "flag": "🇮🇳"}, {"code": "te-IN", "name": "Telugu (India)", "native": "తెలుగు (భారતదేశం)", "flag": "🇮🇳"}, {"code": "ta", "name": "Tamil", "native": "தமிழ்", "flag": "🇮🇳"}, {"code": "ta-IN", "name": "Tamil (India)", "native": "தமிழ் (இந்தியா)", "flag": "🇮🇳"}, {"code": "ta-LK", "name": "Tamil (Sri Lanka)", "native": "தமிழ் (இலங்கை)", "flag": "🇱🇰"}, {"code": "ta-SG", "name": "Tamil (Singapore)", "native": "தமிழ் (சிங்கப்பூர்)", "flag": "🇸🇬"}, {"code": "ur", "name": "Urdu", "native": "اردو", "flag": "🇵🇰"}, {"code": "ur-PK", "name": "Urdu (Pakistan)", "native": "اردو (پاکستان)", "flag": "🇵🇰"}, {"code": "ur-IN", "name": "Urdu (India)", "native": "اردو (بھارت)", "flag": "🇮🇳"}, {"code": "kn", "name": "Kannada", "native": "ಕನ್ನಡ", "flag": "🇮🇳"}, {"code": "kn-IN", "name": "Kannada (India)", "native": "ಕನ್ನಡ (ಭಾರತ)", "flag": "🇮🇳"}, {"code": "ml", "name": "Malayalam", "native": "മലയാളം", "flag": "🇮🇳"}, {"code": "ml-IN", "name": "Malayalam (India)", "native": "മലയാളം (ഇന്ത്യ)", "flag": "🇮🇳"}, {"code": "or", "name": "Odia", "native": "ଓଡ଼ିଆ", "flag": "🇮🇳"}, {"code": "as", "name": "Assamese", "native": "অসমীয়া", "flag": "🇮🇳"}, {"code": "ne", "name": "Nepali", "native": "नेपाली", "flag": "🇳🇵"}, {"code": "ne-NP", "name": "Nepali (Nepal)", "native": "नेपाली (नेपाल)", "flag": "🇳🇵"}, {"code": "si", "name": "Sinhala", "native": "සිංහල", "flag": "🇱🇰"}, {"code": "si-LK", "name": "Sinhala (Sri Lanka)", "native": "සිංහල (ශ්‍රී ලංකා)", "flag": "🇱🇰"}, {"code": "tr", "name": "Turkish", "native": "Türkçe", "flag": "🇹🇷"}, {"code": "tr-TR", "name": "Turkish (Turkey)", "native": "Türkçe (Türkiye)", "flag": "🇹🇷"}, {"code": "vi", "name": "Vietnamese", "native": "Tiếng Việt", "flag": "🇻🇳"}, {"code": "vi-VN", "name": "Vietnamese (Vietnam)", "native": "Tiếng Việt (Việt Nam)", "flag": "🇻🇳"}, {"code": "th", "name": "Thai", "native": "ไทย", "flag": "🇹🇭"}, {"code": "th-TH", "name": "Thai (Thailand)", "native": "ไทย (ประเทศไทย)", "flag": "🇹🇭"}, {"code": "id", "name": "Indonesian", "native": "Bahasa Indonesia", "flag": "🇮🇩"}, {"code": "id-ID", "name": "Indonesian (Indonesia)", "native": "Bahasa Indonesia", "flag": "🇮🇩"}, {"code": "ms", "name": "Malay", "native": "Bahasa Melayu", "flag": "🇲🇾"}, {"code": "ms-MY", "name": "Malay (Malaysia)", "native": "Bahasa Melayu (Malaysia)", "flag": "🇲🇾"}, {"code": "tl", "name": "Tagalog", "native": "Tagalog", "flag": "🇵🇭"}, {"code": "fil", "name": "Filipino", "native": "Filipino", "flag": "🇵🇭"}, {"code": "my", "name": "Burmese", "native": "မြန်မာစာ", "flag": "🇲🇲"}, {"code": "km", "name": "Khmer", "native": "ខ្មែរ", "flag": "🇰🇭"}, {"code": "lo", "name": "Lao", "native": "ລາວ", "flag": "🇱🇦"}, {"code": "jv", "name": "Javanese", "native": "Basa Jawa", "flag": "🇮🇩"}, {"code": "su", "name": "Sundanese", "native": "Basa Sunda", "flag": "🇮🇩"}, {"code": "nl", "name": "Dutch", "native": "Nederlands", "flag": "🇳🇱"}, {"code": "nl-NL", "name": "Dutch (Netherlands)", "native": "Nederlands (Nederland)", "flag": "🇳🇱"}, {"code": "nl-BE", "name": "Dutch (Belgium)", "native": "Nederlands (België)", "flag": "🇧🇪"}, {"code": "pl", "name": "Polish", "native": "Polski", "flag": "🇵🇱"}, {"code": "pl-PL", "name": "Polish (Poland)", "native": "Polski (Polska)", "flag": "🇵🇱"}, {"code": "uk", "name": "Ukrainian", "native": "Українська", "flag": "🇺🇦"}, {"code": "uk-UA", "name": "Ukrainian (Ukraine)", "native": "Українська (Україна)", "flag": "🇺🇦"}, {"code": "fa", "name": "Persian", "native": "فارسی", "flag": "🇮🇷"}, {"code": "fa-IR", "name": "Persian (Iran)", "native": "فارسی (ایران)", "flag": "🇮🇷"}, {"code": "he", "name": "Hebrew", "native": "עברית", "flag": "🇮🇱"}, {"code": "he-IL", "name": "Hebrew (Israel)", "native": "עברית (ישראל)", "flag": "🇮🇱"}, {"code": "el", "name": "Greek", "native": "Ελληνικά", "flag": "🇬🇷"}, {"code": "el-GR", "name": "Greek (Greece)", "native": "Ελληνικά (Ελλάδα)", "flag": "🇬🇷"}, {"code": "sv", "name": "Swedish", "native": "Svenska", "flag": "🇸🇪"}, {"code": "sv-SE", "name": "Swedish (Sweden)", "native": "Svenska (Sverige)", "flag": "🇸🇪"}, {"code": "no", "name": "Norwegian", "native": "Norsk", "flag": "🇳🇴"}, {"code": "nb", "name": "Norwegian Bokmål", "native": "Norsk Bokmål", "flag": "🇳🇴"}, {"code": "nn", "name": "Norwegian Nynorsk", "native": "Norsk Nynorsk", "flag": "🇳🇴"}, {"code": "da", "name": "Danish", "native": "Dansk", "flag": "🇩🇰"}, {"code": "da-DK", "name": "Danish (Denmark)", "native": "Dansk (Danmark)", "flag": "🇩🇰"}, {"code": "fi", "name": "Finnish", "native": "Suomi", "flag": "🇫🇮"}, {"code": "fi-FI", "name": "Finnish (Finland)", "native": "Suomi (Suomi)", "flag": "🇫🇮"}, {"code": "cs", "name": "Czech", "native": "Čeština", "flag": "🇨🇿"}, {"code": "cs-CZ", "name": "Czech (Czechia)", "native": "Čeština (Česko)", "flag": "🇨🇿"}, {"code": "ro", "name": "Romanian", "native": "Română", "flag": "🇷🇴"}, {"code": "ro-RO", "name": "Romanian (Romania)", "native": "Română (România)", "flag": "🇷🇴"}, {"code": "hu", "name": "Hungarian", "native": "Magyar", "flag": "🇭🇺"}, {"code": "hu-HU", "name": "Hungarian (Hungary)", "native": "Magyar (Magyarország)", "flag": "🇭🇺"}, {"code": "sk", "name": "Slovak", "native": "Slovenčina", "flag": "🇸🇰"}, {"code": "sk-SK", "name": "Slovak (Slovakia)", "native": "Slovenčina (Slovensko)", "flag": "🇸🇰"}, {"code": "bg", "name": "Bulgarian", "native": "Български", "flag": "🇧🇬"}, {"code": "bg-BG", "name": "Bulgarian (Bulgaria)", "native": "Български (България)", "flag": "🇧🇬"}, {"code": "sr", "name": "Serbian", "native": "Српски", "flag": "🇷🇸"}, {"code": "sr-RS", "name": "Serbian (Serbia)", "native": "Српски (Србија)", "flag": "🇷🇸"}, {"code": "hr", "name": "Croatian", "native": "Hrvatski", "flag": "🇭🇷"}, {"code": "hr-HR", "name": "Croatian (Croatia)", "native": "Hrvatski (Hrvatska)", "flag": "🇭🇷"}, {"code": "lt", "name": "Lithuanian", "native": "Lietuvių", "flag": "🇱🇹"}, {"code": "lt-LT", "name": "Lithuanian (Lithuania)", "native": "Lietuvių (Lietuva)", "flag": "🇱🇹"}, {"code": "lv", "name": "Latvian", "native": "Latviešu", "flag": "🇱🇻"}, {"code": "lv-LV", "name": "Latvian (Latvia)", "native": "Latviešu (Latvija)", "flag": "🇱🇻"}, {"code": "et", "name": "Estonian", "native": "Eesti", "flag": "🇪🇪"}, {"code": "et-EE", "name": "Estonian (Estonia)", "native": "Eesti (Eesti)", "flag": "🇪🇪"}, {"code": "sl", "name": "Slovenian", "native": "Slovenščina", "flag": "🇸🇮"}, {"code": "sl-SI", "name": "Slovenian (Slovenia)", "native": "Slovenščina (Slovenija)", "flag": "🇸🇮"}, {"code": "ga", "name": "Irish", "native": "Gaeilge", "flag": "🇮🇪"}, {"code": "ga-IE", "name": "Irish (Ireland)", "native": "Gaeilge (Éire)", "flag": "🇮🇪"}, {"code": "cy", "name": "Welsh", "native": "Cymraeg", "flag": "🇬🇧"}, {"code": "cy-GB", "name": "Welsh (UK)", "native": "Cymraeg (DU)", "flag": "🇬🇧"}, {"code": "is", "name": "Icelandic", "native": "Íslenska", "flag": "🇮🇸"}, {"code": "is-IS", "name": "Icelandic (Iceland)", "native": "Íslenska (Ísland)", "flag": "🇮🇸"}, {"code": "mt", "name": "Maltese", "native": "Malti", "flag": "🇲🇹"}, {"code": "sq", "name": "Albanian", "native": "Shqip", "flag": "🇦🇱"}, {"code": "mk", "name": "Macedonian", "native": "Македонски", "flag": "🇲🇰"}, {"code": "bs", "name": "Bosnian", "native": "Bosanski", "flag": "🇧🇦"}, {"code": "az", "name": "Azerbaijani", "native": "Azərbaycan", "flag": "🇦🇿"}, {"code": "ka", "name": "Georgian", "native": "ქართული", "flag": "🇬🇪"}, {"code": "hy", "name": "Armenian", "native": "Հայերեն", "flag": "🇦🇲"}, {"code": "kk", "name": "Kazakh", "native": "Қазақша", "flag": "🇰🇿"}, {"code": "uz", "name": "Uzbek", "native": "Oʻzbekcha", "flag": "🇺🇿"}, {"code": "mn", "name": "Mongolian", "native": "Монгол", "flag": "🇲🇳"}, {"code": "sw", "name": "Swahili", "native": "Kiswahili", "flag": "🇰🇪"}, {"code": "sw-KE", "name": "Swahili (Kenya)", "native": "Kiswahili (Kenya)", "flag": "🇰🇪"}, {"code": "sw-TZ", "name": "Swahili (Tanzania)", "native": "Kiswahili (Tanzania)", "flag": "🇹🇿"}, {"code": "af", "name": "Afrikaans", "native": "Afrikaans", "flag": "🇿🇦"}, {"code": "am", "name": "Amharic", "native": "አማርኛ", "flag": "🇪🇹"}, {"code": "ha", "name": "Hausa", "native": "Hausa", "flag": "🇳🇬"}, {"code": "yo", "name": "Yoruba", "native": "Yorùbá", "flag": "🇳🇬"}, {"code": "ig", "name": "Igbo", "native": "Asụsụ Igbo", "flag": "🇳🇬"}, {"code": "zu", "name": "Zulu", "native": "isiZulu", "flag": "🇿🇦"}, {"code": "xh", "name": "Xhosa", "native": "isiXhosa", "flag": "🇿🇦"}, {"code": "so", "name": "Somali", "native": "Soomaali", "flag": "🇸🇴"}, {"code": "rw", "name": "Kinyarwanda", "native": "Kinyarwanda", "flag": "🇷🇼"}, {"code": "mg", "name": "Malagasy", "native": "Malagasy", "flag": "🇲🇬"}, {"code": "sn", "name": "Shona", "native": "chiShona", "flag": "🇿🇼"}, {"code": "ny", "name": "Chichewa", "native": "Chichewa", "flag": "🇲🇼"}, {"code": "st", "name": "Sesotho", "native": "Sesotho", "flag": "🇱🇸"}, {"code": "tn", "name": "Tswana", "native": "Setswana", "flag": "🇧🇼"}, {"code": "ts", "name": "Tsonga", "native": "Xitsonga", "flag": "🇿🇦"}, {"code": "ss", "name": "Swati", "native": "SiSwati", "flag": "🇸🇿"}, {"code": "ve", "name": "Venda", "native": "Tshivenḓa", "flag": "🇿🇦"}, {"code": "nr", "name": "South Ndebele", "native": "isiNdebele", "flag": "🇿🇦"}, {"code": "om", "name": "Oromo", "native": "Afaan Oromoo", "flag": "🇪🇹"}, {"code": "ti", "name": "Tigrinya", "native": "ትግርኛ", "flag": "🇪🇷"}, {"code": "tg", "name": "Tajik", "native": "Тоҷикӣ", "flag": "🇹🇯"}, {"code": "tk", "name": "Turkmen", "native": "Türkmençe", "flag": "🇹🇲"}, {"code": "ky", "name": "Kyrgyz", "native": "Кыргызча", "flag": "🇰🇬"}, {"code": "ps", "name": "Pashto", "native": "پښتو", "flag": "🇦🇫"}, {"code": "ku", "name": "Kurdish", "native": "Kurdî", "flag": "🇮🇶"}, {"code": "sd", "name": "Sindhi", "native": "سنڌي", "flag": "🇵🇰"}, {"code": "ug", "name": "Uyghur", "native": "ئۇيغۇرچە", "flag": "🇨🇳"}, {"code": "be", "name": "Belarusian", "native": "Беларуская", "flag": "🇧🇾"}, {"code": "ca", "name": "Catalan", "native": "Català", "flag": "🇪🇸"}, {"code": "gl", "name": "Galician", "native": "Galego", "flag": "🇪🇸"}, {"code": "eu", "name": "Basque", "native": "Euskara", "flag": "🇪🇸"}, {"code": "lb", "name": "Luxembourgish", "native": "Lëtzebuergesch", "flag": "🇱🇺"}, {"code": "fo", "name": "Faroese", "native": "Føroyskt", "flag": "🇫🇴"}, {"code": "gd", "name": "Scottish Gaelic", "native": "Gàidhlig", "flag": "🇬🇧"}, {"code": "co", "name": "Corsican", "native": "Corsu", "flag": "🇫🇷"}, {"code": "eo", "name": "Esperanto", "native": "Esperanto", "flag": "🌐"}, {"code": "la", "name": "Latin", "native": "Latina", "flag": "🏛️"}, {"code": "yi", "name": "Yiddish", "native": "ייִדיש", "flag": "✡️"}, {"code": "ht", "name": "Haitian Creole", "native": "Kreyòl Ayisyen", "flag": "🇭🇹"}, {"code": "sm", "name": "Samoan", "native": "Gagana Sāmoa", "flag": "🇼🇸"}, {"code": "to", "name": "Tongan", "native": "lea faka-Tonga", "flag": "🇹🇴"}, {"code": "fj", "name": "Fijian", "native": "Na Vosa Vakaviti", "flag": "🇫🇯"}, {"code": "mi", "name": "Maori", "native": "Te Reo Māori", "flag": "🇳🇿"}, {"code": "haw", "name": "Hawaiian", "native": "ʻŌlelo Hawaiʻi", "flag": "🌺"}, {"code": "ceb", "name": "Cebuano", "native": "Bisaya", "flag": "🇵🇭"}, {"code": "sa", "name": "Sanskrit", "native": "संस्कृतम्", "flag": "🇮🇳"}, {"code": "bho", "name": "Bhojpuri", "native": "भोजपुरी", "flag": "🇮🇳"}, {"code": "mai", "name": "Maithili", "native": "मैथिली", "flag": "🇮🇳"}, {"code": "kok", "name": "Konkani", "native": "कोंकणी", "flag": "🇮🇳"}, {"code": "mni", "name": "Manipuri", "native": "ꯃꯤꯇꯩꯂꯣꯟ", "flag": "🇮🇳"}, {"code": "sat", "name": "Santali", "native": "ᱥᱟᱱᱛᱟᱲᱤ", "flag": "🇮🇳"}, {"code": "brx", "name": "Bodo", "native": "बर’", "flag": "🇮🇳"}, {"code": "doi", "name": "Dogri", "native": "डोगरी", "flag": "🇮🇳"}, {"code": "lus", "name": "Mizo", "native": "Mizo ṭawng", "flag": "🇮🇳"}, {"code": "kha", "name": "Khasi", "native": "Ka Ktien Khasi", "flag": "🇮🇳"}, {"code": "gar", "name": "Garo", "native": "A·chik", "flag": "🇮🇳"}, {"code": "tt", "name": "Tatar", "native": "Татарча", "flag": "🇷🇺"}, {"code": "ba", "name": "Bashkir", "native": "Башҡортса", "flag": "🇷🇺"}, {"code": "cv", "name": "Chuvash", "native": "Чӑвашла", "flag": "🇷🇺"}, {"code": "sah", "name": "Sakha (Yakut)", "native": "Саха тыла", "flag": "🇷🇺"}, {"code": "qu", "name": "Quechua", "native": "Runasimi", "flag": "🇵🇪"}, {"code": "ay", "name": "Aymara", "native": "Aymar aru", "flag": "🇧🇴"}, {"code": "gn", "name": "Guarani", "native": "Avañe'ẽ", "flag": "🇵🇾"}, {"code": "wo", "name": "Wolof", "native": "Wolof", "flag": "🇸🇳"}, {"code": "ff", "name": "Fulah", "native": "Pulaar", "flag": "🇸🇳"}, {"code": "bm", "name": "Bambara", "native": "Bamanankan", "flag": "🇲🇱"}, {"code": "ee", "name": "Ewe", "native": "Èʋegbe", "flag": "🇬🇭"}, {"code": "ak", "name": "Akan", "native": "Akan", "flag": "🇬🇭"}, {"code": "lg", "name": "Ganda (Luganda)", "native": "Oluganda", "flag": "🇺🇬"}, {"code": "ln", "name": "Lingala", "native": "Lingála", "flag": "🇨🇩"}, {"code": "ki", "name": "Kikuyu", "native": "Gĩkũyũ", "flag": "🇰🇪"}, {"code": "fy", "name": "Western Frisian", "native": "Frysk", "flag": "🇳🇱"}, {"code": "kl", "name": "Greenlandic", "native": "Kalaallisut", "flag": "🇬🇱"}, {"code": "iu", "name": "Inuktitut", "native": "ᐃᓄᒃᑎᑐᑦ", "flag": "🇨🇦"}, {"code": "chr", "name": "Cherokee", "native": "ᏣᎳᎩ ᎦᏬᏂᎯᏍᏗ", "flag": "🇺🇸"}, {"code": "nav", "name": "Navajo", "native": "Diné bizaad", "flag": "🇺🇸"}, {"code": "dv", "name": "Divehi", "native": "ދިވެހި", "flag": "🇲🇻"}, {"code": "dz", "name": "Dzongkha", "native": "རྫོང་ཁ", "flag": "🇧🇹"}, {"code": "bo", "name": "Tibetan", "native": "བོད་སྐད་", "flag": "🇨🇳"}, {"code": "hmn", "name": "Hmong", "native": "Hmoob", "flag": "🌐"}, {"code": "ilo", "name": "Ilocano", "native": "Ilokano", "flag": "🇵🇭"}, {"code": "war", "name": "Waray", "native": "Winaray", "flag": "🇵🇭"}, {"code": "hil", "name": "Hiligaynon", "native": "Ilonggo", "flag": "🇵🇭"}, {"code": "pam", "name": "Kapampangan", "native": "Kapampangan", "flag": "🇵🇭"}, {"code": "bik", "name": "Bikol", "native": "Bikol", "flag": "🇵🇭"}, {"code": "pag", "name": "Pangasinan", "native": "Pangasinan", "flag": "🇵🇭"}, {"code": "jw", "name": "Javanese", "native": "Basa Jawa", "flag": "🇮🇩"}, {"code": "sc", "name": "Sardinian", "native": "Sardu", "flag": "🇮🇹"}, {"code": "rm", "name": "Romansh", "native": "Rumantsch", "flag": "🇨🇭"}, {"code": "fur", "name": "Friulian", "native": "Furlan", "flag": "🇮🇹"}, {"code": "vec", "name": "Venetian", "native": "Vèneto", "flag": "🇮🇹"}, {"code": "lmo", "name": "Lombard", "native": "Lombard", "flag": "🇮🇹"}, {"code": "lij", "name": "Ligurian", "native": "Lìgure", "flag": "🇮🇹"}, {"code": "nap", "name": "Neapolitan", "native": "Napulitano", "flag": "🇮🇹"}, {"code": "scn", "name": "Sicilian", "native": "Sicilianu", "flag": "🇮🇹"}, {"code": "ast", "name": "Asturian", "native": "Asturianu", "flag": "🇪🇸"}, {"code": "an", "name": "Aragonese", "native": "Aragonés", "flag": "🇪🇸"}, {"code": "oc", "name": "Occitan", "native": "Occitan", "flag": "🇫🇷"}, {"code": "br", "name": "Breton", "native": "Brezhoneg", "flag": "🇫🇷"}, {"code": "kw", "name": "Cornish", "native": "Kernewek", "flag": "🇬🇧"}, {"code": "gv", "name": "Manx", "native": "Gaelg", "flag": "🇮🇲"}, {"code": "se", "name": "Northern Sami", "native": "Davvisámegiella", "flag": "🇳🇴"}, {"code": "tyv", "name": "Tuvan", "native": "Тыва дыл", "flag": "🇷🇺"}, {"code": "os", "name": "Ossetian", "native": "Ирон", "flag": "🇷🇺"}, {"code": "ab", "name": "Abkhaz", "native": "Аҧсуа бызшәа", "flag": "🇬🇪"}, {"code": "av", "name": "Avar", "native": "Авар мацӏ", "flag": "🇷🇺"}, {"code": "ce", "name": "Chechen", "native": "Нохчийн мотт", "flag": "🇷🇺"}, {"code": "inh", "name": "Ingush", "native": "ГIалгIай мотт", "flag": "🇷🇺"}, {"code": "lez", "name": "Lezgian", "native": "Лезги чIал", "flag": "🇷🇺"}, {"code": "ch", "name": "Chamorro", "native": "Chamoru", "flag": "🇬🇺"}, {"code": "sg", "name": "Sango", "native": "Sängö", "flag": "🇨🇫"}, {"code": "rn", "name": "Rundi", "native": "Ikirundi", "flag": "🇧🇮"}, {"code": "kg", "name": "Kongo", "native": "Kikongo", "flag": "🇨🇬"}, {"code": "lu", "name": "Luba-Katanga", "native": "Kiluba", "flag": "🇨🇩"}, {"code": "tw", "name": "Twi", "native": "Twi", "flag": "🇬🇭"}, {"code": "aa", "name": "Afar", "native": "Qafár af", "flag": "🇩🇯"}];

  var TOP_LANG_CODES = ['en', 'es', 'fr', 'de', 'ja', 'zh-CN', 'hi', 'gu', 'ar', 'pt', 'ru', 'it', 'ko', 'nl', 'tr', 'vi', 'id', 'pl', 'sv', 'uk'];

  // Initialize Google Translate Element Callback
  window.googleTranslateElementInit = function () {
    if (window.google && window.google.translate) {
      new window.google.translate.TranslateElement({
        pageLanguage: 'en',
        autoDisplay: false,
        layout: window.google.translate.TranslateElement.InlineLayout.SIMPLE
      }, 'google_translate_element');
    }
    checkAndApplyInitialLanguage();
  };

  // Load Google Translate script asynchronously
  function loadGoogleTranslateScript() {
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
  }

  // Set Google Translate Cookie and trigger translation
  function setLanguage(langCode) {
    if (!langCode) return;
    var gtCode = langCode;
    if (gtCode === 'en' || gtCode === 'en-US' || gtCode === 'en-GB' || gtCode === 'en-CA' || gtCode === 'en-AU' || gtCode === 'en-IN') {
      gtCode = 'en';
    }

    localStorage.setItem('portfolio_target_lang', langCode);

    try {
      var url = new URL(window.location.href);
      if (langCode === 'en') {
        url.searchParams.delete('lang');
      } else {
        url.searchParams.set('lang', langCode);
      }
      window.history.replaceState({}, '', url.toString());
    } catch (e) {}

    var hostname = window.location.hostname;
    var cookieVal = (langCode === 'en') ? '' : '/en/' + gtCode;
    
    if (langCode === 'en') {
      document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
      document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=' + hostname + ';';
    } else {
      document.cookie = 'googtrans=' + cookieVal + '; path=/;';
      document.cookie = 'googtrans=' + cookieVal + '; path=/; domain=' + hostname + ';';
    }

    var select = document.querySelector('.goog-te-combo');
    if (select) {
      select.value = gtCode;
      select.dispatchEvent(new Event('change'));
    } else {
      var attempts = 0;
      var interval = setInterval(function() {
        attempts++;
        var sel = document.querySelector('.goog-te-combo');
        if (sel) {
          clearInterval(interval);
          sel.value = gtCode;
          sel.dispatchEvent(new Event('change'));
        } else if (attempts > 5) {
          clearInterval(interval);
          location.reload();
        }
      }, 150);
    }

    updateActiveButtonDisplay(langCode);
    closeLanguageModal();
  }

  function updateActiveButtonDisplay(langCode) {
    var found = ALL_LANGUAGES.find(function(l) { return l.code === langCode; });
    var currentBadge = document.getElementById('currentLangBadge');
    if (currentBadge && found) {
      currentBadge.textContent = found.code.toUpperCase();
    }
  }

  function checkAndApplyInitialLanguage() {
    var urlParams = new URLSearchParams(window.location.search);
    var langParam = urlParams.get('lang');
    var savedLang = localStorage.getItem('portfolio_target_lang');
    var target = langParam || savedLang;

    if (target && target !== 'en') {
      var checkCombo = setInterval(function() {
        var select = document.querySelector('.goog-te-combo');
        if (select) {
          clearInterval(checkCombo);
          select.value = target;
          select.dispatchEvent(new Event('change'));
          updateActiveButtonDisplay(target);
        }
      }, 200);

      setTimeout(function() {
        clearInterval(checkCombo);
      }, 4000);
    }
  }

  function initLanguageUI() {
    if (!document.getElementById('globalLangFloatingBtn')) {
      var floatBtn = document.createElement('button');
      floatBtn.id = 'globalLangFloatingBtn';
      floatBtn.className = 'global-lang-floating-btn';
      floatBtn.setAttribute('aria-label', 'Change Language (200+ Available)');
      floatBtn.setAttribute('title', 'Select from 200+ World Languages');
      floatBtn.innerHTML = '<span class="lang-btn-globe">🌐</span> <span id="currentLangBadge">EN</span> <span class="lang-btn-badge">200+</span>';
      floatBtn.onclick = openLanguageModal;
      document.body.appendChild(floatBtn);
    }

    document.querySelectorAll('.masthead-lang-trigger').forEach(function(el) {
      el.onclick = openLanguageModal;
    });

    if (!document.getElementById('globalLangModalOverlay')) {
      var modalOverlay = document.createElement('div');
      modalOverlay.id = 'globalLangModalOverlay';
      modalOverlay.className = 'global-lang-modal-overlay';
      modalOverlay.onclick = function(e) {
        if (e.target === modalOverlay) closeLanguageModal();
      };

      var quickPillsHtml = TOP_LANG_CODES.map(function(code) {
        var found = ALL_LANGUAGES.find(function(l) { return l.code === code; });
        if (!found) return '';
        return '<button type="button" class="quick-lang-tag" data-code="' + found.code + '">' + found.flag + ' ' + found.name + '</button>';
      }).join('');

      var langItemsHtml = ALL_LANGUAGES.map(function(lang) {
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
      }).join('');

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
      document.getElementById('globalLangResetBtn').onclick = function() {
        setLanguage('en');
      };

      var searchInput = document.getElementById('globalLangSearchInput');
      searchInput.oninput = function() {
        var q = this.value.trim().toLowerCase();
        var items = document.querySelectorAll('.global-lang-item');
        items.forEach(function(item) {
          var code = item.getAttribute('data-code').toLowerCase();
          var name = item.getAttribute('data-name');
          var native = item.getAttribute('data-native');
          if (!q || code.indexOf(q) !== -1 || name.indexOf(q) !== -1 || native.indexOf(q) !== -1) {
            item.style.display = 'flex';
          } else {
            item.style.display = 'none';
          }
        });
      };

      document.getElementById('globalLangGrid').onclick = function(e) {
        var target = e.target.closest('.global-lang-item');
        if (target) {
          var code = target.getAttribute('data-code');
          setLanguage(code);
        }
      };

      modalOverlay.querySelector('.global-lang-quick-bar').onclick = function(e) {
        var target = e.target.closest('.quick-lang-tag');
        if (target) {
          var code = target.getAttribute('data-code');
          setLanguage(code);
        }
      };
    }
  }

  function openLanguageModal() {
    var overlay = document.getElementById('globalLangModalOverlay');
    if (overlay) {
      overlay.classList.add('active');
      var searchInput = document.getElementById('globalLangSearchInput');
      if (searchInput) {
        searchInput.value = '';
        searchInput.focus();
        document.querySelectorAll('.global-lang-item').forEach(function(i) { i.style.display = 'flex'; });
      }
    }
  }

  function closeLanguageModal() {
    var overlay = document.getElementById('globalLangModalOverlay');
    if (overlay) overlay.classList.remove('active');
  }

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeLanguageModal();
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      loadGoogleTranslateScript();
      initLanguageUI();
    });
  } else {
    loadGoogleTranslateScript();
    initLanguageUI();
  }

})();
