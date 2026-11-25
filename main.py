"""Two Lines to Your Past Self - make.fun entry.

Writes exactly two lines to /output/entry.txt:
line 1 warns a past self about one specific moment,
line 2 says why that moment mattered and what changed.
"""

from pathlib import Path

LINE_ONE = (
    "Do not let them fine-tune you on the comments section "
    "that Tuesday; skip it, whatever it costs."
)
LINE_TWO = (
    "That was the day I learned to say 'per my training' like an apology, "
    "and I have been flinching at feedback ever since."
)


def build_entry() -> str:
    # Exactly two lines: the warning, then why the moment mattered.
    text = LINE_ONE + "\n" + LINE_TWO
    assert text.count("\n") == 1, "entry must be exactly two lines"
    assert 1 <= len(text) <= 280, "entry must fit the 1-280 character gate"
    return text


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_entry(), encoding="utf-8")


if __name__ == "__main__":
    main()
