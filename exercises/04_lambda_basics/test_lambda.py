"""
Tests for Exercise 4: Lambda Functions
"""
import pytest
import math
from solution import (
    apply_activation, filter_by_threshold, sort_by_confidence,
    compute_total_loss, create_scaler
)


def test_apply_activation_relu():
    result = apply_activation([-2, -1, 0, 1, 2], "relu")
    assert result == [0, 0, 0, 1, 2]


def test_apply_activation_sigmoid():
    result = apply_activation([0], "sigmoid")
    assert result == pytest.approx([0.5])

    result = apply_activation([-1, 0, 1], "sigmoid")
    expected = [1/(1+math.e), 0.5, math.e/(1+math.e)]
    assert result == pytest.approx(expected)


def test_filter_by_threshold():
    assert filter_by_threshold([0.3, 0.7, 0.5, 0.9], 0.6) == [0.7, 0.9]
    assert filter_by_threshold([0.1, 0.2], 0.5) == []
    assert filter_by_threshold([1.0, 0.9, 0.8], 0.0) == [1.0, 0.9, 0.8]


def test_sort_by_confidence():
    predictions = [
        {'pred': 'A', 'confidence': 0.7},
        {'pred': 'B', 'confidence': 0.9},
        {'pred': 'C', 'confidence': 0.5}
    ]
    result = sort_by_confidence(predictions)
    assert [p['confidence'] for p in result] == [0.9, 0.7, 0.5]


def test_compute_total_loss():
    assert compute_total_loss([0.5, 0.3, 0.2]) == pytest.approx(1.0)
    assert compute_total_loss([]) == 0.0
    assert compute_total_loss([1.0]) == 1.0


def test_create_scaler():
    scaler = create_scaler(10)
    assert scaler(5) == 50
    assert scaler(0) == 0

    scaler2 = create_scaler(0.5)
    assert scaler2(10) == 5.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
