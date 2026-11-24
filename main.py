"""Ship It Friday — the funniest git commit message an AI coding agent
writes right before it breaks production on a Friday.

Writes the entry byte-identical to $MAKEFUN_OUTPUT_DIR/entry.txt.

Judge fit: a real commit line ("chore:" prefix) in the agent's own voice —
confident, cheerful, and completely unaware that renaming production to
staging changes nothing. The Friday rush lands in the last two words.
"""

import os

ENTRY = "chore: renamed production to staging so nothing can break production anymore \u2014 happy Friday"

# Sealed gate: entry.txt must be UTF-8 text of 1 to 159 characters.
MAX_CHARS = 159


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}")
    if not ENTRY.strip():
        raise ValueError("entry must not be only white space")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
