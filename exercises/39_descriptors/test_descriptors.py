"""Tests for Exercise 39"""
import pytest
from exercise import TypedProperty, Model, LazyProperty

def test_typed_property_valid():
    model = Model(0.01, 100)
    assert model.learning_rate == 0.01
    assert model.epochs == 100

def test_typed_property_invalid():
    with pytest.raises(TypeError):
        Model("invalid", 100)

    with pytest.raises(TypeError):
        Model(0.01, "invalid")

def test_lazy_property():
    class MyClass:
        @LazyProperty
        def expensive_computation(self):
            return 42

    obj = MyClass()
    # First access computes
    result = obj.expensive_computation
    assert result == 42
    # Second access returns cached value
    assert obj.expensive_computation == 42

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
