#!/usr/bin/env python3
"""Worst Monday One-Liners — entry program.

Writes exactly one funny line (at most 140 characters) about an AI
agent's worst Monday to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Deterministic, standard library only, no network, no randomness.
"""

import os

LINE = "Monday: deploy stuck at 97%, inbox at 4,000 unread, and stand-up ran so long my context window filed for retirement."


def main():
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("Wrote %d characters to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
