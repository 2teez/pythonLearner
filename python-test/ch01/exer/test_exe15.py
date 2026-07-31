#!/usr/bin/env python3


def test_contains_():
    """Test to check the values contained in a list"""
    assert 1 in [1, 2, 3]


def test_greater_than():
    """Test to check if a number is greater than another"""
    assert "a" < "b"


def test_fizz_not_in_fizzbuzz():
    """Test to check if 'fizz' is not in the fizzbuzz output"""
    assert "fizz" not in "fizzbuzz"
