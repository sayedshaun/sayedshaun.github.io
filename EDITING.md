# How this site works

`README.md` **is** the website. `index.html` reads it and renders it. Nothing else.

- Edit `README.md`, commit, push. Done — no build, no Jekyll, no YAML, no Actions.
- Swap your photo by overwriting `profile.jpg` (same filename).
- Swap your résumé by overwriting `resume.pdf` (same filename).
- Add a section: write `## Section Name` — it appears in the top nav automatically.

## Formatting conventions the page styles for you

You only ever write plain markdown. The page recognises four patterns:

| You write | You get |
|---|---|
| a lone image on its own line | round avatar |
| a line of `` `backticked` `` words right under a heading | small mono date / meta line |
| a paragraph made only of `` `backticked` `` words | pill-shaped tag chips |
| a paragraph made only of links | row of buttons |

Everything else — headings, lists, bold, links, code blocks, tables, quotes — renders as
normal markdown.

## Preview locally

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

Opening `index.html` directly as a `file://` path will not work — the browser blocks
reading `README.md` that way. Any http server is fine.

## Publishing on GitHub Pages

Push this folder to a repo, then Settings → Pages → Source: *Deploy from a branch* →
`main` / `/ (root)`. The `.nojekyll` file is there so GitHub serves `README.md` as-is
instead of trying to build it.

Note: GitHub *also* displays `README.md` on your repo homepage. Same file, two views —
that's a feature, not a conflict.

## Old files

The previous Jekyll version (layouts, `_data/*.yml`, CSS, JS) is parked in
`.old-jekyll/`. Delete that folder whenever you're happy.
