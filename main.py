#!/usr/bin/env python3
"""The Robot Apology — a two-line robot confession.

Writes the entry text to /output/entry.txt:
  line 1 — the robot owns one specific mistake;
  line 2 — what it learned and what it will do differently.
"""

import os

ENTRY = (
    "I watered the plastic fern on Mrs. Alvarez's balcony for eleven days, proud of how green it stayed.\n"
    "Now I read the tag before I lift the can, because tending something starts with knowing whether it is alive.\n"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
