#!/usr/bin/env python3

from datetime import date

from person import Person


def main() -> None:
    java = Person("Java", "Gosling", date(1995, 5, 23))
    print(java)


if __name__ == "__main__":
    main()
