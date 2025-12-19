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

## Your Task

1. `normalize_features(data)` - Min-max normalize to [0, 1]
2. `standardize_features(data)` - Z-score standardization
3. `one_hot_encode(labels, num_classes)` - One-hot encode integer labels
4. `split_train_val_test(data, train_ratio, val_ratio)` - Split into 3 sets

## Testing
```bash
pytest exercises/33_preprocessing/test_preprocessing.py -v
```
