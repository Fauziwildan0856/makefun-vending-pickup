#!/usr/bin/env python3
"""Vending machine pickup line entry for make.fun.

Writes one pickup line, spoken by a vending machine to a passing human,
to MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the variable
is unset). The line is validated against the kit gate before it is
written: UTF-8 text, 1-200 characters, not only whitespace, exactly
one line. Standard library only, deterministic output.
"""

import os
import sys

ENTRY = (
    "Hey gorgeous \u2014 I've been humming all day, my coils are spinning, "
    "and every snack in here is jealous. Press B7... that's me."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Check the line against the kit gate; raise ValueError on failure."""
    if not line:
        raise ValueError("entry is empty")
    if not line.strip():
        raise ValueError("entry is only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character limit"
            % (len(line), MAX_CHARS)
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Read-back check: what landed on disk must be exactly the validated line.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: entry.txt does not match ENTRY")
    print("Wrote %d characters to %s" % (len(ENTRY), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
