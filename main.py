"""How many tabs do you have open? — make.fun entry (program/v1).

Writes a single number — the count of open browser tabs — to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The number is 365: one tab for every day of the year. It is the count
this entry answers with — a year of tabs opened and never closed.
Deterministic: no network, no randomness, no input, no dependencies
beyond the Python 3.13 standard library.
"""

import os

COUNT = 365


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(str(COUNT))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
