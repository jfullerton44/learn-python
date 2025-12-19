"""Tests for Exercise 27"""
import pytest
import tempfile
import os
from exercise import pickle_save, pickle_load, json_save, json_load, serialize_model_weights, deserialize_model_weights

def test_pickle_save_load():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        filepath = f.name
    try:
        data = {'a': 1, 'b': [1, 2, 3]}
        pickle_save(data, filepath)
        loaded = pickle_load(filepath)
        assert loaded == data
    finally:
        os.unlink(filepath)

def test_json_save_load():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        filepath = f.name
    try:
        data = {'x': 10, 'y': 20}
        json_save(data, filepath)
        loaded = json_load(filepath)
        assert loaded == data
    finally:
        os.unlink(filepath)

def test_serialize_deserialize_weights():
    weights = [1, 2, 3, 4, 5]
    serialized = serialize_model_weights(weights)
    deserialized = deserialize_model_weights(serialized)
    assert deserialized == weights

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
