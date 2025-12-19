"""Tests for Exercise 16"""
import pytest
from exercise import sum_all, create_model, train_model, process

def test_sum_all():
    assert sum_all(1, 2, 3, 4) == 10

def test_create_model():
    model = create_model(type='cnn', layers=5)
    assert model['type'] == 'cnn'

def test_train_model():
    result = train_model([1,2,3], epochs=10, learning_rate=0.001)
    assert "10 epochs" in result

def test_process():
    assert process(1, 2, 3) == 6
    assert process(1, 2, z=3) == 6

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
