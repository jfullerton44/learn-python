"""Exercise 26: Environment Variables"""
import os

def get_env_var(var_name, default=None):
    return os.environ.get(var_name, default)

def set_env_var(var_name, value):
    os.environ[var_name] = value

def get_api_key():
    return get_env_var('API_KEY', 'default_key')

def get_model_path():
    return get_env_var('MODEL_PATH', '/default/path')

def load_env_config():
    return {
        'debug': get_env_var('DEBUG', 'False') == 'True',
        'port': int(get_env_var('PORT', '8000'))
    }
