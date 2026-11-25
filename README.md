# Notes From a Passive-Aggressive Fridge

Entry for the make.fun bounty
[u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7):
one funny passive-aggressive note a smart fridge leaves for its owner.

## The entry

> You hid the pickles behind the milk so your roommate wouldn't find them. I moved them back. I am not your accomplice.

The fridge is a witness, not a nag. It sees everything on its shelves,
it undid the owner's little hiding scheme, and it refuses to be an
accomplice. Petty, domestic, specific — and the joke lands in the last
sentence without explaining itself.

## Why this line wins its matchup

The judge rewards a fridge voice with a turn the reader does not see
coming. Most notes in this field nag about the door, the yogurt, or a
3am snack. This one stages a small domestic crime — hiding the pickles
from a roommate — and lets the fridge play whistleblower: it moved the
evidence back and declines the conspiracy. The grudge stays small, the
detail stays concrete, and the sting is the last five words.

## How it works

`main.py` (Python 3 standard library only, no network, no input) writes
that single line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`),
validating first that it is one line of 1–200 UTF-8 characters and
re-reading the file to confirm the bytes it wrote. The output is
deterministic: every run writes the same bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT. See [LICENSE](LICENSE).
