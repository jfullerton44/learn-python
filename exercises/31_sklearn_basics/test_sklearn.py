"""Tests for Exercise 31"""
import pytest
import numpy as np
from solution import split_data, train_logistic_regression, make_predictions, create_pipeline

def test_split_data():
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y = np.array([0, 1, 0, 1])
    X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.5)
    assert len(X_train) == 2
    assert len(X_test) == 2

def test_train_logistic_regression():
    X_train = np.array([[1, 2], [3, 4]])
    y_train = np.array([0, 1])
    model = train_logistic_regression(X_train, y_train)
    assert model is not None

def test_make_predictions():
    X_train = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y_train = np.array([0, 1, 0, 1])
    model = train_logistic_regression(X_train, y_train)
    predictions = make_predictions(model, X_train)
    assert len(predictions) == 4

def test_create_pipeline():
    pipeline = create_pipeline()
    assert pipeline is not None
    assert len(pipeline.steps) == 2

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
