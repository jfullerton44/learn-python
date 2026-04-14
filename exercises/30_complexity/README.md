# Exercise 30: Algorithm Complexity Basics

## Concept

Understanding time and space complexity helps you write efficient code. Big O notation describes how performance scales with input size.

### Key Concepts

1. **O(1)**: Constant time - independent of input size
2. **O(n)**: Linear time - grows with input size
3. **O(log n)**: Logarithmic - binary search pattern
4. **O(n²)**: Quadratic - nested loops

## AI/ML Application

- Optimizing data processing pipelines
- Choosing appropriate algorithms
- Understanding model training complexity

## Code Examples

### O(1) — Constant time: same speed regardless of input size

```python
def get_first(items):
    return items[0]  # Always one operation, no matter how big the list

data = list(range(1_000_000))
first = get_first(data)  # Instant, even with a million items
```

### O(n) — Linear time: grows proportionally with input size

```python
def linear_search(items, target):
    for i, item in enumerate(items):  # May check every element
        if item == target:
            return i
    return -1

index = linear_search([10, 20, 30, 40, 50], 40)  # Returns 3
```

### O(log n) — Logarithmic time: halves the problem each step

```python
def binary_search(sorted_items, target):
    low, high = 0, len(sorted_items) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_items[mid] == target:
            return mid
        elif sorted_items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Searching 1,000,000 items takes ~20 steps instead of 1,000,000
result = binary_search(list(range(100)), 73)  # Returns 73
```

### O(n²) — Quadratic time: nested loops over the input

```python
def find_all_pairs(items):
    pairs = []
    for i in range(len(items)):       # n iterations
        for j in range(len(items)):   # × n iterations = n² total
            pairs.append((items[i], items[j]))
    return pairs

# 5 items → 25 pairs; 100 items → 10,000 pairs
pairs = find_all_pairs([1, 2, 3])  # 9 pairs
```

## Your Task

1. `constant_time(items)` - O(1) operation: return first item
2. `linear_search(items, target)` - O(n): search for target, return index or -1
3. `quadratic_operation(n)` - O(n²): nested loop operation
4. `logarithmic_search(sorted_items, target)` - O(log n): binary search
5. `analyze_complexity(operation_type)` - Return complexity string for operation type

## Testing
```bash
pytest exercises/30_complexity/test_complexity.py -v
```
