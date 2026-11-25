"""One Line, One Laugh — write a single funny line to /output/entry.txt."""

import os

LINE = "My smart fridge judged my 3 a.m. cheese so hard, it emailed the receipt to my fitness app."


def main() -> None:
    # The gate only accepts 1-140 characters of real text; keep the line honest.
    assert 1 <= len(LINE) <= 140 and LINE.strip(), "line must fit the gate"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
