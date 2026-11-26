#!/usr/bin/env python3
"""Write the cat's defence to /output/entry.txt.

Entry for the make.fun bounty "Five Seconds to Explain the Glass":
the one sentence a house cat would say in its own defence, in the five
seconds after knocking a glass off the table. No apology, no confession.
"""

import os

ENTRY = "I gave the glass five seconds to move and it chose the floor."

# The line is a fixed string: no input, no randomness, no time or
# environment dependence, so every run writes exactly the same bytes.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
