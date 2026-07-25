#!/usr/bin/env python3

from pathlib import Path


def user_input(msg: str) -> str:
    return input(msg).strip()


def dict_from_file(path: Path) -> dict[str, str]:
    words: dict[str, str] = {}

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            tokens = line.strip().split()
            if len(tokens) == 2:
                words[tokens[0]] = tokens[1]
    return words


def main() -> None:
    try:
        words = dict_from_file(Path(user_input("Enter file path: ")))
        print(words)
    except FileNotFoundError as e:
        print(f"File not found: {e}")


if __name__ == "__main__":
    main()
