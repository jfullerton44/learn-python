# Exercise 3: List/Dict/Set Comprehensions

## Concept

Comprehensions provide a concise way to create lists, dictionaries, and sets. They're more readable and often faster than equivalent for loops.

### Syntax
- **List**: `[expression for item in iterable if condition]`
- **Dict**: `{key: value for item in iterable if condition}`
- **Set**: `{expression for item in iterable if condition}`
- **Nested**: Multiple for clauses for nested iteration

## AI/ML Application

Comprehensions are essential for:
- Data preprocessing and transformation
- Feature engineering (creating new features from existing ones)
- Batch processing (transforming batches of data)
- Filtering datasets based on conditions

## Code Examples

### List Comprehension
```python
# Basic list comprehension: [expression for item in iterable]
squares = [x ** 2 for x in range(6)]
# [0, 1, 4, 9, 16, 25]

# With a filter condition
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
```

### Dict Comprehension
```python
# Create a dict from two lists
names = ["lr", "epochs", "batch"]
values = [0.01, 10, 32]
config = {k: v for k, v in zip(names, values)}
# {'lr': 0.01, 'epochs': 10, 'batch': 32}

# Transform dict values
celsius = {"NYC": 0, "LA": 20, "CHI": -5}
fahrenheit = {city: c * 9/5 + 32 for city, c in celsius.items()}
# {'NYC': 32.0, 'LA': 68.0, 'CHI': 23.0}
```

### Set Comprehension
```python
# Unique word lengths from a sentence
words = ["the", "cat", "sat", "on", "the", "mat"]
lengths = {len(w) for w in words}
# {2, 3}
```

### Nested Comprehension
```python
# Flatten a 2D matrix into a 1D list
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [val for row in matrix for val in row]
# [1, 2, 3, 4, 5, 6]

# Generate coordinate pairs
coords = [(r, c) for r in range(2) for c in range(3)]
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
```

### Conditional Expression in Comprehension
```python
# Ternary expression inside a comprehension
labels = ["positive" if score >= 0.5 else "negative" for score in [0.9, 0.3, 0.7, 0.1]]
# ['positive', 'negative', 'positive', 'negative']

# Transform values differently based on a condition
nums = [1, 2, 3, 4, 5]
transformed = [x ** 2 if x % 2 == 0 else x ** 3 for x in nums]
# [1, 4, 27, 16, 125]
```

## Your Task

Implement these functions using comprehensions:

1. `square_numbers(numbers)` - Return list of squared numbers
2. `filter_even(numbers)` - Return list of only even numbers
3. `create_feature_dict(names, values)` - Create dict mapping names to values
4. `extract_labels(data_dicts)` - Extract 'label' field from list of dicts
5. `flatten_matrix(matrix)` - Flatten 2D list using nested comprehension
6. `unique_lengths(strings)` - Return set of unique string lengths
7. `conditional_transform(numbers)` - Square if even, cube if odd
8. `batch_normalize(values, mean, std)` - Normalize values: `(x - mean) / std`

## Testing
```bash
pytest exercises/03_comprehensions/test_comprehensions.py -v
```
