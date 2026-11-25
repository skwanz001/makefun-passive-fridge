"""Passive-aggressive fridge note writer.

Writes one single-line note from a smart fridge to /output/entry.txt.
Standard library only: the grading sandbox installs nothing.
"""

import os
from pathlib import Path

NOTE = "Inventory update: the yogurt expired Tuesday. You ate it Wednesday. I have filed this under 'evidence'."


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(NOTE, encoding="utf-8")


if __name__ == "__main__":
    main()
