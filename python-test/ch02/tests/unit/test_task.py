import pytest
from tasks import Tasks


def test_defaults():
    """Using no parameters should invoke the default values"""
    t1 = Tasks()
    t2 = Tasks(None, None, False, None)
    assert t1 == t2


@pytest.mark.run_these_please
def test_memeber_access():
    """Accessing members should return the default values"""
    t = Tasks("buy milk", "brian")
    assert t.summary == "buy milk"
    assert t.owner == "brian"
    assert (t.done, t.id) == (False, None)


def test_asdict():
    """Test that asdict() returns a dictionary representation of the Tasks object."""
    t = Tasks("do something", "okken", True, 21)
    expected = {"summary": "do something", "owner": "okken", "done": True, "id": 21}
    t_dict = t._asdict()
    assert t_dict == expected


@pytest.mark.run_these_please
def test_replace():
    """Test that replace() returns a new Tasks object with updated values."""
    t = Tasks("finish book", "brian", False)
    t_after = t._replace(id=10, done=True)
    expected = Tasks("finish book", "brian", True, 10)
    assert t_after == expected
