"""The 3AM Fridge Text — make.fun entry.

Writes one text message (at most 140 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt):
the message a smart fridge sends its owner at 3am.

Pure standard library only.
"""

import os

MESSAGE = (
    "3am. The smart home asked me to check on you. I told it you're fine. "
    "You're standing here in your underwear eating butter."
)

MAX_CHARS = 140


def validate(text):
    """Enforce the RULES.txt gate: UTF-8, 1-140 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 140-char limit" % len(text))
    text.encode("utf-8")
    return text


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry = validate(MESSAGE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry)
    # Read back and re-validate what actually landed on disk.
    with open(path, "r", encoding="utf-8") as fh:
        on_disk = validate(fh.read())
    assert on_disk == entry, "entry.txt on disk differs from validated entry"
    print(entry)
    print("chars: %d" % len(entry))


if __name__ == "__main__":
    main()
