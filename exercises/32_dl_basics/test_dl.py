"""Tests for Exercise 32"""
import pytest
import numpy as np
from exercise import create_tensor, tensor_add, tensor_multiply, create_network

def test_create_tensor():
    tensor = create_tensor((2, 3))
    assert tensor.shape == (2, 3)

def test_tensor_add():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    result = tensor_add(a, b)
    assert np.array_equal(result, [5, 7, 9])

def test_tensor_multiply():
    a = np.array([2, 3, 4])
    b = np.array([1, 2, 3])
    result = tensor_multiply(a, b)
    assert np.array_equal(result, [2, 6, 12])

def test_create_network():
    net = create_network(10, 5, 2)
    x = np.random.randn(1, 10)
    output = net.forward(x)
    assert output.shape == (1, 2)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
