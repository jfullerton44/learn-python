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

## Code Examples

### `dict.get()` — Safe Access with a Default

```python
config = {"epochs": 10, "lr": 0.001}

print(config.get("epochs"))        # 10
print(config.get("batch_size"))    # None — no KeyError
print(config.get("batch_size", 32))  # 32 — custom default
```

### `dict.setdefault()` — Get or Initialize

```python
counts = {"apple": 3}

# Returns existing value if key is present
val = counts.setdefault("apple", 0)
print(val)     # 3

# Sets and returns default if key is missing
val = counts.setdefault("banana", 0)
print(val)     # 0
print(counts)  # {'apple': 3, 'banana': 0}
```

### Dictionary Merging

```python
defaults = {"color": "blue", "size": 10, "verbose": False}
overrides = {"size": 20, "verbose": True}

# Unpacking method (Python 3.5+)
merged = {**defaults, **overrides}
print(merged)  # {'color': 'blue', 'size': 20, 'verbose': True}

# Merge operator (Python 3.9+)
merged = defaults | overrides
print(merged)  # {'color': 'blue', 'size': 20, 'verbose': True}
```

### Set Operations

```python
frontend = {"alice", "bob", "charlie"}
backend = {"bob", "diana", "charlie"}

# Union — everyone on either team
print(frontend | backend)   # {'alice', 'bob', 'charlie', 'diana'}

# Intersection — on both teams
print(frontend & backend)   # {'bob', 'charlie'}

# Difference — frontend only
print(frontend - backend)   # {'alice'}

# Symmetric difference — on exactly one team
print(frontend ^ backend)   # {'alice', 'diana'}
```

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
