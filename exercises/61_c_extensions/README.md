# Exercise 61: C Extensions

## Concept

C extensions enable performance-critical code in Python through Cython, ctypes, or the C API.

### Key Concepts

1. **Cython**: Python-like syntax compiled to C
2. **ctypes**: Call C libraries from Python
3. **Performance**: 10-100x speedups for numerical code
4. **Integration**: Wrap existing C/C++ libraries

## AI/ML Application

- Custom CUDA kernels
- Optimized preprocessing
- Integrating C++ ML libraries

## Code Examples

### ctypes Basic Usage — Calling C from Python

```python
import ctypes

# Load the standard C math library
libm = ctypes.CDLL("libm.so.6")  # Linux; use "libSystem.B.dylib" on macOS

# Call the C sqrt function
libm.sqrt.restype = ctypes.c_double
libm.sqrt.argtypes = [ctypes.c_double]

result = libm.sqrt(ctypes.c_double(25.0))
print(result)  # 5.0
```

### ctypes — Defining Structures

```python
import ctypes

class Point(ctypes.Structure):
    """Mirror a C struct in Python."""
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]

p = Point(3.0, 4.0)
print(f"Point({p.x}, {p.y})")  # Point(3.0, 4.0)
```

### Performance Comparison — Pure Python vs. Optimized

```python
import time

# Pure Python dot product
def dot_product_python(a, b):
    total = 0.0
    for x, y in zip(a, b):
        total += x * y
    return total

# Using built-in sum (C-optimized internally)
def dot_product_builtin(a, b):
    return sum(x * y for x, y in zip(a, b))

size = 1_000_000
a = list(range(size))
b = list(range(size))

start = time.perf_counter()
dot_product_python(a, b)
py_time = time.perf_counter() - start

start = time.perf_counter()
dot_product_builtin(a, b)
builtin_time = time.perf_counter() - start

print(f"Pure loop:  {py_time:.4f}s")
print(f"Built-in:   {builtin_time:.4f}s")
# C extensions (numpy, ctypes) can provide even larger speedups
```

## Your Task

1. `MLComponent` class - Component for C extension wrapping
2. `Pipeline` class - Pipeline with C-optimized stages
3. `create_component(name)` - Factory
4. `validate_config(config)` - Validation

## Testing
```bash
pytest exercises/61_c_extensions/test_c_extensions.py -v
```
