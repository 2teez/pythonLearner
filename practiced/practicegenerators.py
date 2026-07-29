#!/usr/bin/env python3


def square_generator(n: int = 5, /, *, start: int = 1, status: bool = False):
    if status and start == 1:
        print(f"Generating squares for the first {n} numbers")
    elif status and start != 1:
        print(f"Generating squares for the first {n} numbers starting from {start}")
    for i in range(start, n + 1):
        yield i**2


def main() -> None:
    print(list(square_generator()))
    print(list(square_generator(34, status=True)))
    print(list(square_generator(67, status=True, start=15)))


if __name__ == "__main__":
    main()
