# Exercise 39: Descriptors

## Concept

Descriptors control attribute access using `__get__`, `__set__`, and `__delete__`. They power properties, methods, and static/class methods.

### Key Concepts

1. **Descriptor protocol**: `__get__`, `__set__`, `__delete__`
2. **Data descriptors**: Define both `__get__` and `__set__`
3. **Non-data descriptors**: Define only `__get__`
4. **Lazy properties**: Compute once, cache result

## AI/ML Application

- Type-validated model parameters
- Lazy loading of model weights
- Computed properties with caching

## Your Task

1. `TypedProperty` class - Descriptor that validates type on assignment
2. `Model` class - Uses TypedProperty for learning_rate (float) and epochs (int)
3. `LazyProperty` class - Descriptor that computes value once and caches it

## Testing
```bash
pytest exercises/39_descriptors/test_descriptors.py -v
```
