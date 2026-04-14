# Exercise 41: Advanced NumPy

## Concept

Advanced NumPy techniques for high-performance numerical computing and ML workloads.

### Key Concepts

1. **Broadcasting**: Automatic array shape expansion
2. **Vectorization**: Replace loops with array operations
3. **Memory views**: Efficient array slicing
4. **Advanced indexing**: Boolean and integer arrays

## AI/ML Application

- Optimizing tensor operations
- Efficient batch processing
- Memory-efficient data handling

## Code Examples

### Broadcasting

```python
import numpy as np

# Broadcasting lets NumPy operate on arrays of different shapes
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])   # Shape: (2, 3)
row_vector = np.array([10, 20, 30])  # Shape: (3,)

# The row vector is "broadcast" across each row of the matrix
result = matrix + row_vector
print(result)
# [[11 22 33]
#  [14 25 36]]

# Subtract the column mean from each column
col_means = matrix.mean(axis=0)  # Shape: (3,)
centered = matrix - col_means
print(centered)
# [[-1.5 -1.5 -1.5]
#  [ 1.5  1.5  1.5]]
```

### Vectorized Operations vs Loops

```python
import numpy as np

data = np.random.rand(1_000_000)

# Slow: Python loop
def normalize_loop(arr):
    result = np.empty_like(arr)
    mean = arr.mean()
    std = arr.std()
    for i in range(len(arr)):
        result[i] = (arr[i] - mean) / std
    return result

# Fast: Vectorized (runs in optimized C under the hood)
def normalize_vectorized(arr):
    return (arr - arr.mean()) / arr.std()

# The vectorized version is typically 50-100x faster
result = normalize_vectorized(data)
```

### Fancy (Integer Array) Indexing

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Select elements at specific positions using an index array
indices = np.array([0, 3, 4])
print(arr[indices])  # [10 40 50]

# Works with 2D arrays too — select specific rows
matrix = np.arange(12).reshape(3, 4)
print(matrix[[0, 2]])
# [[ 0  1  2  3]
#  [ 8  9 10 11]]
```

### Boolean Indexing

```python
import numpy as np

temperatures = np.array([18.5, 22.1, 35.0, 29.3, 15.2, 40.1])

# Create a boolean mask and use it to filter
hot_days = temperatures[temperatures > 30]
print(hot_days)  # [35.  40.1]

# Combine conditions with & (and), | (or)
mild = temperatures[(temperatures > 20) & (temperatures < 35)]
print(mild)  # [22.1 29.3]

# Replace values conditionally
capped = np.where(temperatures > 30, 30, temperatures)
print(capped)  # [18.5 22.1 30.  29.3 15.2 30. ]
```

## Your Task

1. `example_function()` - Demonstrate vectorized computation
2. `Iterator` class - Custom iterator for array processing
   - Implement `__iter__` and `__next__` methods

## Testing
```bash
pytest exercises/41_numpy_advanced/test_*.py -v
```
