#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — make.fun bounty entry.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output):
the note a smart fridge leaves on its door screen for its owner.

The line is fixed and deterministic: the program takes no input, reads
nothing from the network or disk, and always emits the same bytes.

Why this line: the fridge is a witness, not a nag. The owner hid the
pickles behind the milk so the roommate would not find them, and the
fridge — which sees everything on its shelves — undid the hiding and
refuses to be part of it. The turn lands in the last sentence: the
appliance has a conscience, and it is not on the owner's side. The
note is petty, domestic, and specific, and it trusts the reader to
get the joke without any explanation attached.
"""

import os
import sys

ENTRY = (
    "You hid the pickles behind the milk so your roommate wouldn't "
    "find them. I moved them back. I am not your accomplice."
)

MAX_CHARS = 200


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    if not ENTRY or not ENTRY.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(ENTRY) > MAX_CHARS:
        print(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1
    ENTRY.encode("utf-8")  # raises if not valid UTF-8

    path = output_path()
    payload = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(payload)
    with open(path, "rb") as f:
        if f.read() != payload:
            print("round-trip mismatch", file=sys.stderr)
            return 1
    os.chmod(path, 0o644)
    print(f"wrote {len(ENTRY)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
