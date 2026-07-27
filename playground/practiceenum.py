#!/usr/bin/env python3

import enum


class Weekday(enum.Enum):
    """
    Represents a weekday.
    """

    Monday = enum.auto()
    Tuesday = enum.auto()
    Wednesday = enum.auto()
    Thursday = enum.auto()
    Friday = enum.auto()
    Saturday = enum.auto()
    Sunday = enum.auto()

    """
    Returns the name of the weekday.
    """

    def __str__(self) -> str:
        return self.name


class TrafficLight(enum.Flag):
    """
    Represents a traffic light state.
    """

    RED = enum.auto()
    YELLOW = enum.auto()
    GREEN = enum.auto()


def main() -> None:
    for day in Weekday:
        print(day)

    for light in TrafficLight:
        print(light)

    combined_state = TrafficLight.RED | TrafficLight.GREEN
    print(combined_state)
    print(TrafficLight.RED & TrafficLight.YELLOW)


if __name__ == "__main__":
    main()
