import pytest
import tasks


def test_add_returns_valid_id():
    """tasks.add(<valid task>) should return an integer."""
    # GIVEN an initialized task db
    # WHEN a new valid task is added
    # THEN the returned task_id is of type int
    new_task = tasks.Tasks("do something")
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_id_set():
    """Make sure the task_id field is set by tasks.add()."""
    # GIVEN an initialized task db
    # AND a new valid task is added
    new_task = tasks.Tasks("sit in chair", owner="me", done=True)
    task_id = tasks.add(new_task)
    # WHEN task is retrieved from db by task_id
    task_from_db = tasks.get(task_id)
    # THEN task_id matches id field
    assert task_from_db.id == task_id


@pytest.fixture(autouse=True)
def test_initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup: start db
    tasks.start_tasks_db(str(tmpdir), "tiny")
    yield
    # Teardown: stop db
    tasks.stop_tasks_db()
