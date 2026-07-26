#!/usr/bin/env python3

import collections


def main() -> None:
    # using namedtuples
    Person = collections.namedtuple("Person", ["name", "age", "friends"])
    java = Person(name="Java", age=30, friends=["clojure", "groovy", "scala", "kotlin"])
    print(
        f"{java.name}, has {len(java.friends)} number of friends. Namely {', '.join(sorted(java.friends))}"
    )


if __name__ == "__main__":
    main()
