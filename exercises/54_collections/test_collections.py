"""Tests for Exercise 54"""
import pytest
from exercise import *

def test_ml_component():
    component = MLComponent("test")
    assert component.name == "test"
    assert component.process([1, 2, 3]) == [1, 2, 3]

def test_pipeline():
    pipeline = Pipeline()
    component = create_component("step1")
    pipeline.add_step(component)
    result = pipeline.execute([1, 2, 3])
    assert result == [1, 2, 3]

def test_validate_config():
    valid_config = {"model": "resnet", "data": "/path"}
    assert validate_config(valid_config) == True

    invalid_config = {"model": "resnet"}
    assert validate_config(invalid_config) == False

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
