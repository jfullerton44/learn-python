# Exercise 17: Common Built-in Functions

## Concept

Python's built-in functions provide powerful utilities for common operations without importing modules.

### Key Concepts

1. **len()**: Get length of sequences
2. **enumerate()**: Iterate with index
3. **zip()**: Pair elements from multiple iterables
4. **isinstance()**: Check object types
5. **getattr()/setattr()**: Dynamic attribute access
6. **min()/max()/sum()**: Aggregate functions

## AI/ML Application

- Processing batches of data
- Dynamic model configuration
- Iterating over datasets with indices

## Your Task

1. `count_items(items)` - Return the length of items using len()
2. `create_pairs(list1, list2)` - Pair elements using zip()
3. `enumerate_items(items)` - Return list of (index, item) tuples
4. `check_type(obj, expected_type)` - Check if obj is an instance of expected_type
5. `get_attribute(obj, attr_name, default=None)` - Get attribute with default
6. `find_extremes(numbers)` - Return dict with min, max, and sum

## Testing
```bash
pytest exercises/17_builtins/test_builtins.py -v
```
