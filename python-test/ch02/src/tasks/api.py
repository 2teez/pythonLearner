#!/usr/bin/env python3
#
from collections import namedtuple

Tasks = namedtuple("Tasks", ["summary", "owner", "done", "id"])
Tasks.__new__.__defaults__ = (None, None, False, None)


def add(task: Tasks) -> int:
    """Add a task to the task list and return the task's ID."""
    if not isinstance(task, Tasks):
        raise TypeError("task must be a Tasks object")

    tasks.append(task)
    return len(tasks) - 1


def get(task_id: int) -> Tasks:  # (int) -> Tasks
    """Return the task with the given ID."""
    if not isinstance(task_id, int):
        raise TypeError("task_id must be an integer")

    return tasks[task_id]


def list_tasks(owner: str | None) -> list[Tasks]:
    """Return a list of tasks owned by the given owner."""
    if not isinstance(owner, (str, type(None))):
        raise TypeError("owner must be a string or None")

    if owner is None:
        return tasks
    return [task for task in tasks if task.owner == owner]


def count() -> int:
    """Return the number of tasks owned by the given owner."""
    return len(tasks)


def update(task_id: int, task: Tasks) -> None:
    """Update the task with the given ID."""
    tasks[task_id] = task


def delete(task_id: int) -> None:
    """Delete the task with the given ID."""
    tasks.pop(task_id)


def delete_all() -> None:
    """Delete all tasks."""
    tasks.clear()


def unique_id() -> set[int]:
    """Return the number of unique task IDs."""
    return set({task.id for task in tasks})


def start_tasks_db(db_path: str, db_type: str) -> None:
    """Start the tasks database."""
    if db_type not in ("tiny", "mongo"):
        raise ValueError("db_type must be 'tiny' or 'mongo'")


def stop_tasks_db() -> None:
    """Stop the tasks database."""


tasks = []
