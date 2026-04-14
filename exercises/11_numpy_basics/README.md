# Exercise 11: NumPy Basics

## Concept
Array creation, indexing/slicing, common operations, basic matrix operations.

## AI/ML Application
Essential for tensor manipulation, numerical computations, data preprocessing.

## Code Examples

### Array Creation
```python
import numpy as np

a = np.array([1, 2, 3, 4])          # from a list
zeros = np.zeros((2, 3))             # 2×3 array of zeros
ones = np.ones((3,))                 # 1D array of ones
rng = np.arange(0, 10, 2)            # [0, 2, 4, 6, 8]
lin = np.linspace(0, 1, 5)           # [0.0, 0.25, 0.5, 0.75, 1.0]
```

### Indexing and Slicing
```python
arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print(arr[0, 1])     # 20       (row 0, col 1)
print(arr[:, 0])     # [10, 40] (all rows, col 0)
print(arr[1, :2])    # [40, 50] (row 1, first 2 cols)

# Select specific rows by index
rows = arr[[0, 1, 0]]  # rows 0, 1, 0
```

### Array Operations (Element-wise)
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)    # [5, 7, 9]
print(a * 2)    # [2, 4, 6]
print(a ** 2)   # [1, 4, 9]
print(np.mean(a))  # 2.0
print(np.std(a))   # 0.8165...
```

### Matrix Multiplication
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

product = A @ B  # or np.dot(A, B)
# [[19, 22],
#  [43, 50]]
```

### Reshaping
```python
arr = np.arange(12)          # [0, 1, 2, ..., 11]
matrix = arr.reshape(3, 4)   # 3 rows × 4 cols
flat = matrix.flatten()       # back to 1D
```

### Normalization (Min-Max Scaling)
```python
data = np.array([10, 20, 30, 40, 50], dtype=float)
normalized = (data - data.min()) / (data.max() - data.min())
# [0.0, 0.25, 0.5, 0.75, 1.0]
```

## Your Task
1. `create_array(values)` - Create NumPy array from list
2. `create_zeros(shape)` - Create array of zeros
3. `array_stats(arr)` - Return dict with mean, std, min, max
4. `normalize_array(arr)` - Normalize to range [0, 1]
5. `matrix_multiply(a, b)` - Multiply two matrices
6. `select_rows(arr, indices)` - Select rows by indices
7. `reshape_array(arr, new_shape)` - Reshape array

## Testing
```bash
pytest exercises/11_numpy_basics/test_numpy_basics.py -v
```
