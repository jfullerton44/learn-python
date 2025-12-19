"""Tests for Exercise 33"""
import pytest
import numpy as np
from exercise import normalize_features, standardize_features, one_hot_encode, split_train_val_test

def test_normalize_features():
    data = np.array([[0, 10], [5, 5], [10, 0]])
    normalized = normalize_features(data)
    assert np.min(normalized) >= 0
    assert np.max(normalized) <= 1

def test_standardize_features():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    standardized = standardize_features(data)
    assert standardized.shape == data.shape

def test_one_hot_encode():
    labels = np.array([0, 1, 2, 0])
    encoded = one_hot_encode(labels, 3)
    assert encoded.shape == (4, 3)
    assert np.sum(encoded[0]) == 1

def test_split_train_val_test():
    data = np.arange(100)
    train, val, test = split_train_val_test(data)
    assert len(train) == 70
    assert len(val) == 15
    assert len(test) == 15

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
