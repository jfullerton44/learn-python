"""Tests for Exercise 24"""
import pytest
import tempfile
import os
from solution import dict_to_json_string, json_string_to_dict, save_config, load_config

def test_dict_to_json():
    result = dict_to_json_string({'a': 1, 'b': 2})
    assert '"a": 1' in result

def test_json_to_dict():
    result = json_string_to_dict('{"a": 1}')
    assert result == {'a': 1}

def test_save_load_config():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        filepath = f.name
    try:
        config = {'model': 'resnet', 'lr': 0.001}
        save_config(config, filepath)
        loaded = load_config(filepath)
        assert loaded == config
    finally:
        os.unlink(filepath)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
