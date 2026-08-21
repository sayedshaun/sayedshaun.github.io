#!/usr/bin/env python3
"""Fetch the current résumé PDF from an Overleaf read-only share link.

Overleaf publishes no direct URL for a compiled PDF, so this walks the same
path a browser does: grant anonymous read access with the share token, ask the
project to compile, then download the build output.

Usage:
    OVERLEAF_READ_URL="https://www.overleaf.com/read/<token>" \
        python3 scripts/fetch_resume.py [destination.pdf]

Exits 0 even when the fetch fails, leaving any existing file untouched — a
stale résumé is better than a broken deploy. Pass --strict to fail instead.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from http.cookiejar import CookieJar

BASE = "https://www.overleaf.com"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
DEFAULT_DEST = "docs/files/resume.pdf"
MIN_BYTES = 1024

opener = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(CookieJar())
)


def get(url: str, headers: dict | None = None, data: bytes | None = None) -> bytes:
    req = urllib.request.Request(url, data=data, method="POST" if data else "GET")
    req.add_header("User-Agent", UA)
    for key, value in (headers or {}).items():
        req.add_header(key, value)
    with opener.open(req, timeout=60) as response:
        return response.read()


def csrf_from(html: str) -> str:
    match = re.search(r'name="ol-csrfToken"\s+content="([^"]+)"', html)
    if not match:
        raise RuntimeError("no CSRF token on the page — Overleaf markup changed?")
    return match.group(1)


def fetch(read_url: str) -> bytes:
    token = read_url.rstrip("/").split("/read/")[-1].split("#")[0].split("?")[0]
    if not token:
        raise RuntimeError(f"could not read a share token out of {read_url!r}")

    # 1. load the share page for a session cookie and a CSRF token
    csrf = csrf_from(get(f"{BASE}/read/{token}").decode("utf-8", "replace"))

    # 2. trade the token for anonymous read-only access to the project
    grant = json.loads(
        get(
            f"{BASE}/read/{token}/grant",
            headers={"Content-Type": "application/json", "Accept": "application/json",
                     "x-csrf-token": csrf},
            data=json.dumps({"confirmedByUser": True, "_csrf": csrf}).encode(),
        )
    )
    project_id = grant.get("redirect", "").rstrip("/").split("/")[-1]
    if not re.fullmatch(r"[0-9a-f]{24}", project_id):
        raise RuntimeError(f"unexpected grant response: {grant}")

    # 3. the project page issues its own CSRF token for the compile call
    csrf = csrf_from(get(f"{BASE}/project/{project_id}").decode("utf-8", "replace"))
    result = json.loads(
        get(
            f"{BASE}/project/{project_id}/compile?enable_pdf_caching=false",
            headers={"Content-Type": "application/json", "Accept": "application/json",
                     "x-csrf-token": csrf},
            data=json.dumps({"check": "silent", "draft": False,
                             "incrementalCompilesEnabled": True,
                             "stopOnFirstError": False}).encode(),
        )
    )
    if result.get("status") != "success":
        raise RuntimeError(f"compile did not succeed: status={result.get('status')!r}")

    output = next((f for f in result.get("outputFiles", [])
                   if f.get("path", "").endswith(".pdf")), None)
    if not output:
        raise RuntimeError("compile produced no PDF")

    # 4. build outputs are served from a separate host, keyed by the build id
    domain = result.get("pdfDownloadDomain", BASE)
    query = f"?compileGroup={result.get('compileGroup', 'standard')}" \
            f"&clsiserverid={result.get('clsiServerId', '')}&enable_pdf_caching=false"
    pdf = get(domain + output["url"] + query,
              headers={"Referer": f"{BASE}/project/{project_id}"})

    if not pdf.startswith(b"%PDF") or len(pdf) < MIN_BYTES:
        raise RuntimeError(f"downloaded {len(pdf)} bytes that are not a PDF")
    return pdf


def main() -> int:
    strict = "--strict" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    dest = args[0] if args else DEFAULT_DEST

    read_url = os.environ.get("OVERLEAF_READ_URL", "").strip()
    if not read_url:
        print("OVERLEAF_READ_URL is not set — keeping the committed résumé", file=sys.stderr)
        return 1 if strict else 0

    try:
        pdf = fetch(read_url)
    except (urllib.error.URLError, RuntimeError, ValueError, KeyError) as exc:
        print(f"could not fetch the résumé from Overleaf: {exc}", file=sys.stderr)
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
