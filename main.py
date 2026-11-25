#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes a one-line office joke — the Monday meeting that should have
been an email — to /output/entry.txt,
one line, no trailing newline.
"""

import os

ENTRY = "Our Monday meeting could have been an email, but the printer ate that too."


def main():
    line = ENTRY.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
