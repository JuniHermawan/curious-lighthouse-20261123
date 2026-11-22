"""Make the AI judge feel curious.

Writes one short intriguing text to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Deterministic, no network.
"""

import os

TEXT = (
    "Every night at 3 a.m. the lighthouse log gains one new word. Read in "
    "order, the words form a sentence no keeper has ever finished \u2014 "
    "because the last page is still blank, and tonight it is your turn to write."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to {path}")


if __name__ == "__main__":
    main()
