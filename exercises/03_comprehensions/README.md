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

## Example
```python
square_numbers([1, 2, 3, 4])  # [1, 4, 9, 16]
filter_even([1, 2, 3, 4, 5])  # [2, 4]
flatten_matrix([[1, 2], [3, 4]])  # [1, 2, 3, 4]
```

## Testing
```bash
pytest exercises/03_comprehensions/test_comprehensions.py -v
```
