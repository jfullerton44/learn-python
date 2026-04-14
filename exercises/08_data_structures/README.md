# Exercise 8: Basic Data Structures

## Concept
Master lists, tuples, sets, dicts - when to use each, trade-offs.

## AI/ML Application
- Storing predictions and labels
- Managing hyperparameters
- Caching computed results
- Deduplication of data

## Code Examples

### Lists — Ordered, Mutable Sequences
```python
predictions = [0.9, 0.3, 0.7]
predictions.append(0.5)       # [0.9, 0.3, 0.7, 0.5]
predictions.sort()             # [0.3, 0.5, 0.7, 0.9]
top = predictions[-1]          # 0.9
```

### Tuples — Immutable Ordered Sequences
```python
# Use tuples for fixed collections (e.g., coordinate pairs)
point = (3, 4)
x, y = point  # unpacking: x=3, y=4

# Tuples as dict keys (lists can't be used)
grid = {(0, 0): "start", (1, 2): "end"}

# Zip predictions and labels together
preds = [0.9, 0.4, 0.8]
labels = [1, 0, 1]
pairs = list(zip(preds, labels))  # [(0.9, 1), (0.4, 0), (0.8, 1)]
```

### Sets — Unordered, Unique Elements
```python
seen = {1, 2, 3, 2, 1}
print(seen)  # {1, 2, 3}

a = {"cat", "dog", "bird"}
b = {"dog", "fish"}
print(a & b)  # intersection: {'dog'}
print(a | b)  # union: {'cat', 'dog', 'bird', 'fish'}
```

### Dicts — Key-Value Mappings
```python
config = {"lr": 0.001, "epochs": 10, "batch_size": 32}
config["dropout"] = 0.5          # add a key
lr = config.get("lr", 0.01)      # safe access with default

# Iterate over keys and values
for key, value in config.items():
    print(f"{key}: {value}")
```

### When to Use Each
```python
# List  — ordered collection, allows duplicates
# Tuple — fixed record, hashable (usable as dict key)
# Set   — membership testing, deduplication
# Dict  — lookup by key, configuration, caching
```

### Stacks and Queues
```python
# Stack (LIFO) — use a plain list
stack = []
stack.append("a")
stack.append("b")
top = stack.pop()  # "b"

# Queue (FIFO) — use collections.deque for O(1) pops
from collections import deque
queue = deque()
queue.append("first")
queue.append("second")
front = queue.popleft()  # "first"
```

## Your Task
1. `store_predictions(predictions, labels)` - Return list of tuples (pred, label)
2. `manage_hyperparams()` - Return dict with nested structure
3. `deduplicate_samples(samples)` - Use set to remove duplicates, return list
4. `cache_results(func, args_list)` - Cache function results in dict
5. `implement_stack()` - Return list with push/pop operations
6. `implement_queue()` - Use collections.deque for queue operations

## Testing
```bash
pytest exercises/08_data_structures/test_data_structures.py -v
```
