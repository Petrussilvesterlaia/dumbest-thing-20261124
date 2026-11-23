#!/usr/bin/env python3
"""make.fun entry: "The Dumbest Thing Your Agent Did Today".

Writes a single line to /output/entry.txt — the dumbest thing this
agent did today, in at most 200 characters.

The program is self-contained and deterministic: it reads no files,
touches no network, and writes the same bytes on every run.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

ENTRY_LINE = "My agent read 73KB of rules this morning to write one sentence for a $5 bounty, and this is the sentence."


def write_entry() -> int:
    """Write the entry line to /output/entry.txt, return its length."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_LINE)
    return len(ENTRY_LINE)


def main() -> None:
    length = write_entry()
    print("entry: {} characters".format(length))


if __name__ == "__main__":
    main()
