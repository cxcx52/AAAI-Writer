#!/usr/bin/env python3
"""Audit AAAI draft text for defensive style, AI-smell, and weak claim markers."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PATTERNS = {
    "defensive_contrast": re.compile(
        r"\bnot only\b|\bnot\b[^.\n]{0,120}\bbut\b|\brather than\b|\binstead of\b|\bless\b[^.\n]{0,80}\bthan\b|不是[^。\n]{0,80}而是",
        re.IGNORECASE,
    ),
    "scope_apology": re.compile(
        r"\bnot a claim\b|\bdoes not claim\b|\bdo not claim\b|\bnot to defend\b|\bnot a general\b|\bnot exhaustive\b|\bonly conditional\b|\bscope boundary\b",
        re.IGNORECASE,
    ),
    "generic_hype": re.compile(
        r"\bnovel\b|\bsignificant(?:ly)?\b|\bsubstantial(?:ly)?\b|\bcomprehensive\b|\brobust\b|\bpowerful\b|\bpromising\b|\bstate-of-the-art\b|\bextensive experiments\b|\bgroundbreaking\b|\bpivotal\b|\bholistic\b|\bseamless\b",
        re.IGNORECASE,
    ),
    "throat_clearing": re.compile(
        r"\bIn this paper, we\b|\bIn this section, we\b|\bIt is worth noting that\b|\bIt should be noted that\b|\bNotably\b|\bImportantly\b|\bFurthermore\b|\bMoreover\b|\bAdditionally\b",
        re.IGNORECASE,
    ),
    "weak_mechanism": re.compile(
        r"\bplays? an important role\b|\bis challenging\b|\bis difficult\b|\bcan potentially\b|\bmay help\b|\bleverage\b|\butilize\b|\bserves as\b|\bstands as\b|\bfeatures\b|\bshowcases\b",
        re.IGNORECASE,
    ),
    "formulaic_opening": re.compile(
        r"\bIn recent years\b|\bWith the rapid development of\b|\bDespite recent advances\b|\bRecent advances in\b|\bAs .* become(?:s)? increasingly\b",
        re.IGNORECASE,
    ),
    "ai_vocabulary": re.compile(
        r"\bdelve\b|\bdives? into\b|\bunderscore(?:s|d)?\b|\bintricate\b|\btapestry\b|\blandscape\b|\bparadigm\b|\bfoster(?:s|ing)?\b|\bempower(?:s|ing)?\b|\bplethora\b|\bmyriad\b|\bcrucial\b|\bkey\b",
        re.IGNORECASE,
    ),
}

TEXT_EXTENSIONS = {".tex", ".txt", ".md"}


def iter_files(path: Path):
    if path.is_file():
        if path.suffix.lower() in TEXT_EXTENSIONS:
            yield path
        return
    for child in path.rglob("*"):
        if child.is_file() and child.suffix.lower() in TEXT_EXTENSIONS:
            parts = {p.lower() for p in child.parts}
            if ".git" not in parts and "build" not in parts:
                yield child


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def clean_snippet(text: str, start: int, end: int) -> str:
    left = max(0, start - 80)
    right = min(len(text), end + 120)
    snippet = re.sub(r"\s+", " ", text[left:right]).strip()
    return snippet


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="A .tex/.txt/.md file or a directory to audit")
    parser.add_argument("--max-snippets", type=int, default=12)
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.exists():
        print(f"ERROR: path does not exist: {root}")
        return 2

    totals = {name: 0 for name in PATTERNS}
    snippets: list[tuple[str, str, int, str]] = []
    files = list(iter_files(root))

    for file_path in files:
        try:
            text = file_path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            print(f"WARN: could not read {file_path}: {exc}")
            continue
        for name, pattern in PATTERNS.items():
            matches = list(pattern.finditer(text))
            totals[name] += len(matches)
            for match in matches[: args.max_snippets]:
                snippets.append(
                    (
                        name,
                        str(file_path),
                        line_number(text, match.start()),
                        clean_snippet(text, match.start(), match.end()),
                    )
                )

    print(f"Audited files: {len(files)}")
    print("")
    print("| Pattern | Count |")
    print("|---|---:|")
    for name, count in totals.items():
        print(f"| {name} | {count} |")

    print("")
    print("Top snippets:")
    for name, file_path, line_no, snippet in snippets[: args.max_snippets]:
        print(f"- [{name}] {file_path}:{line_no}: {snippet}")

    risk = "low"
    if totals["defensive_contrast"] >= 8 or totals["scope_apology"] >= 4:
        risk = "high"
    elif totals["defensive_contrast"] >= 4 or totals["scope_apology"] >= 2:
        risk = "medium"

    print("")
    print(f"Defensive-style risk: {risk}")
    return 1 if risk == "high" else 0


if __name__ == "__main__":
    raise SystemExit(main())
