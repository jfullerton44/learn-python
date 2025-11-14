"""Exercise 24: JSON"""
import json

def dict_to_json_string(data):
    return json.dumps(data)

def json_string_to_dict(json_str):
    return json.loads(json_str)

def save_config(config, filepath):
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=2)

def load_config(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def model_to_json(model_dict):
    return json.dumps(model_dict, indent=2)
