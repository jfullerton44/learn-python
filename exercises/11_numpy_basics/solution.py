"""
Exercise 11: NumPy Basics
"""
import numpy as np
from typing import List, Tuple, Dict


def create_array(values: List) -> np.ndarray:
    """Create NumPy array from list."""
    return np.array(values)


def create_zeros(shape: Tuple) -> np.ndarray:
    """Create array of zeros with given shape."""
    return np.zeros(shape)


def array_stats(arr: np.ndarray) -> Dict[str, float]:
    """Return dictionary with mean, std, min, max of array."""
    return {
        "mean": float(np.mean(arr)),
        "std": float(np.std(arr)),
        "min": float(np.min(arr)),
        "max": float(np.max(arr))
    }


def normalize_array(arr: np.ndarray) -> np.ndarray:
    """Normalize array to range [0, 1]."""
    min_val = np.min(arr)
    max_val = np.max(arr)
    return (arr - min_val) / (max_val - min_val)


def matrix_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Multiply two matrices."""
    return np.matmul(a, b)


def select_rows(arr: np.ndarray, indices: List[int]) -> np.ndarray:
    """Select rows by indices."""
    return arr[indices]


def reshape_array(arr: np.ndarray, new_shape: Tuple) -> np.ndarray:
    """Reshape array to new shape."""
    return arr.reshape(new_shape)


if __name__ == "__main__":
    arr = create_array([1, 2, 3, 4, 5])
    print("Array:", arr)
    print("Stats:", array_stats(arr))
    print("Normalized:", normalize_array(arr))
