import pytest


@pytest.fixture()
def some_data():
    """Return answer to ultimate question"""
    return 42


@pytest.fixture()
def some_other_data():
    """Raise an exception from fixture"""
    x = 43
    assert x == 42


def test_some_data(some_data):
    """Use fixture return value in a test"""
    assert some_data == 42


@pytest.fixture()
def a_tuple():
    """Return a tuple"""
    return (1, "foo", None, {"bar": 23})


@pytest.mark.xfail(reason="32 is not equal to 23")
def test_a_tuple(a_tuple):
    """Use fixture return value in a test"""
    assert a_tuple[3]["bar"] == 32
