# sayedshaun.github.io

Personal site — [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), live at
<https://sayedshaun.github.io>.

```bash
.venv/bin/mkdocs serve      # http://127.0.0.1:8000, live-reloads
```

Push to `main` and the site rebuilds and deploys itself.

## Editing

One markdown file per page under `docs/`; add a page by creating the file and adding a line
under `nav:` in `mkdocs.yml`. Looks come from `docs/assets/css/theme.css`.

Patterns the stylesheet expects:

- `<div class="entry" markdown>` wrapping `<div class="entry-mark">AI</div>` — an entry row
  with a monogram tile, used for jobs, papers, degrees and certificates.
- `{ .meta }` after a line — the monospace date/issuer line.
- `<div class="grid cards" markdown>` — Material's card grid; add `stack` for one box per row.

## Résumé

`docs/files/resume.pdf` is refreshed from
[sayedshaun/resume.latex](https://github.com/sayedshaun/resume.latex) on every deploy by
`scripts/fetch_resume.py`. Edit the CV there and push to `main`, and this site catches up on
the next deploy, or within a day via the cron in the workflow. If GitHub is unreachable the
committed PDF ships unchanged — it never breaks a deploy.
