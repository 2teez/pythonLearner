#!/usr/bin/env python3
#
from collections import namedtuple
from dataclasses import dataclass


@dataclass
class DataClassAddress:
    number: int
    street: str
    city: str
    state: str
    zip: str


def main() -> None:
    Address = namedtuple("Address", ["number", "street", "city", "state", "zip"])
    # Create an Address instance using keyword arguments
    # like so: address = Address(123, "Main St", "Anytown", "CA", "12345")
    address = Address(
        number=123, street="Main St", city="Anytown", state="CA", zip="12345"
    )
    print(address)
    dc_address = DataClassAddress(
        number=123, street="Main St", city="Anytown", state="CA", zip="12345"
    )
    print(dc_address)


if __name__ == "__main__":
    main()
