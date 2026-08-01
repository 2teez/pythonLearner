import pytest
import tasks


@pytest.mark.xfail(
    tasks.__version__ < "0.2.0",
    reason="not supported until version 0.2.0",
)
def test_unique_id():
    """Calling unique_id() twice should return different numbers"""
    id1 = tasks.unique_id()
    id2 = tasks.unique_id()
    assert id1 != id2


@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    """Demostrates xfail"""
    uid = tasks.unique_id()
    assert uid == "a duck"


@pytest.mark.xfail()
def test_unique_id_not_a_duck():
    """Demostrates xpass."""
    uid = tasks.unique_id()
    assert uid != "a duck"
