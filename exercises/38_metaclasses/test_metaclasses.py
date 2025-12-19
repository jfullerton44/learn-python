"""Tests for Exercise 38"""
import pytest
from exercise import ModelRegistry, BaseModel, ResNet, VGG, get_registered_models

def test_model_registry():
    models = get_registered_models()
    assert 'ResNet' in models
    assert 'VGG' in models

def test_base_model_not_registered():
    models = get_registered_models()
    assert 'BaseModel' not in models

def test_model_instantiation():
    resnet = ResNet()
    vgg = VGG()
    assert isinstance(resnet, BaseModel)
    assert isinstance(vgg, BaseModel)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
