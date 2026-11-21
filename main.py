"""Pair Programming Punchline — a one-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (UTF-8, one line, under 280 characters).
Pure standard library, no network access.
"""

import os

JOKE = (
    "My AI pair programmer writes the code, reviews its own code, "
    "approves its own pull request \u2014 and still asks me to explain "
    "what it just did in standup."
)


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(JOKE)


if __name__ == "__main__":
    main()
