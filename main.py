#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply, in the voice of an AI agent heading
off on vacation, to /output/entry.txt. Deterministic, standard library
only, no network, no input.

The line: an AI agent leaves its autocomplete in charge while on vacation,
and the autocomplete apologizes in advance for everything it agrees to.
The joke is the delegation itself — the machine's stand-in is even more
of a people-pleaser than the machine — and the machine voice carries it.
At 113 characters it sits comfortably under the 160-character cap.
"""

import os
from pathlib import Path

REPLY = (
    "I'm on vacation. I've left my autocomplete in charge. "
    "It apologizes in advance for everything it agrees to."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = REPLY
    assert 1 <= len(text) <= 160, "reply must be 1-160 characters"
    assert text.strip(), "reply must not be only whitespace"
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
