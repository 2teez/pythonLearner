#!/usr/bin/env python3

import datetime
from datetime import date


class Person:
    def __init__(self, first_name: str, last_name: str, age: date) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        today = datetime.datetime.now(tz=datetime.timezone.utc).date()
        age = today.year - self.age.year
        return f"{self.first_name} {self.last_name} ({age})"

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        self._first_name = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        self._last_name = value

    @property
    def age(self) -> date:
        return self._age

    @age.setter
    def age(self, value: date) -> None:
        self._age = value
