"""Tests for Exercise 26"""
import pytest
import os
from exercise import get_env_var, set_env_var, get_api_key, load_env_config

def test_get_env_var():
    os.environ['TEST_VAR'] = 'test_value'
    assert get_env_var('TEST_VAR') == 'test_value'

def test_set_env_var():
    set_env_var('NEW_VAR', 'new_value')
    assert os.environ['NEW_VAR'] == 'new_value'

def test_get_api_key():
    os.environ['API_KEY'] = 'secret123'
    assert get_api_key() == 'secret123'

def test_load_env_config():
    os.environ['DEBUG'] = 'True'
    os.environ['PORT'] = '3000'
    config = load_env_config()
    assert config['debug'] == True
    assert config['port'] == 3000

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
