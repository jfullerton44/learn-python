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
def lookup_by_key(mapping, key):
    return mapping[key]  # Dict lookup is O(1) on average

scores = {f"player_{i}": i * 10 for i in range(1_000_000)}
score = lookup_by_key(scores, "player_999")  # Instant, even with a million entries
```

### O(n) — Linear time: grows proportionally with input size

```python
def find_max(numbers):
    biggest = numbers[0]
    for num in numbers:  # Must check every element
        if num > biggest:
            biggest = num
    return biggest

result = find_max([3, 7, 2, 9, 4])  # Returns 9
# Doubling the list roughly doubles the time
```

### O(log n) — Logarithmic time: halves the problem each step

```python
def guess_number(secret, low=1, high=100):
    steps = 0
    while low <= high:
        mid = (low + high) // 2
        steps += 1
        if mid == secret:
            return steps
        elif mid < secret:
            low = mid + 1
        else:
            high = mid - 1
    return steps

# Guessing among 100 numbers takes at most 7 steps
# Guessing among 1,000,000 takes at most ~20 steps
print(guess_number(73))  # Only a few steps needed
```

### O(n²) — Quadratic time: nested loops over the input

```python
def has_duplicates_naive(items):
    count = 0
    for i in range(len(items)):            # n iterations
        for j in range(i + 1, len(items)): # × ~n/2 iterations = O(n²)
            count += 1
            if items[i] == items[j]:
                return True, count
    return False, count

# 10 items → 45 comparisons; 100 items → 4,950 comparisons
found, checks = has_duplicates_naive([1, 2, 3, 4, 5])
print(f"Duplicate: {found}, comparisons: {checks}")  # False, 10
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
