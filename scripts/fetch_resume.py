#!/usr/bin/env python3
"""Fetch the current résumé PDF from the resume.latex GitHub repo.

Usage:
    python3 scripts/fetch_resume.py [destination.pdf]

Exits 0 even when the fetch fails, leaving any existing file untouched — a
stale résumé is better than a broken deploy. Pass --strict to fail instead.
"""

from __future__ import annotations

import os
import sys
import urllib.error
import urllib.request

RESUME_URL = "https://raw.githubusercontent.com/sayedshaun/resume.latex/main/main.pdf"
DEFAULT_DEST = "docs/files/resume.pdf"
MIN_BYTES = 1024


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "sayedshaun.github.io"})
    with urllib.request.urlopen(req, timeout=60) as response:
        pdf = response.read()
    if not pdf.startswith(b"%PDF") or len(pdf) < MIN_BYTES:
        raise RuntimeError(f"downloaded {len(pdf)} bytes that are not a PDF")
    return pdf


def main() -> int:
    strict = "--strict" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    dest = args[0] if args else DEFAULT_DEST

    try:
        pdf = fetch(RESUME_URL)
    except (urllib.error.URLError, RuntimeError, ValueError) as exc:
        print(f"could not fetch the résumé from GitHub: {exc}", file=sys.stderr)
        print("keeping the committed copy", file=sys.stderr)
        return 1 if strict else 0

    previous = b""
    if os.path.exists(dest):
        with open(dest, "rb") as handle:
            previous = handle.read()

    if pdf == previous:
        print(f"résumé unchanged ({len(pdf):,} bytes)")
        return 0

    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    with open(dest, "wb") as handle:
        handle.write(pdf)
    print(f"résumé updated: {len(previous):,} → {len(pdf):,} bytes at {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
