#!/usr/bin/env python3
#
from time import sleep, time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Time taken: for the function {func.__name__} is {end - start}")
        return result

    return wrapper


@timeit
def helloworld() -> None:
    print("Hello World!")
    sleep(1)


@timeit
def main() -> None:
    sleep(2)
    helloworld()


if __name__ == "__main__":
    main()
