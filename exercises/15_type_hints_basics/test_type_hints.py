"""Tests for Exercise 15"""
import pytest
from solution import process_numbers, get_config, find_item, split_data

def test_process_numbers():
    assert process_numbers([1, 2, 3]) == 6

def test_get_config():
    config = get_config()
    assert isinstance(config, dict)

def test_find_item():
    assert find_item(['a', 'b', 'c'], 'b') == 1
    assert find_item(['a', 'b'], 'z') is None

def test_split_data():
    train, test = split_data([1, 2, 3, 4, 5], 0.8)
    assert len(train) == 4
    assert len(test) == 1

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
