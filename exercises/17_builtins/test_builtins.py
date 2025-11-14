"""Tests for Exercise 17"""
import pytest
from solution import count_items, create_pairs, enumerate_items, check_type, get_attribute, find_extremes

def test_count_items():
    assert count_items([1, 2, 3]) == 3

def test_create_pairs():
    assert create_pairs([1, 2], ['a', 'b']) == [(1, 'a'), (2, 'b')]

def test_enumerate_items():
    assert enumerate_items(['a', 'b']) == [(0, 'a'), (1, 'b')]

def test_check_type():
    assert check_type(5, int) == True
    assert check_type("hello", int) == False

def test_get_attribute():
    class Obj:
        x = 10
    assert get_attribute(Obj(), 'x') == 10

def test_find_extremes():
    result = find_extremes([1, 2, 3, 4, 5])
    assert result == {"min": 1, "max": 5, "sum": 15}

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
