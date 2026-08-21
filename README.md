# sayedshaun.github.io

Personal site — a single scrolling page built from markdown by [MkDocs](https://www.mkdocs.org/)
with a small hand-written theme. Live at <https://sayedshaun.github.io>.

## Editing

Everything you'd normally want to change lives in `docs/_content/` — one markdown file per
section, stitched together in file-name order by `docs/index.md`:

```
docs/_content/00-intro.md         left rail: photo, name, tagline, bio, status, links
docs/_content/05-about.md         the longer story
docs/_content/10-experience.md    jobs
docs/_content/20-projects.md      projects
docs/_content/30-research.md      publications + interests
docs/_content/40-education.md     degree
docs/_content/50-toolkit.md       stack table
docs/_content/60-contact.md       contact
```

Everything before the first `##` heading becomes the sticky left rail; everything after it is
the scrolling column. Adding a section = add `docs/_content/70-writing.md` starting with
`## Writing`, then add one `--8<-- "70-writing.md"` line to `docs/index.md`. The nav and the
section numbers build themselves from the `##` headings, so nothing else needs updating.

### Markdown conventions the theme styles

| You write | It renders as |
|---|---|
| `## Experience` | small-caps section label with a hairline |
| `### Role · Company` | entry title (wrap it in `[...](url)` to link it) |
| `*Jul 2026 — present · Dhaka*` (a line of its own, italic) | monospace meta line |
| `- item` | dash-marked list |
| `{ .note }` after a paragraph | accent-bar callout |
| `{ .links }` after a row of links | pill buttons |
| `{ .status }` after a short line | monospace line with a pulsing dot |
| a list wrapped in `<div class="stack" markdown>` | label / value rows (the Toolkit table) |

Other files: `docs/images/profile.jpg` (photo), `docs/files/resume.pdf` (résumé),
`theme/main.html` + `theme/assets/style.css` (layout, colours, type), `mkdocs.yml` (site
metadata and the footer links).

## Preview locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve          # http://127.0.0.1:8000 — live-reloads as you edit
```

## Deploying

Push or merge to `main` — `.github/workflows/deploy.yml` builds the site and publishes it to
GitHub Pages. One-time setup: **repo Settings → Pages → Source → GitHub Actions**.
