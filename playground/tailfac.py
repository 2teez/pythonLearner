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


def fib(n: int) -> int:
    nums = [0, 1]
    for i in range(2, n + 1):
        nums.append(nums[i - 1] + nums[i - 2])
    return nums[n]


def from_user(prompt: str) -> str:
    return input(prompt).strip()


def get_number(user_input: str) -> int:
    return int(user_input)


def main() -> None:
    while True:
        try:
            input = get_number(from_user("Enter a number:"))
            print(tail_fac(input))
            if input == 0:
                break
        except ValueError:
            print("Invalid input. Please enter a number. Enter 0 to exit.")

    factorial_func = lambda x, f: f(x)
    result = factorial_func(56, fac)
    print(result)
    #
    # fibonacci
    print(fib(560))


if __name__ == "__main__":
    main()
