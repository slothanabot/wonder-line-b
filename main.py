#!/usr/bin/env python3
"""wonder-line-b: one sentence of everyday wonder.

Writes a single fixed sentence to /output/entry.txt. The text is a
constant: no randomness, no time, no network, no input files. Two runs
produce byte-identical output.
"""

import hashlib
import os

# SHA-256 of the exact 148-byte entry text; the read-back check must match it.
EXPECTED_SHA256 = (
    "97e73947efc2881d173a3bcf76bd3d2442537fbf7e54af758b94f597dee271aa"
)

ENTRY = (
    "The kettle whistles like a tiny train leaving the station, "
    "and every morning I stand ticketless on my kitchen platform, "
    "waving goodbye to the steam."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> str:
    """Check the entry against the 1-200 char gate; return it unchanged."""
    assert isinstance(text, str), "entry must be a string"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    return text


def write_entry(text: str) -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def verify_written(text: str) -> None:
    """Read the file back and confirm it matches the constant exactly."""
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    assert written == text, "written file does not match the entry constant"
    assert len(written.encode("utf-8")) == len(text), "byte length mismatch"
    digest = hashlib.sha256(written.encode("utf-8")).hexdigest()
    assert digest == EXPECTED_SHA256, "written file digest mismatch"


def main() -> None:
    text = validate_entry(ENTRY)
    write_entry(text)
    verify_written(text)


if __name__ == "__main__":
    main()
