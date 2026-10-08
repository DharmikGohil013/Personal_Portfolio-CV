# Blog build pipeline

The 16 articles, 6 topic hubs and `blog.html` are **generated**. Do not edit `blog/*.html`, `blog/topics/*.html` or `blog.html` by hand; your changes will be overwritten the next time the build runs.

## Write or edit an article

1. Article body (HTML fragment, `<h2>` for sections, no `<h1>`): `tools/blog/posts/<slug>.html`
2. SEO + editorial metadata (title, description, date, topic, tags, takeaways, FAQs, related posts, contextual links): `tools/blog/content.py`
3. Rebuild everything: `python tools/blog/make.py`

`make.py` runs, in order:

| Script | What it does |
| --- | --- |
| `build.py` | Renders posts, topic hubs and the blog index; rewrites the blog entries of `sitemap.xml`, the blog section of `llms.txt` and `feed.xml` |
| `patch_index.py` | Home page: kinetic headline, ticker, orbit diagram, process pipeline, "Field Notes", link hub, client showcase |
| `patch_pages.py` | About, Services, Portfolio, Achievements, Contact: related-reading block, link hub, motion layer |
| `patch_misc.py` | HTML sitemap blog section, `robots.txt` tooling rule, home-page `ItemList` JSON-LD |
| `audit.py` | Broken local links/assets, duplicate ids, missing alt text, h1 count, JSON-LD validity |

All patch scripts are idempotent (they replace fenced `<!-- motion:... -->` blocks), so re-running is safe.

## Add a new article

Add `posts/<slug>.html`, add an entry to `POSTS` and list the slug under a topic in `TOPICS` (both in `content.py`), add `"<slug>": {"title": ..., "cover": ..., "cover_alt": ...}` to `extracted.json`, then run `make.py`.

## Notes

* `extract.py` was a one-time migration from the legacy pages; it reads them from the pre-migration commit and should not be re-run.
* Missing images referenced by an article are dropped at build time with a `[warn]` line, so the page never ships broken-image icons.
* Motion is progressive: everything is gated behind `html.motion-ok`, which is only set when the visitor has not requested reduced motion.
