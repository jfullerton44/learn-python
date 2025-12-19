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
