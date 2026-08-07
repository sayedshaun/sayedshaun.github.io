# Portfolio — MkDocs experiment

Experimental branch. Rebuilds the portfolio as a **multi-page MkDocs site**, in the style of
[fralfaro/portfolio](https://github.com/fralfaro/portfolio) — sidebar nav, a home page of
icon cards, per-section card grids, a timeline, search, and a light/dark toggle.

`main` keeps the zero-build version (one `index.html` rendering markdown at load time) and is
what https://sayedshaun.github.io currently serves. **This branch changes nothing live.**

## Preview locally

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve            # http://127.0.0.1:8000 — live-reloads as you edit
```

## Content layout

```
mkdocs.yml                  site config + nav (add a page → add a nav line)
docs/index.md               home: hero + icon cards
docs/about/profile.md
docs/about/experience.md    card grid + timeline
docs/about/education.md
docs/about/skills.md
docs/research/publications.md
docs/portfolio/projects.md  neoteroi cards
docs/contact.md
docs/assets/css/styles.css  hero, card, profile-item styles
docs/css/                   neoteroi cards/timeline stylesheet
docs/images/                profile photo + card icons (inline SVG, no downloads)
docs/files/resume.pdf
```

## Trade-off vs `main`

| | `main` | this branch |
|---|---|---|
| Dependencies | none | Python + MkDocs + 2 packages |
| Build step | none | `mkdocs build` |
| Editing | one markdown file per section | same, plus a nav entry in `mkdocs.yml` |
| Pages | single scrolling page | multi-page with sidebar + search |
| Deploy | `git push` | `mkdocs gh-deploy` or an Actions workflow |

## Deploying this version (only if you decide to adopt it)

```bash
mkdocs gh-deploy        # builds and pushes to the gh-pages branch
```

Then switch GitHub Pages source to `gh-pages` in repo Settings → Pages. Until you do that,
`main` stays live.
