"""MkDocs hook: bust browser/CDN cache for extra.css (same URL = stale styles on GitHub Pages)."""

from __future__ import annotations

import hashlib
import pathlib
import re

_CSS_PATTERN = re.compile(r'stylesheets/extra\.css(?:\?[^"#]*)?(?=")')


def on_post_build(config, **kwargs) -> None:
    site_dir = pathlib.Path(config["site_dir"])
    css_path = site_dir / "stylesheets" / "extra.css"
    if not css_path.is_file():
        return
    digest = hashlib.md5(css_path.read_bytes()).hexdigest()[:12]
    replacement = f"stylesheets/extra.css?v={digest}"
    for html_path in site_dir.rglob("*.html"):
        text = html_path.read_text(encoding="utf-8")
        if "stylesheets/extra.css" not in text:
            continue
        new_text = _CSS_PATTERN.sub(replacement, text)
        if new_text != text:
            html_path.write_text(new_text, encoding="utf-8")
