"""Write one hilarious autocorrect-fail line to the output file.

Entry for make.fun's "Funniest Autocorrect Fail" bounty
(u-zeroxfive-funniest-autocorrect-fail-ddf82154).

The program writes a single line of plain text to entry.txt in the
output directory (MAKEFUN_OUTPUT_DIR when set, else /output).
Standard library only, deterministic: the same bytes every run.
"""

import os

ENTRY = "I have an intercourse at 3pm tomorrow, wish me luck! It's my dream job."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the line, no trailing newline: the file's contents
    # are the entry, and the gate counts its characters (1-199).
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify the bytes landed exactly as intended before exiting.
    with open(path, encoding="utf-8", newline="") as f:
        assert f.read() == ENTRY, "entry.txt does not match the entry"


if __name__ == "__main__":
    main()
