from html import escape, unescape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = [
    p for p in ROOT.rglob("*.html")
    if not any(part.lower() in {"assets", "tools", "node_modules", ".git"} for part in p.relative_to(ROOT).parts[:-1])
    and p.name.lower() not in {
        "dome-gallery-demo.html", "dome-gallery-diagnostic.html", "loader-test.html",
        "premium-loader-template.html", "schema-markup-complete.html", "meta-tags-templates.html",
    }
]

META = {
    "about.html": (
        "About Dharmik Gohil | Unity Game Developer in India",
        "Learn about Dharmik Gohil, a Unity game and full-stack developer in Surat, India. Explore his education, experience, skills, and projects.",
    ),
    "Achivemtn.html": (
        "Game Development Awards | Dharmik Gohil",
        "Explore Dharmik Gohil’s game development awards, including IIT Bombay Techfest, Global Game Jam, Code Raider Clash, and technical certifications.",
    ),
    "contact.html": (
        "Contact Dharmik Gohil | Hire a Unity Game Developer",
        "Contact Dharmik Gohil about Unity game development, multiplayer, XR, or full-stack projects. Based in Surat, India and open to remote work.",
    ),
    "game3.html": (
        "Memory Master | Unity Brain Training Game",
        "Play Memory Master, a Unity brain-training game by Dharmik Gohil. Test memory and focus through interactive matching challenges.",
    ),
    "game4.html": (
        "Mavericks Battlegrounds | Unity Multiplayer Game",
        "Explore Mavericks Battlegrounds, a Unity multiplayer game built with Photon PUN and showcased at CHARUSAT Expo 3.0.",
    ),
    "game5.html": (
        "Action Blitz | Unity 3D Mobile Action Game",
        "Play Action Blitz, a 3D mobile action game made with Unity by Dharmik Gohil. Explore its combat, power-ups, and gameplay.",
    ),
    "logo.html": (
        "Game UI & Logo Design | Dharmik Gohil Portfolio",
        "Explore game interface and logo design work by Dharmik Gohil, including UI/UX concepts for games and digital products.",
    ),
    "portfolio.html": (
        "Game Developer Portfolio | Dharmik Gohil",
        "Explore Unity games, multiplayer projects, XR experiences, and web apps by Dharmik Gohil, a game developer in Surat, India.",
    ),
    "services.html": (
        "Unity Game Development Services | Dharmik Gohil",
        "Hire Dharmik Gohil for Unity game development, multiplayer systems, XR experiences, or full-stack web projects. Based in Surat, India.",
    ),
    "blog/hackron-hackathon-2025-blinkit-experience.html": (
        "Hackron 2025: Building SafaiNova for Blinkit",
        "A 24-hour Hackron 2025 project for Blinkit: how our team built SafaiNova, an AI and IoT waste-management concept for dark stores.",
    ),
    "blog/topics/multiplayer-game-development.html": (
        "Multiplayer Game Development | Photon PUN & WebSockets",
        "Learn how Unity multiplayer games use Photon PUN2, lobbies, player synchronization, and latency handling, with Mavericks Battlegrounds case studies.",
    ),
    "mb-the-pack-unites/index.html": (
        "The Pack Unites | Tactical Multiplayer Game",
        "Explore The Pack Unites, a tactical team-based game concept by Dharmik Gohil with 5v5 combat, vehicles, procedural maps, and dynamic weather.",
    ),
    "mb-the-pack-unites/learn-more.html": (
        "The Pack Unites | Game Features & Gameplay",
        "See the features and gameplay planned for The Pack Unites: team combat, aerial vehicles, procedural maps, destructible environments, and dynamic weather.",
    ),
    "sitemap-page.html": (
        "Website Sitemap | Dharmik Gohil",
        "Browse the website sitemap for Dharmik Gohil’s portfolio, projects, services, and game development articles.",
    ),
    "protected-access.html": (
        "Protected Access | Dharmik Gohil",
        "",
    ),
}

def tag_pattern(key: str, attrs: tuple[str, ...]) -> re.Pattern[str]:
    allowed = "|".join(re.escape(a) for a in attrs)
    return re.compile(
        rf'<meta\b(?=[^>]*\b(?:{allowed})=["\']{re.escape(key)}["\'])[^>]*>', re.I | re.S
    )

def set_single_meta(source: str, key: str, value: str, attrs: tuple[str, ...], canonical_attr: str) -> str:
    pattern = tag_pattern(key, attrs)
    tags = list(pattern.finditer(source))
    tag = f'<meta {canonical_attr}="{key}" content="{escape(value, quote=True)}">'
    if tags:
        first = tags[0]
        source = source[:first.start()] + tag + source[first.end():]
        # Remove the remaining matching duplicate tags after replacing the first.
        source = pattern.sub("", source, count=0) if False else source
        matches = list(pattern.finditer(source))
        if matches:
            for match in reversed(matches[1:]):
                source = source[:match.start()] + source[match.end():]
    else:
        source = source.replace("</head>", f"  {tag}\n</head>", 1)
    return source

def set_description(source: str, value: str) -> str:
    return set_single_meta(source, "description", value, ("name",), "name")

for path in PUBLIC:
    rel = path.relative_to(ROOT).as_posix()
    data = path.read_bytes().decode("utf-8")
    newline = "\r\n" if "\r\n" in data else "\n"
    config = META.get(rel)
    if config:
        title, description = config
        title_markup = f"<title>{escape(title, quote=False)}</title>"
        data = re.sub(r"<title\b[^>]*>.*?</title>", lambda _: title_markup, data, count=1, flags=re.I | re.S)
        data = set_description(data, description)
    else:
        title_match = re.search(r"<title\b[^>]*>(.*?)</title>", data, re.I | re.S)
        desc_match = tag_pattern("description", ("name",)).search(data)
        if not title_match:
            continue
        title = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", title_match.group(1))).strip())
        description = ""
        if desc_match:
            content = re.search(r"\bcontent=[\"']([^\"']*)[\"']", desc_match.group(0), re.I | re.S)
            if content:
                description = unescape(content.group(1))
        if description:
            data = set_description(data, description)

    # Keep one canonical URL when legacy pages contain duplicate copies.
    canonical_re = re.compile(r'<link\b(?=[^>]*\brel=["\']canonical["\'])[^>]*>', re.I | re.S)
    canonicals = list(canonical_re.finditer(data))
    for match in reversed(canonicals[1:]):
        data = data[:match.start()] + data[match.end():]

    # Keep social snippets aligned with the page's own title and description.
    data = set_single_meta(data, "og:title", title, ("property",), "property")
    if description:
        data = set_single_meta(data, "og:description", description, ("property",), "property")
        data = set_single_meta(data, "twitter:description", description, ("name", "property"), "name")
    data = set_single_meta(data, "twitter:title", title, ("name", "property"), "name")
    # Normalize legacy Twitter tags from property= to the standard name= form.
    data = re.sub(r'<meta\s+property=((["\'])twitter:[^"\']+\2)', r'<meta name=\1', data, flags=re.I)

    if rel == "protected-access.html":
        if re.search(r'<meta\s+name=["\']robots["\']', data, re.I):
            data = re.sub(r'<meta\s+name=["\']robots["\'][^>]*>', '<meta name="robots" content="noindex, follow">', data, count=1, flags=re.I)
        else:
            data = data.replace("</head>", '  <meta name="robots" content="noindex, follow">\n</head>', 1)

    # Preserve each source file's original newline convention.
    if newline == "\r\n":
        data = data.replace("\r\n", "\n").replace("\n", "\r\n")
    path.write_bytes(data.encode("utf-8"))
