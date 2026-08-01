import pytest
import tasks


def test_and_raises():
    """add() should raise an exception with wrong type parameters"""
    with pytest.raises(TypeError):
        tasks.add(task="not a Task object")


def test_start_task_db_raises():
    """Make sure unsupported db raises an exception"""
    with pytest.raises(ValueError) as ecinfo:
        tasks.start_tasks_db("some/great/path", "mysql")
    assert ecinfo.value.args[0] == "db_type must be 'tiny' or 'mongo'"


@pytest.mark.smoke
def test_list_raises():
    """list() should raise an exception with wrong type param"""
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """Make sure get() raises an exception with invalid task_id"""
    with pytest.raises(TypeError):
        tasks.get(tasks_id="123")
