#!/usr/bin/env python3

import random
import time


def with_timing(fn):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            end = time.perf_counter()
            print(f"{fn.__name__} Time taken: {end - start:.2f} seconds")

    return wrapper


@with_timing
def napper() -> None:
    time.sleep(random.randint(1, 5))


@with_timing
def sleeper() -> None:
    time.sleep(2)


@with_timing
def main() -> None:
    print("Start Here!")
    sleeper()
    napper()


if __name__ == "__main__":
    main()
