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

## Code Examples

### `len()` — Get the Length of a Sequence

```python
print(len([10, 20, 30]))     # 3
print(len("hello"))           # 5
print(len({"a": 1, "b": 2})) # 2
```

### `enumerate()` — Iterate with an Index

```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# Start counting from 1
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

### `zip()` — Pair Elements from Multiple Iterables

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

pairs = list(zip(names, scores))
print(pairs)  # [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Useful for building dicts
score_map = dict(zip(names, scores))
print(score_map)  # {'Alice': 85, 'Bob': 92, 'Charlie': 78}
```

### `isinstance()` — Check Object Types

```python
print(isinstance(42, int))          # True
print(isinstance("hi", str))        # True
print(isinstance(3.14, (int, float)))  # True — check multiple types
print(isinstance([], dict))         # False
```

### `getattr()` / `setattr()` — Dynamic Attribute Access

```python
class Config:
    batch_size = 32
    lr = 0.001

cfg = Config()
print(getattr(cfg, "batch_size"))          # 32
print(getattr(cfg, "missing", "default"))  # "default"

setattr(cfg, "lr", 0.01)
print(cfg.lr)  # 0.01
```

### `min()` / `max()` with `key` Functions

```python
words = ["banana", "fig", "cherry", "apple"]

print(min(words))                        # "apple" — alphabetical
print(max(words, key=len))               # "banana" — longest word
print(min(words, key=lambda w: w[-1]))   # "banana" — smallest last letter
```

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
