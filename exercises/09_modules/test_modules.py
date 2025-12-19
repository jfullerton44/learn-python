"""
Tests for Exercise 9: Modules and Packages
"""
import pytest
from exercise import BaseModel, NeuralNet, load_data, save_checkpoint


def test_base_model():
    model = BaseModel("TestModel")
    assert model.name == "TestModel"
    assert "Training TestModel" in model.train()


def test_neural_net_inheritance():
    nn = NeuralNet("MLP", [64, 128])
    assert isinstance(nn, BaseModel)
    assert nn.name == "MLP"
    assert nn.layers == [64, 128]


def test_neural_net_forward():
    nn = NeuralNet("CNN", [32, 64, 128])
    result = nn.forward("input")
    assert "3 layers" in result


def test_load_data():
    result = load_data("/path/to/data.csv")
    assert "Data loaded" in result
    assert "/path/to/data.csv" in result


def test_save_checkpoint():
    model = BaseModel("SaveTest")
    result = save_checkpoint(model, "/path/checkpoint.pt")
    assert "Saved" in result
    assert "SaveTest" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
