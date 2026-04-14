# Exercise 4: Lambda Functions and Basic Functional Programming

## Concept

Lambda functions are anonymous, single-expression functions. Combined with map(), filter(), reduce(), and sorted(), they enable functional programming patterns.

## AI/ML Application

- Filtering datasets
- Transforming features
- Sorting predictions by confidence
- Aggregating metrics

## Code Examples

### Lambda Functions
```python
# A lambda is a small anonymous function
double = lambda x: x * 2
print(double(5))  # 10

# Lambdas can take multiple arguments
add = lambda a, b: a + b
print(add(3, 7))  # 10
```

### map() — Apply a Function to Every Item
```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
# [1, 4, 9, 16]

# Convert strings to uppercase
words = ["hello", "world"]
upper = list(map(lambda s: s.upper(), words))
# ['HELLO', 'WORLD']
```

### filter() — Keep Items That Match a Condition
```python
scores = [0.2, 0.8, 0.5, 0.9, 0.1]
passing = list(filter(lambda s: s >= 0.5, scores))
# [0.8, 0.5, 0.9]
```

### reduce() — Accumulate Items into a Single Value
```python
from functools import reduce

nums = [1, 2, 3, 4, 5]
total = reduce(lambda acc, x: acc + x, nums)
# 15

product = reduce(lambda acc, x: acc * x, nums)
# 120
```

### Sorting with key Functions
```python
# Sort dicts by a specific field
predictions = [
    {"label": "cat", "confidence": 0.9},
    {"label": "dog", "confidence": 0.7},
    {"label": "bird", "confidence": 0.8},
]
ranked = sorted(predictions, key=lambda p: p["confidence"], reverse=True)
# [{'label': 'cat', ...}, {'label': 'bird', ...}, {'label': 'dog', ...}]

# Sort strings by length
words = ["banana", "pie", "strawberry", "kiwi"]
by_length = sorted(words, key=lambda w: len(w))
# ['pie', 'kiwi', 'banana', 'strawberry']
```

### Returning Lambdas from Functions
```python
def make_multiplier(factor):
    return lambda x: x * factor

triple = make_multiplier(3)
print(triple(10))  # 30
print(triple(4))   # 12
```

## Your Task

1. `apply_activation(values, activation_name)` - Use lambda with map() to apply activation:
   - "relu": max(0, x)
   - "sigmoid": 1 / (1 + e^(-x))
2. `filter_by_threshold(predictions, threshold)` - Filter predictions >= threshold
3. `sort_by_confidence(predictions)` - Sort list of dicts by 'confidence' key (descending)
4. `compute_total_loss(losses)` - Use reduce() to sum losses
5. `create_scaler(factor)` - Return lambda that multiplies input by factor

## Testing
```bash
pytest exercises/04_lambda_basics/test_lambda.py -v
```
