"""Exercise 27: Serialization"""
import pickle
import json

def pickle_save(obj, filepath):
    with open(filepath, 'wb') as f:
        pickle.dump(obj, f)

def pickle_load(filepath):
    with open(filepath, 'rb') as f:
        return pickle.load(f)

def json_save(obj, filepath):
    with open(filepath, 'w') as f:
        json.dump(obj, f)

def json_load(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def serialize_model_weights(weights):
    """Serialize numpy-like weights"""
    return pickle.dumps(weights)

def deserialize_model_weights(data):
    return pickle.loads(data)
