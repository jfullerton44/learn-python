"""Exercise 33: Data Preprocessing"""
import numpy as np

def normalize_features(data):
    """Min-max normalization to [0, 1]"""
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    return (data - min_val) / (max_val - min_val + 1e-8)

def standardize_features(data):
    """Z-score normalization"""
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    return (data - mean) / (std + 1e-8)

def one_hot_encode(labels, num_classes):
    """One-hot encode labels"""
    n = len(labels)
    encoded = np.zeros((n, num_classes))
    encoded[np.arange(n), labels] = 1
    return encoded

def split_train_val_test(data, train_ratio=0.7, val_ratio=0.15):
    """Split data into train/val/test"""
    n = len(data)
    train_end = int(n * train_ratio)
    val_end = int(n * (train_ratio + val_ratio))
    return data[:train_end], data[train_end:val_end], data[val_end:]
