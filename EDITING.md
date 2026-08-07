# How this site works

Plain markdown files, assembled by `index.html` at page load. No build step.

```
README.md              header only — name, tagline, photo, intro, link buttons
docs/experience.md     one file per section
docs/projects.md
docs/publications.md
docs/skills.md
docs/education.md
docs/contact.md
docs/sections.txt      which sections appear, and in what order
index.html             the renderer. Never edit this.
profile.jpg            your photo (overwrite, same filename)
resume.pdf             your résumé (overwrite, same filename)
```

Edit a file, commit, push. Live in ~30 seconds.

## Adding a section

1. Create `docs/awards.md` starting with a `##` heading:

   ```markdown
   ## Awards

   ### Best Paper — Some Conference
   `2027` · Dhaka, Bangladesh

   - What it was for.
   ```

2. Add one line to `docs/sections.txt`:

   ```
   docs/awards.md
   ```

It appears on the page, and in the top nav, automatically. Reorder sections by moving
lines in `sections.txt`; hide one by deleting its line or prefixing it with `#`.

Horizontal rules between sections are added for you — don't put `---` in your files.

## Formatting conventions the page styles for you

You only write plain markdown. The renderer recognises four patterns:

| You write | You get |
|---|---|
| a lone image on its own line | round avatar |
| a line of `` `backticked` `` words right under a heading | small mono date / meta line |
| a paragraph made only of `` `backticked` `` words | pill-shaped tag chips |
| a paragraph made only of links | row of buttons |

Everything else — headings, lists, bold, links, code blocks, tables, quotes — renders as
normal markdown. `##` becomes a section (and a nav item); `###` is an entry within it.

Image and file paths are resolved from the **site root**, not from `docs/`. So write
`![me](profile.jpg)`, not `../profile.jpg`, even inside `docs/`.

## Preview locally

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

Opening `index.html` as a `file://` path will not work — the browser blocks reading the
markdown files that way. Any http server is fine.

## Publishing

Already set up: repo `sayedshaun/sayedshaun.github.io`, GitHub Pages serving `main` at the
root, live at https://sayedshaun.github.io. `.nojekyll` tells GitHub to serve the files
as-is instead of running Jekyll on them.

Pushing to `main` is the entire deploy:

```bash
git add -A && git commit -m "update" && git push
```

## Old files

The previous Jekyll version and your original full-size photo are parked in
`.old-jekyll/` (gitignored, never pushed). Delete it whenever you're ready.
