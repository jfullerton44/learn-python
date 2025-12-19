# Exercise 20: Dictionary and Set Advanced Features

## Concept

Advanced dictionary and set operations provide efficient ways to handle collections of data with special access patterns.

### Key Concepts

1. **dict.get()**: Safe access with default values
2. **dict.setdefault()**: Get or set if missing
3. **Dictionary merging**: `{**d1, **d2}` or `d1 | d2` (Python 3.9+)
4. **Set operations**: Union, intersection, difference

## AI/ML Application

- Merging configuration dictionaries
- Feature set operations
- Deduplication and comparison

## Your Task

1. `safe_get(d, key, default=None)` - Get value with default using .get()
2. `ensure_key(d, key, default_value)` - Use setdefault to ensure key exists
3. `merge_dicts(d1, d2)` - Merge two dictionaries
4. `set_union(s1, s2)` - Return union of two sets
5. `set_intersection(s1, s2)` - Return intersection of two sets
6. `set_difference(s1, s2)` - Return elements in s1 but not in s2

## Testing
```bash
pytest exercises/20_dict_set_advanced/test_dict_set.py -v
```
