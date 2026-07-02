from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
NAME_RE = re.compile(r"^[A-Z0-9.-]+_Research_\d{8}\.html$")
LINK_RE = re.compile(r"""(?:href|src)=["']([^"']+)["']""", re.I)


def main() -> int:
    errors: list[str] = []
    reports = sorted(REPORTS.glob("*.html"))
    if not reports:
        errors.append("reports/ contains no HTML reports")

    index = (ROOT / "index.html").read_text(encoding="utf-8")
    for report in reports:
        rel = report.relative_to(ROOT).as_posix()
        text = report.read_text(encoding="utf-8")
        if not NAME_RE.match(report.name):
            errors.append(f"invalid report filename: {rel}")
        if rel not in index:
            errors.append(f"missing index entry: {rel}")
        if 'href="../index.html"' not in text:
            errors.append(f"missing ../index.html return link: {rel}")
        if re.search(r"[A-Za-z]:\\|file://", text):
            errors.append(f"local absolute path found: {rel}")
        for link in LINK_RE.findall(text):
            if link.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = (report.parent / link.split("#", 1)[0]).resolve()
            if link and not target.exists():
                errors.append(f"broken local link in {rel}: {link}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validation passed: {len(reports)} reports")
    return 0


if __name__ == "__main__":
    sys.exit(main())
