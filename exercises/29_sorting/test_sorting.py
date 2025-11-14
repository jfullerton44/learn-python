"""Tests for Exercise 29"""
import pytest
from solution import sort_by_value, sort_by_key, sort_descending, sort_by_confidence, in_place_sort

def test_sort_by_value():
    assert sort_by_value([3, 1, 2]) == [1, 2, 3]

def test_sort_by_key():
    data = [{'name': 'b', 'val': 2}, {'name': 'a', 'val': 1}]
    result = sort_by_key(data, 'name')
    assert result[0]['name'] == 'a'

def test_sort_descending():
    assert sort_descending([1, 2, 3]) == [3, 2, 1]

def test_sort_by_confidence():
    preds = [{'confidence': 0.7}, {'confidence': 0.9}, {'confidence': 0.5}]
    result = sort_by_confidence(preds)
    assert result[0]['confidence'] == 0.9

def test_in_place_sort():
    items = [3, 1, 2]
    result = in_place_sort(items)
    assert result == [1, 2, 3]
    assert items == [1, 2, 3]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
