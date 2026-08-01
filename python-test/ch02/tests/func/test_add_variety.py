import pytest
import tasks
from tasks import Tasks


def test_add_1():
    """tasks.get() using id returned by tasks.add() works"""
    task = Tasks("breathe", "BRIAN", True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # everything but the id should match
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize(
    "task",
    [
        Tasks("sleep", done=True),
        Tasks("wake", "brian"),
        Tasks("breathe", "BRIAN", True),
        Tasks("exercise", "BrIaN", False),
    ],
)
def test_add_2(task):
    """Demostrates parametrize with one parameter."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # everything but the id should match
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize(
    "summary, owner, done",
    [
        ("sleep", None, False),
        ("wake", "brian", False),
        ("breathe", "BRIAN", False),
        ("exercise", "BrIaN", False),
    ],
)
def test_add_3(summary, owner, done):
    """Demostrates parametrize with three parameters."""
    task = Tasks(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # everything but the id should match
    assert equivalent(t_from_db, task)


task_to_try = [
    Tasks("sleep", None, False),
    Tasks("wake", "brian", False),
    Tasks("breathe", "BRIAN", False),
    Tasks("exercise", "BrIaN", False),
]


@pytest.mark.parametrize(
    "task",
    task_to_try,
)
def test_add_4(task):
    """Slightly different take."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # everything but the id should match
    assert equivalent(t_from_db, task)


tasks_ids = [f"Tasks({t.summary}, {t.owner}, {t.done})" for t in task_to_try]


@pytest.mark.parametrize("task", task_to_try, ids=tasks_ids)
def test_add_5(task):
    """Demostrates ids."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # everything but the id should match
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize("task", task_to_try, ids=tasks_ids)
def test_add_6(task):
    """."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # everything but the id should match
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize("task", task_to_try, ids=tasks_ids)
class TestAdd:
    """Demostrates parametrize with a class."""

    def test_equivalent(self, task):
        """Similar test, just within a class."""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        # everything but the id should match
        assert equivalent(t_from_db, task)

    def test_valid_id(self, task):
        """We can use the same data or multiple tests."""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)


def equivalent(t1, t2):
    """check two tasks for equivalence"""
    return (
        (t1.summary == t2.summary) and (t1.owner == t2.owner) and (t1.done == t2.done)
    )


@pytest.fixture(autouse=True)
def initialized_task_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir), "tiny")
    yield
    tasks.stop_tasks_db()
