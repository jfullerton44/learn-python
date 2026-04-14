# Exercise 54: Advanced Collections

## Concept

Python's collections module provides specialized container types for efficient data handling.

### Key Concepts

1. **namedtuple**: Immutable records with names
2. **defaultdict**: Auto-initializing dictionaries
3. **Counter**: Count occurrences
4. **deque**: Efficient double-ended queue

## AI/ML Application

- Metrics tracking with Counter
- Feature caching with defaultdict
- Sliding window with deque

## Code Examples

### namedtuple — Immutable Records with Named Fields

```python
from collections import namedtuple

# Define a lightweight record type for model metrics
Metric = namedtuple("Metric", ["name", "value", "epoch"])

m = Metric(name="accuracy", value=0.95, epoch=10)
print(m.name)    # "accuracy"
print(m.epoch)   # 10
# Namedtuples are immutable — m.value = 0.99 would raise AttributeError
```

### defaultdict — Auto-Initializing Dictionary

```python
from collections import defaultdict

# Group predictions by label without checking key existence
predictions = [("cat", 0.9), ("dog", 0.8), ("cat", 0.7), ("dog", 0.6)]

by_label = defaultdict(list)
for label, score in predictions:
    by_label[label].append(score)

print(dict(by_label))  # {'cat': [0.9, 0.7], 'dog': [0.8, 0.6]}
```

### Counter — Counting Occurrences

```python
from collections import Counter

# Count word frequencies in a dataset
words = ["the", "cat", "sat", "on", "the", "mat", "the"]
freq = Counter(words)

print(freq.most_common(2))  # [('the', 3), ('cat', 1)]
print(freq["the"])           # 3
```

### deque — Efficient Double-Ended Queue

```python
from collections import deque

# Sliding window of recent loss values
recent_losses = deque(maxlen=3)
for loss in [0.9, 0.7, 0.5, 0.3, 0.2]:
    recent_losses.append(loss)

print(list(recent_losses))  # [0.3, 0.2] — wait, maxlen=3 → [0.5, 0.3, 0.2]
# deque also supports efficient appendleft() and popleft()
```

### OrderedDict — Insertion-Ordered Dictionary

```python
from collections import OrderedDict

# Track layer parameters in insertion order
layers = OrderedDict()
layers["input"] = 784
layers["hidden"] = 128
layers["output"] = 10

# Move a layer to the end
layers.move_to_end("input")
print(list(layers.keys()))  # ['hidden', 'output', 'input']
```

## Your Task

1. `MLComponent` class - Component using collections
2. `Pipeline` class - Pipeline with deque for stages
3. `create_component(name)` - Factory function
4. `validate_config(config)` - Validation

## Testing
```bash
pytest exercises/54_collections/test_collections.py -v
```
