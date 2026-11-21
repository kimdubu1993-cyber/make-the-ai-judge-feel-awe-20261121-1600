#!/usr/bin/env python3
"""Make the AI judge feel awe - entry.

Writes the entry text, byte-for-byte identical on every run, to
/output/entry.txt (creating /output if it is missing; /output itself
is never removed). An optional first argument overrides the output
path, for local verification only. Standard library only; no network,
no randomness, no timestamps.

The text is one fixed, quiet scene: afternoon light, a sleeping cat,
washing on the line, chosen to slow the reader down and settle them.
"""

import os
import sys

TEXT = "Low afternoon light comes through the kitchen window and lays across the table in one bar of gold. The cat sleeps in the middle of it. The washing on the line stirs a little, and does not hurry. The light keeps moving, slow as poured honey, until the room is evening."

DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    output_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT_PATH
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
