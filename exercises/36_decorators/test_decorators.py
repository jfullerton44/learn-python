"""Tests for Exercise 36"""
import pytest
from exercise import timer, repeat, log_calls, train_model, predict

def test_timer_decorator():
    @timer
    def sample_func():
        return "done"
    result = sample_func()
    assert result == "done"

def test_repeat_decorator():
    @repeat(3)
    def double(x):
        return x * 2
    results = double(5)
    assert len(results) == 3
    assert all(r == 10 for r in results)

def test_log_calls():
    @log_calls
    def greet(name):
        return f"Hello, {name}"
    result = greet("World")
    assert result == "Hello, World"

def test_train_model():
    result = train_model()
    assert result == "trained"

def test_predict():
    results = predict(5)
    assert results == [10, 10, 10]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
