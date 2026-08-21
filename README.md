# sayedshaun.github.io — material branch

Personal site built on [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/),
restyled: a teal palette, Newsreader for display headings over Inter body text, tabbed
navigation, and a light/dark toggle. `main` carries a different design — a single scrolling
page with a hand-written theme.

## Content layout

```
mkdocs.yml                     theme, nav, palette, extensions
docs/index.md                  hero + grid cards + selected work (nav and toc hidden)
docs/about_me/me.md            profile
docs/about_me/work_exp.md      experience entries
docs/about_me/education.md
docs/about_me/skills.md
docs/research/research.md      publications
docs/research/talks.md
docs/software/projects.md      project grid cards
docs/contact.md
docs/assets/css/theme.css      palette, display type, hero, entry rows, cards
docs/images/profile.jpg
docs/files/resume.pdf          exported from Overleaf; the Résumé links download this file
```

Adding a page = create the markdown file and add one line under `nav:` in `mkdocs.yml`.

### Conventions the stylesheet adds

| You write | It renders as |
|---|---|
| `<div class="entry" markdown>` + `<div class="entry-mark">AI</div>` | an entry row with a monogram tile |
| `{ .meta }` after a line | monospace date/place line |
| `{ .hero-role }` / `{ .status }` | the hero's role line / status line with a dot |
| `<div class="tags" markdown><span>…</span></div>` | small tag chips |
| `<div class="grid cards" markdown>` | Material's card grid |

## Preview locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve          # http://127.0.0.1:8000
```

## Deploying

`.github/workflows/deploy.yml` builds and publishes to GitHub Pages on every push to `main`.
This branch is not deployed unless merged there. One-time setup: **Settings → Pages → Source →
GitHub Actions** (Pages also requires the repo to be public on a free plan).
