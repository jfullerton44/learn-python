# Exercise 27: Basic Serialization

## Concept

Serialization converts Python objects to bytes for storage/transmission. Pickle handles Python objects; JSON for cross-language compatibility.

### Key Concepts

1. **pickle**: Python-specific binary serialization
2. **JSON**: Text-based, cross-language compatible
3. **Trade-offs**: Pickle is more flexible but less secure; JSON is safer but limited to basic types

## AI/ML Application

- Saving model weights and checkpoints
- Caching computed results
- Storing training state

## Code Examples

### Saving and loading Python objects with pickle

```python
import pickle

weights = {"layer1": [0.1, 0.5, -0.3], "layer2": [0.8, -0.2]}

# Save to file
with open("weights.pkl", "wb") as f:
    pickle.dump(weights, f)

# Load from file
with open("weights.pkl", "rb") as f:
    loaded = pickle.load(f)
print(loaded)  # {'layer1': [0.1, 0.5, -0.3], 'layer2': [0.8, -0.2]}
```

### Serializing to bytes with `pickle.dumps()` / `pickle.loads()`

```python
import pickle

data = [1, 2, 3, {"key": "value"}]
raw_bytes = pickle.dumps(data)    # Serialize to bytes (not a file)
restored = pickle.loads(raw_bytes) # Deserialize from bytes
print(restored)  # [1, 2, 3, {'key': 'value'}]
```

### JSON serialization for cross-language compatibility

```python
import json

config = {"model": "svm", "C": 1.0, "kernel": "rbf"}

# Save to JSON file
with open("config.json", "w") as f:
    json.dump(config, f)

# Load from JSON file
with open("config.json", "r") as f:
    loaded = json.load(f)
print(loaded)  # {'model': 'svm', 'C': 1.0, 'kernel': 'rbf'}
```

### When to use each format

```python
# Use PICKLE when:
# - Saving complex Python objects (classes, functions, numpy arrays)
# - Only Python will read the data
# - WARNING: Never unpickle data from untrusted sources (security risk)

# Use JSON when:
# - Data needs to be read by other languages (JavaScript, Java, etc.)
# - Human-readable format is desired
# - Data contains only basic types (dict, list, str, int, float, bool, None)
```

## Your Task

1. `pickle_save(obj, filepath)` - Save object to pickle file
2. `pickle_load(filepath)` - Load object from pickle file
3. `json_save(obj, filepath)` - Save object to JSON file
4. `json_load(filepath)` - Load object from JSON file
5. `serialize_model_weights(weights)` - Convert weights to bytes with pickle.dumps
6. `deserialize_model_weights(data)` - Restore weights with pickle.loads

## Testing
```bash
pytest exercises/27_serialization/test_serialization.py -v
```
