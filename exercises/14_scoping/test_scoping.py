"""Tests for Exercise 14"""
import pytest
from exercise import demonstrate_legb, use_global, use_nonlocal, create_counter, global_var

def test_legb():
    assert demonstrate_legb() == "local"

def test_global():
    result = use_global()
    assert result == "modified"

def test_nonlocal():
    assert use_nonlocal() == "modified"

def test_counter():
    counter = create_counter()
    assert counter() == 1
    assert counter() == 2

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
