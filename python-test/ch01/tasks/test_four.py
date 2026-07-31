#!/usr/bin/env python3

from collections import namedtuple

Tasks = namedtuple("Tasks", ["summary", "owner", "done", "id"])
Tasks.__new__.__defaults__ = (None, None, False, None)


def test_asdict():
    """Test that asdict() returns a dictionary representation of the Tasks object."""
    t = Tasks("do something", "okken", True, 21)
    expected = {"summary": "do something", "owner": "okken", "done": True, "id": 21}
    t_dict = t._asdict()
    assert t_dict == expected


def test_replace():
    """Test that replace() returns a new Tasks object with updated values."""
    t = Tasks("finish book", "brian", False)
    t_after = t._replace(id=10, done=True)
    expected = Tasks("finish book", "brian", True, 10)
    assert t_after == expected
