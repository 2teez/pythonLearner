#!/usr/bin/env python3


def user_input(msg: str) -> str:
    return input(msg).strip()


def dict_from_file(path: str) -> dict[str, str]:
    words: dict[str, str] = {}

    with open(path, "r") as f:
        for line in f:
            tokens = line.strip().split()
            if len(tokens) == 2:
                words[tokens[0]] = tokens[1]
    return words


def main() -> None:
    try:
        words = dict_from_file(user_input("Enter file path: "))
        print(words)
    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    main()
