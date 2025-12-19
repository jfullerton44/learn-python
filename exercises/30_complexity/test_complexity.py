"""Tests for Exercise 30"""
import pytest
from exercise import constant_time, linear_search, logarithmic_search, analyze_complexity

def test_constant_time():
    assert constant_time([1, 2, 3]) == 1

def test_linear_search():
    assert linear_search([1, 2, 3, 4], 3) == 2
    assert linear_search([1, 2, 3], 5) == -1

def test_logarithmic_search():
    assert logarithmic_search([1, 2, 3, 4, 5], 3) == 2
    assert logarithmic_search([1, 2, 3, 4], 5) == -1

def test_analyze_complexity():
    assert analyze_complexity('dict_lookup') == 'O(1)'
    assert analyze_complexity('binary_search') == 'O(log n)'

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
