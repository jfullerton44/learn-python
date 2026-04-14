# Exercise 59: Dataset Patterns

## Concept

Dataset patterns handle data loading, caching, batching, and preprocessing efficiently.

### Key Concepts

1. **Lazy loading**: Load data on demand
2. **Caching**: Memory and disk caching
3. **Batching**: Process in batches
4. **Augmentation**: Transform data on the fly

## AI/ML Application

- Training data pipelines
- Large dataset handling
- Real-time data augmentation

## Code Examples

### Lazy Loading — Load Data on Demand

```python
class LazyDataset:
    """Only loads items when accessed, not at initialization."""
    def __init__(self, file_paths):
        self._paths = file_paths
        self._cache = {}

    def __getitem__(self, index):
        if index not in self._cache:
            # Simulate reading from disk
            self._cache[index] = f"data_from_{self._paths[index]}"
        return self._cache[index]

    def __len__(self):
        return len(self._paths)

ds = LazyDataset(["file0.csv", "file1.csv", "file2.csv"])
print(ds[1])  # "data_from_file1.csv" — loaded on first access
print(ds[1])  # Returns cached version
```

### Cached Property Pattern

```python
class FeatureStore:
    """Compute expensive features once and cache them."""
    def __init__(self, raw_data):
        self._raw = raw_data
        self._features = None

    @property
    def features(self):
        if self._features is None:
            print("Computing features...")
            self._features = [x ** 2 for x in self._raw]
        return self._features

store = FeatureStore([1, 2, 3, 4])
print(store.features)  # Computes: [1, 4, 9, 16]
print(store.features)  # Returns cached result without recomputing
```

### Batch Iterator

```python
def batch_iterator(data, batch_size):
    """Yield data in fixed-size batches."""
    for i in range(0, len(data), batch_size):
        yield data[i : i + batch_size]

samples = list(range(10))
for batch in batch_iterator(samples, batch_size=3):
    print(batch)
# [0, 1, 2]
# [3, 4, 5]
# [6, 7, 8]
# [9]
```

### Data Augmentation Pipeline

```python
import random

def add_noise(value, scale=0.1):
    return value + random.gauss(0, scale)

def normalize(value, mean=0.0, std=1.0):
    return (value - mean) / std

def augmentation_pipeline(data, transforms):
    """Apply a sequence of transforms to each data point."""
    result = []
    for item in data:
        for fn in transforms:
            item = fn(item)
        result.append(item)
    return result

raw = [10.0, 20.0, 30.0]
augmented = augmentation_pipeline(raw, [add_noise, lambda x: normalize(x, 20, 10)])
print(augmented)  # Normalized values with noise added
```

## Your Task

1. `MLComponent` class - Dataset component
2. `Pipeline` class - Data pipeline
3. `create_component(name)` - Factory
4. `validate_config(config)` - Validation

## Testing
```bash
pytest exercises/59_dataset_patterns/test_dataset_patterns.py -v
```
