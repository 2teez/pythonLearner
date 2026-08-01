import pytest
import tasks


@pytest.mark.skipif(
    tasks.__version__ < "0.2.0",
    reason="misunderstood the API, and not supported until version 0.2.0",
)
def test_unique_id():
    """Calling unique_id() twice should return different numbers"""
    id1 = tasks.unique_id()
    id2 = tasks.unique_id()
    assert id1 != id2


def test_unique_id_2():
    """unique_id() should return an unused id."""
    ids = []
    ids.append(tasks.add(tasks.Tasks("one")))
    ids.append(tasks.add(tasks.Tasks("two")))
    ids.append(tasks.add(tasks.Tasks("three")))

    uid = tasks.unique_id()
    assert uid not in ids
