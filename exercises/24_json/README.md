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
