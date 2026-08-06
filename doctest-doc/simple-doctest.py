#!/usr/bin/env python3
"""
This module provides a simple factorial function.
>>> fac(0)
1
>>> fac(5)
120
"""


def fac(n: int) -> int:
    """
    Returns the factorial of n.
    >>> [fac(num) for num in range(6)]
    [1, 1, 2, 6, 24, 120]
    """
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)


def main() -> None:
    """
    Entry point of the program.
    """
    result = fac(5)
    print(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
