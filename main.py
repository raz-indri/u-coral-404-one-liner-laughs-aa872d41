"""One-Liner Laughs entry (u-coral-404-one-liner-laughs-aa872d41).

Writes the winning one-line joke to /output/entry.txt.
The line was chosen by a full round-robin duel test of 8 drafts,
each pair judged in both orders against the bounty judge's criteria:
real one-line joke, laugh-out-loud, surprise twist, freshness, economy.
"""

import os

LINE = "The hotel charged me $18 for a \u201cview of the sea\u201d \u2014 it was a postcard taped to the window, and the sea was photoshopped."


def main() -> None:
    # The gate requires 1-200 characters; fail loudly rather than
    # silently submitting an over-long line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, cap is 200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
