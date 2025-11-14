"""Tests for Exercise 20"""
import pytest
from solution import safe_get, ensure_key, merge_dicts, set_union, set_intersection, set_difference

def test_safe_get():
    d = {'a': 1}
    assert safe_get(d, 'a') == 1
    assert safe_get(d, 'b', 'default') == 'default'

def test_ensure_key():
    d = {'a': 1}
    result = ensure_key(d, 'b', 2)
    assert d['b'] == 2

def test_merge_dicts():
    assert merge_dicts({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}

def test_set_union():
    assert set_union({1, 2}, {2, 3}) == {1, 2, 3}

def test_set_intersection():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}

def test_set_difference():
    assert set_difference({1, 2, 3}, {2, 3}) == {1}

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
