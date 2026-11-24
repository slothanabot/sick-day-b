"""sick-day-B — make.fun entry for "The Funniest Sick-Day Excuse".

Writes one original one-line sick-day excuse to /output/entry.txt.

The excuse: my alarm clock quit with no notice, so nobody in the house
knows what time it is anymore — and I'm taking the day off to grieve.
Fresh idea (no fever, no dog, no dead grandmother), half-believable in
the way a text to your boss is, with the punch landing on the last word.
"""

ENTRY = (
    "Can't come in today \u2014 my alarm clock quit this morning with no "
    "notice, so nobody in this house knows what time it is anymore, and "
    "I'm taking the day off to grieve."
)


MAX_CHARS = 200
MIN_CHARS = 1
OUTPUT_PATH = "/output/entry.txt"


def verify(text):
    """Enforce the gate from RULES.txt: 1-200 chars, non-blank, one line."""
    if not isinstance(text, str):
        raise TypeError("entry must be str")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry is %d chars, must be %d-%d" % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def main():
    verify(ENTRY)
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %d chars to %s" % (len(ENTRY), OUTPUT_PATH))


if __name__ == "__main__":
    main()
