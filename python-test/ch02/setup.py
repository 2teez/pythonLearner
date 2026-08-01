# setup.py - Package setup for tasks
from setuptools import find_packages, setup

setup(
    name="tasks",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
