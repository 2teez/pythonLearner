#!/usr/bin/env python3

from math import isqrt


class GeneratePrimeNumbers:
    def __init__(self, number_of: int = 2, /):
        self.number_of = number_of
        self.prime_number = 2
        self.counter = 0

    def __iter__(self):
        return self

    @staticmethod
    def _is_prime_number(n: int) -> bool:
        if n < 2:
            return False
        for divisor in range(2, isqrt(n) + 1):
            if n % divisor == 0:
                return False
        return True

    def __next__(self):
        while True:
            if self._is_prime_number(self.prime_number):
                self.counter += 1

                if self.counter > self.number_of:
                    raise StopIteration

                result = self.prime_number
                self.prime_number += 1
                return result

            self.prime_number += 1


def main() -> None:
    print(list(GeneratePrimeNumbers(500)))


if __name__ == "__main__":
    main()
