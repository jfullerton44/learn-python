"""
Tests for Exercise 8: Basic Data Structures
"""
import pytest
from solution import (
    store_predictions, manage_hyperparams, deduplicate_samples,
    cache_results, implement_stack, implement_queue
)


def test_store_predictions():
    result = store_predictions([1, 0, 1], [1, 0, 0])
    assert result == [(1, 1), (0, 0), (1, 0)]
    assert all(isinstance(item, tuple) for item in result)


def test_manage_hyperparams():
    params = manage_hyperparams()
    assert "model" in params
    assert "training" in params
    assert params["model"]["type"] == "neural_network"
    assert params["training"]["epochs"] == 100


def test_deduplicate_samples():
    assert deduplicate_samples([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
    assert deduplicate_samples([]) == []
    assert deduplicate_samples([1, 1, 1]) == [1]


def test_cache_results():
    cache = cache_results(lambda x: x**2, [1, 2, 3, 2, 1])
    assert cache[1] == 1
    assert cache[2] == 4
    assert cache[3] == 9
    assert len(cache) == 3


def test_stack():
    stack = implement_stack()
    assert stack.is_empty()
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty()


def test_queue():
    queue = implement_queue()
    assert queue.is_empty()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.size() == 2
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.is_empty()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
