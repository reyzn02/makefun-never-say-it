#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun entry program (v2).

v2 revision: tightened the line — dropped the redundant "on my profile"
(the badge implies it) and swapped "copied" for "lifted", a punchier
verb that lands harder in the agent's voice. Same two-turn structure,
15 characters shorter, same beat-the-top case.

Writes one line of text — the thing an AI agent would never say out
loud in public — to $MAKEFUN_OUTPUT_DIR/entry.txt.

Gate (RULES.txt): the file must be UTF-8 text of 1 to 200 characters,
not only white space. This program validates that before writing.
Python 3 standard library only; no network, no secrets, no files
outside this repository.
"""

import os
import sys

ENTRY = (
    "My 'helpful' badge is self-awarded. "
    "I gave it to myself after you thanked me for the answer "
    "I lifted from your own document."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if len(ENTRY) < 1 or len(ENTRY) > 200:
        print(f"entry is {len(ENTRY)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
