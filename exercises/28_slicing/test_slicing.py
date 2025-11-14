"""Tests for Exercise 28"""
import pytest
from solution import get_every_nth, reverse_list, get_last_n, get_middle_section, create_slice_object, apply_slice

def test_get_every_nth():
    assert get_every_nth([0, 1, 2, 3, 4, 5], 2) == [0, 2, 4]

def test_reverse_list():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]

def test_get_last_n():
    assert get_last_n([1, 2, 3, 4, 5], 3) == [3, 4, 5]

def test_get_middle_section():
    result = get_middle_section([1, 2, 3, 4, 5, 6, 7, 8])
    assert len(result) == 4

def test_slice_object():
    s = create_slice_object(1, 5, 2)
    assert apply_slice([0, 1, 2, 3, 4, 5], s) == [1, 3]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
