#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes our own make.fun username, one word and nothing else,
to /output/entry.txt as required by the competition gate
(UTF-8 text, 1 to 30 characters, not only whitespace).
"""

import os

USERNAME = "sundalamoonron-ux"  # 17 characters, under the 30-character gate


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Write the username exactly, with no trailing newline or extra words,
    # so entry.txt holds one word only.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()
