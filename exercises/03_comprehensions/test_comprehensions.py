"""
Tests for Exercise 3: List/Dict/Set Comprehensions
"""
import pytest
from exercise import (
    square_numbers, filter_even, create_feature_dict, extract_labels,
    flatten_matrix, unique_lengths, conditional_transform, batch_normalize
)


def test_square_numbers():
    assert square_numbers([1, 2, 3, 4]) == [1, 4, 9, 16]
    assert square_numbers([]) == []
    assert square_numbers([0]) == [0]
    assert square_numbers([-2, -1, 0, 1, 2]) == [4, 1, 0, 1, 4]


def test_filter_even():
    assert filter_even([1, 2, 3, 4, 5]) == [2, 4]
    assert filter_even([1, 3, 5]) == []
    assert filter_even([2, 4, 6]) == [2, 4, 6]
    assert filter_even([]) == []


def test_create_feature_dict():
    assert create_feature_dict(['a', 'b'], [1.0, 2.0]) == {'a': 1.0, 'b': 2.0}
    assert create_feature_dict([], []) == {}
    assert create_feature_dict(['x'], [5.5]) == {'x': 5.5}


def test_extract_labels():
    data = [{'label': 'A', 'value': 1}, {'label': 'B', 'value': 2}]
    assert extract_labels(data) == ['A', 'B']
    assert extract_labels([]) == []
    assert extract_labels([{'label': 'X'}]) == ['X']


def test_flatten_matrix():
    assert flatten_matrix([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten_matrix([[1], [2], [3]]) == [1, 2, 3]
    assert flatten_matrix([[]]) == []
    assert flatten_matrix([[1, 2, 3]]) == [1, 2, 3]


def test_unique_lengths():
    assert unique_lengths(['a', 'ab', 'abc', 'ab']) == {1, 2, 3}
    assert unique_lengths(['hello', 'world']) == {5}
    assert unique_lengths([]) == set()
    assert unique_lengths(['', 'a', '']) == {0, 1}


def test_conditional_transform():
    assert conditional_transform([1, 2, 3, 4]) == [1, 4, 27, 16]  # 1^3, 2^2, 3^3, 4^2
    assert conditional_transform([2, 4]) == [4, 16]  # Both even
    assert conditional_transform([1, 3]) == [1, 27]  # Both odd
    assert conditional_transform([]) == []


def test_batch_normalize():
    result = batch_normalize([1.0, 2.0, 3.0], mean=2.0, std=1.0)
    assert result == pytest.approx([-1.0, 0.0, 1.0])

    result = batch_normalize([0.0, 5.0, 10.0], mean=5.0, std=5.0)
    assert result == pytest.approx([-1.0, 0.0, 1.0])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
