# Exercise 54: Advanced Collections

## Concept

Python's collections module provides specialized container types for efficient data handling.

### Key Concepts

1. **namedtuple**: Immutable records with names
2. **defaultdict**: Auto-initializing dictionaries
3. **Counter**: Count occurrences
4. **deque**: Efficient double-ended queue

## AI/ML Application

- Metrics tracking with Counter
- Feature caching with defaultdict
- Sliding window with deque

## Your Task

1. `MLComponent` class - Component using collections
2. `Pipeline` class - Pipeline with deque for stages
3. `create_component(name)` - Factory function
4. `validate_config(config)` - Validation

## Testing
```bash
pytest exercises/54_collections/test_collections.py -v
```
