import pytest
import tasks
from tasks import Task


def test_add_returns_valid_id(tasks_db):
    """tasks.add(<valid task>) should return an integer."""
    # GIVEN an initialized task db
    # WHEN a new valid task is added
    # THEN the returned task_id is of type int
    new_task = Task("do something")
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


@pytest.mark.skip(reason="to be attended to latter")
def test_added_task_has_id_set(tasks_db):
    """Make sure the task_id field is set by tasks.add()."""
    # GIVEN an initialized task db
    # AND a new valid task is added
    new_task = Task("sit in chair", owner="me", done=True)
    task_id = tasks.add(new_task)
    # WHEN task is retrieved from db by task_id
    task_from_db = tasks.get(task_id)
    # THEN task_id matches id field
    assert task_from_db.id == task_id
