# Exercise 33: Data Preprocessing Basics

## Concept

Data preprocessing transforms raw data into a format suitable for ML models. Essential steps include normalization, encoding, and splitting.

### Key Concepts

1. **Normalization**: Scale features to [0, 1] range
2. **Standardization**: Z-score normalization (mean=0, std=1)
3. **One-hot encoding**: Convert categories to binary vectors
4. **Train/val/test split**: Divide data for training and evaluation

## AI/ML Application

- Preparing data for neural networks
- Handling categorical features
- Creating proper evaluation splits

## Code Examples

### Min-max normalization (scale to [0, 1])

```python
import numpy as np

data = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
normalized = (data - data.min()) / (data.max() - data.min())
print(normalized)  # [0.   0.25 0.5  0.75 1.  ]
```

### Z-score standardization (mean=0, std=1)

```python
import numpy as np

data = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
standardized = (data - data.mean()) / data.std()
print(f"Mean: {standardized.mean():.1f}, Std: {standardized.std():.1f}")
# Mean: 0.0, Std: 1.0
```

### One-hot encoding for categorical data

```python
import numpy as np

labels = [0, 2, 1, 0]  # 3 classes: 0, 1, 2
num_classes = 3

one_hot = np.zeros((len(labels), num_classes))
for i, label in enumerate(labels):
    one_hot[i, label] = 1.0

print(one_hot)
# [[1. 0. 0.]   ← class 0
#  [0. 0. 1.]   ← class 2
#  [0. 1. 0.]   ← class 1
#  [1. 0. 0.]]  ← class 0
```

### Splitting data into train, validation, and test sets

```python
import numpy as np

data = np.arange(100)
np.random.seed(42)
np.random.shuffle(data)

train_end = int(0.7 * len(data))   # 70% train
val_end = int(0.85 * len(data))    # 15% validation

train = data[:train_end]            # 70 samples
val = data[train_end:val_end]       # 15 samples
test = data[val_end:]               # 15 samples
print(f"Train: {len(train)}, Val: {len(val)}, Test: {len(test)}")
# Train: 70, Val: 15, Test: 15
```

## Your Task

1. `normalize_features(data)` - Min-max normalize to [0, 1]
2. `standardize_features(data)` - Z-score standardization
3. `one_hot_encode(labels, num_classes)` - One-hot encode integer labels
4. `split_train_val_test(data, train_ratio, val_ratio)` - Split into 3 sets

## Testing
```bash
pytest exercises/33_preprocessing/test_preprocessing.py -v
```
