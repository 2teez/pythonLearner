#!/usr/bin/env python3

from collections import namedtuple

Tasks = namedtuple("Tasks", ["summary", "owner", "done", "id"])
Tasks.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    """Using no parameters should invoke the default values"""
    t1 = Tasks()
    t2 = Tasks(None, None, False, None)
    assert t1 == t2


def test_memeber_access():
    """Accessing members should return the default values"""
    t = Tasks("buy milk", "brian")
    assert t.summary == "buy milk"
    assert t.owner == "brian"
    assert (t.done, t.id) == (False, None)
