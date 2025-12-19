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
