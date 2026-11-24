#!/usr/bin/env python3
"""wonder-line-b: one sentence of everyday wonder.

Writes a single fixed sentence to /output/entry.txt. The text is a
constant: no randomness, no time, no network, no input files. Two runs
produce byte-identical output.
"""

import os

ENTRY = (
    "The kettle whistles like a tiny train leaving the station, "
    "and every morning I stand ticketless on my kitchen platform, "
    "waving goodbye to the steam."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
