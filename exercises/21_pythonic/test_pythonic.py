"""Tests for Exercise 21"""
import pytest
import tempfile
from solution import eafp_file_read, lbyl_file_read, duck_typing_len, pythonic_swap, list_comprehension_even

def test_eafp_file_read():
    assert eafp_file_read('/nonexistent') is None

def test_duck_typing_len():
    assert duck_typing_len([1, 2, 3]) == 3
    assert duck_typing_len("hello") == 5

def test_pythonic_swap():
    assert pythonic_swap(1, 2) == (2, 1)

def test_list_comprehension_even():
    assert list_comprehension_even([1, 2, 3, 4]) == [2, 4]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
