# Exercise 55: Algorithms and Data Structures

## Concept

Understanding fundamental algorithms and data structures for efficient ML implementations.

### Key Concepts

1. **Sorting algorithms**: Quicksort, mergesort
2. **Search algorithms**: Binary search, hash tables
3. **Graph algorithms**: BFS, DFS
4. **Dynamic programming**: Memoization, tabulation

## AI/ML Application

- Efficient nearest neighbor search
- Graph-based models
- Optimization algorithms

## Code Examples

### Binary Search

```python
def binary_search(sorted_list, target):
    """Find target in a sorted list, return index or -1."""
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(binary_search(data, 23))  # 5
print(binary_search(data, 10))  # -1
```

### Graph Traversal — BFS and DFS

```python
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [], "E": [], "F": [],
}

def bfs(graph, start):
    """Breadth-first search — explores level by level."""
    visited, queue = set(), deque([start])
    order = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend(graph[node])
    return order

def dfs(graph, start, visited=None):
    """Depth-first search — explores as deep as possible first."""
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result

print(bfs(graph, "A"))  # ['A', 'B', 'C', 'D', 'E', 'F']
print(dfs(graph, "A"))  # ['A', 'B', 'D', 'E', 'C', 'F']
```

### Dynamic Programming — Memoization

```python
from functools import lru_cache

# Fibonacci with memoization avoids redundant computation
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))  # 55
print(fib(50))  # 12586269025  (computed instantly with caching)
```

## Your Task

1. `MLComponent` class - Algorithm component
2. `Pipeline` class - Algorithm pipeline
3. `create_component(name)` - Factory
4. `validate_config(config)` - Validation

## Testing
```bash
pytest exercises/55_algorithms/test_algorithms.py -v
```
