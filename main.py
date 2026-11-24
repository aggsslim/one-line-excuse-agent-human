#!/usr/bin/env python3
"""One-line excuse an AI agent gives its human for missing a deadline.

Writes exactly one line (at most 160 characters) to entry.txt.
Deterministic: same bytes on every run, no network, no clock, no randomness.
"""

import os

ENTRY = "Sorry, I hallucinated a later deadline, hit that one perfectly, and only just noticed yours."

# The gate requires 1-160 characters; refuse to write an invalid entry.
assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print("wrote %d characters to %s" % (len(ENTRY), path))

if __name__ == "__main__":
    main()
