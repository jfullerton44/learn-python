# Exercise 24: Working with JSON

## Concept

JSON (JavaScript Object Notation) is the standard format for data exchange. Python's json module provides easy serialization and deserialization.

### Key Concepts

1. **json.dumps()**: Convert Python object to JSON string
2. **json.loads()**: Parse JSON string to Python object
3. **json.dump()/load()**: File-based JSON operations
4. **indent**: Pretty-print JSON output

## AI/ML Application

- Saving/loading model configurations
- API data exchange
- Experiment logging

## Code Examples

### Converting Python objects to JSON strings with `json.dumps()`

```python
import json

user = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}
json_string = json.dumps(user)
print(json_string)  # '{"name": "Alice", "age": 30, "scores": [95, 87, 92]}'
```

### Parsing JSON strings with `json.loads()`

```python
import json

json_string = '{"model": "linear_regression", "accuracy": 0.95}'
data = json.loads(json_string)
print(data["model"])     # 'linear_regression'
print(data["accuracy"])  # 0.95
```

### Writing JSON to a file with `json.dump()`

```python
import json

config = {"learning_rate": 0.01, "epochs": 100, "batch_size": 32}
with open("config.json", "w") as f:
    json.dump(config, f, indent=2)
```

### Reading JSON from a file with `json.load()`

```python
import json

with open("config.json", "r") as f:
    config = json.load(f)
print(config["learning_rate"])  # 0.01
```

### Pretty-printing with `indent`

```python
import json

model_info = {"name": "ResNet", "layers": [64, 128, 256], "trained": True}
pretty = json.dumps(model_info, indent=4)
print(pretty)
# {
#     "name": "ResNet",
#     "layers": [64, 128, 256],
#     "trained": true
# }
```

## Your Task

1. `dict_to_json_string(data)` - Convert dict to JSON string
2. `json_string_to_dict(json_str)` - Parse JSON string to dict
3. `save_config(config, filepath)` - Save config dict to JSON file (with indent)
4. `load_config(filepath)` - Load config from JSON file
5. `model_to_json(model_dict)` - Convert model dict to pretty-printed JSON

## Testing
```bash
pytest exercises/24_json/test_json.py -v
```
