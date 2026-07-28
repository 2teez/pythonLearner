#!/usr/bin/env python3

"""
Function for calculating factorial using recursion.
>> fac(5)
120
"""


def fac(n: int) -> int:
    if n <= 0:
        return 1
    else:
        return n * fac(n - 1)


"""
Function for calculating factorial using tail recursion.
>> tail_fac(5)
120
"""


def tail_fac(n: int) -> int:
    def helper(n: int, acc: int) -> int:
        if n == 0:
            return acc
        return helper(n - 1, acc * n)

    return helper(n, 1)


def from_user(prompt: str) -> str:
    return input(prompt).strip()


def get_number(user_input: str) -> int:
    return int(user_input)


def main() -> None:
    while True:
        try:
            input = get_number(from_user("Enter a number:"))
            print(tail_fac(input))
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
