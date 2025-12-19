"""
Tests for Exercise 11: NumPy Basics
"""
import pytest
import numpy as np
from exercise import (
    create_array, create_zeros, array_stats, normalize_array,
    matrix_multiply, select_rows, reshape_array
)


def test_create_array():
    arr = create_array([1, 2, 3])
    assert isinstance(arr, np.ndarray)
    assert np.array_equal(arr, np.array([1, 2, 3]))


def test_create_zeros():
    arr = create_zeros((2, 3))
    assert arr.shape == (2, 3)
    assert np.all(arr == 0)


def test_array_stats():
    arr = np.array([1, 2, 3, 4, 5])
    stats = array_stats(arr)
    assert stats["mean"] == pytest.approx(3.0)
    assert stats["min"] == 1.0
    assert stats["max"] == 5.0


def test_normalize_array():
    arr = np.array([0, 5, 10])
    normalized = normalize_array(arr)
    assert np.allclose(normalized, [0.0, 0.5, 1.0])


def test_matrix_multiply():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[2, 0], [1, 2]])
    result = matrix_multiply(a, b)
    expected = np.array([[4, 4], [10, 8]])
    assert np.array_equal(result, expected)


def test_select_rows():
    arr = np.array([[1, 2], [3, 4], [5, 6]])
    result = select_rows(arr, [0, 2])
    expected = np.array([[1, 2], [5, 6]])
    assert np.array_equal(result, expected)


def test_reshape_array():
    arr = np.array([1, 2, 3, 4, 5, 6])
    reshaped = reshape_array(arr, (2, 3))
    assert reshaped.shape == (2, 3)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
