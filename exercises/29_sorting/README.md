# Exercise 29: Sorting and Ordering

## Concept

Python provides flexible sorting with sorted() and .sort(), supporting custom keys and multiple criteria.

### Key Concepts

1. **sorted()**: Returns new sorted list
2. **.sort()**: Sorts list in place
3. **key parameter**: Custom sort function
4. **reverse**: Descending order

## AI/ML Application

- Ranking predictions by confidence
- Sorting results by multiple metrics
- Top-K selection

## Code Examples

### `sorted()` returns a new sorted list

```python
scores = [88, 45, 92, 71, 65]
ordered = sorted(scores)
print(ordered)  # [45, 65, 71, 88, 92]
print(scores)   # [88, 45, 92, 71, 65] — original unchanged
```

### Sorting in descending order with `reverse`

```python
scores = [88, 45, 92, 71, 65]
top_scores = sorted(scores, reverse=True)
print(top_scores)  # [92, 88, 71, 65, 45]
```

### Custom sort key with `key` parameter

```python
words = ["banana", "pie", "strawberry", "kiwi"]
by_length = sorted(words, key=len)
print(by_length)  # ['pie', 'kiwi', 'banana', 'strawberry']
```

### Sorting dicts by a specific key using `lambda`

```python
predictions = [
    {"label": "cat", "confidence": 0.92},
    {"label": "dog", "confidence": 0.85},
    {"label": "bird", "confidence": 0.97},
]
ranked = sorted(predictions, key=lambda p: p["confidence"], reverse=True)
print(ranked[0]["label"])  # 'bird'
```

### Multi-key sorting with `itemgetter`

```python
from operator import itemgetter

students = [
    {"name": "Alice", "grade": "A", "age": 22},
    {"name": "Bob", "grade": "A", "age": 20},
    {"name": "Carol", "grade": "B", "age": 21},
]
# Sort by grade first, then by age
by_grade_age = sorted(students, key=itemgetter("grade", "age"))
print([s["name"] for s in by_grade_age])  # ['Bob', 'Alice', 'Carol']
```

### In-place sort with `.sort()`

```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()        # Modifies the list directly, returns None
print(numbers)        # [1, 1, 3, 4, 5]
```

## Your Task

1. `sort_by_value(items)` - Sort list in ascending order
2. `sort_by_key(dict_list, key)` - Sort list of dicts by specified key
3. `sort_descending(items)` - Sort in descending order
4. `sort_by_confidence(predictions)` - Sort predictions by 'confidence' key descending
5. `sort_by_multiple_keys(items, keys)` - Sort by multiple keys using itemgetter
6. `in_place_sort(items)` - Sort list in place and return it

## Testing
```bash
pytest exercises/29_sorting/test_sorting.py -v
```
