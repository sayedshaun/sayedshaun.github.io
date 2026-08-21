# sayedshaun.github.io — fralfaro-style branch

Personal site built on the layout of [fralfaro/portfolio](https://github.com/fralfaro/portfolio)
(MIT) — the [Dracula theme for MkDocs](https://github.com/dracula/mkdocs), neoteroi cards and
timeline, a sidebar portrait, and a home page of cards linking into each section — with its own
visual identity on top.

`docs/assets/css/styles.css` and `docs/css/neoteroi-mkdocs.css` come from that project.
`docs/assets/css/extra.css` is the identity layer: a slate-and-teal palette in place of the
Dracula purples, Inter for body copy instead of theme-wide monospace, flat chrome instead of
the gradient header and diamond toggle, and teal line icons instead of colour emoji.
`overrides/modules/` replaces the theme's sidebar block and footer with my own.

`main` carries a different design — a single-page site with a hand-written theme.

## Content layout

```
mkdocs.yml                    theme, nav, extensions
docs/index.md                 home: icon cards per section
docs/about_me/me.md           presentation card
docs/about_me/education.md
docs/about_me/work_exp.md     work + tech experience, timeline
docs/about_me/skills.md
docs/research/research.md     publications
docs/research/talks.md
docs/software/projects.md     neoteroi cards + details table
docs/contact.md
docs/assets/css/styles.css    from fralfaro/portfolio
docs/assets/css/extra.css     badges, single-column card grids, social row
docs/css/neoteroi-mkdocs.css  cards / timeline stylesheet
docs/images/icons/*.svg       twemoji card icons
```

Adding a page = create the markdown file and add one line under `nav:` in `mkdocs.yml`.

Conventions the CSS styles: `<div class="card-grid">` wraps one or two `<div class="card">`
columns (add `single` to the grid for a full-width card); inside a card, `<article
class="profile-item">` pairs a `<div class="profile-badge">` monogram with a heading,
a `<p class="profile-meta">` line, and body copy.

## Preview locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve          # http://127.0.0.1:8000
```

## Deploying

`.github/workflows/deploy.yml` builds and publishes to GitHub Pages on every push to `main`.
This branch is not deployed unless it is merged there. One-time setup:
**Settings → Pages → Source → GitHub Actions** (Pages also requires the repo to be public on
a free plan).
