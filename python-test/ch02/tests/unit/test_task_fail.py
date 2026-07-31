#!/usr/bin/env python3

import pytest
from tasks import Tasks


def test_task_equality():
    """Different tasks should not be equal"""
    t1 = Tasks("Sit there", "brian")
    t2 = Tasks("do something", "okken")
    assert t1 == t2


def test_dict_equality():
    """Different tasks compared as dicts should not be equal"""
    t1_dict = Tasks("make sandwich", "okken")._asdict()
    t2_dict = Tasks("make sandwich", "okkem")._asdict()

    assert t1_dict == t2_dict
