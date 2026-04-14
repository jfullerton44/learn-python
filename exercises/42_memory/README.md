# Exercise 42: Memory Management

## Concept

Understanding Python's memory model helps write efficient code for large-scale ML workloads.

### Key Concepts

1. **Reference counting**: How Python tracks object usage
2. **Garbage collection**: Automatic memory cleanup
3. **Memory profiling**: Measure memory usage
4. **Generators**: Memory-efficient iteration

## AI/ML Application

- Processing large datasets
- Avoiding memory leaks in training
- Efficient data pipelines

## Code Examples

### Checking Reference Counts

```python
import sys

a = [1, 2, 3]
print(sys.getrefcount(a))  # Typically 2 (a + the getrefcount arg)

b = a              # Another reference to the same list
print(sys.getrefcount(a))  # Now 3

del b              # Remove one reference
print(sys.getrefcount(a))  # Back to 2
```

### Measuring Object Size

```python
import sys

# sys.getsizeof returns the size of an object in bytes
print(sys.getsizeof(42))          # ~28 bytes (int)
print(sys.getsizeof("hello"))     # ~54 bytes (str)
print(sys.getsizeof([1, 2, 3]))   # ~120 bytes (list overhead + pointers)

# Compare container sizes
small_list = list(range(10))
big_list = list(range(10_000))
print(sys.getsizeof(small_list))   # ~184 bytes
print(sys.getsizeof(big_list))     # ~87,624 bytes
```

### Generator vs List Memory Usage

```python
import sys

# A list stores ALL elements in memory at once
nums_list = [x * x for x in range(1_000_000)]
print(sys.getsizeof(nums_list))  # ~8 MB

# A generator produces elements one at a time — constant memory
nums_gen = (x * x for x in range(1_000_000))
print(sys.getsizeof(nums_gen))   # ~200 bytes (just the generator object)

# Both can be iterated the same way
total = sum(x * x for x in range(1_000_000))  # Memory-efficient
```

### Using __slots__ to Reduce Memory

```python
import sys

class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedPoint:
    __slots__ = ("x", "y")  # No __dict__, fixed attributes
    def __init__(self, x, y):
        self.x = x
        self.y = y

r = RegularPoint(1, 2)
s = SlottedPoint(1, 2)

# Slotted objects use significantly less memory
print(sys.getsizeof(r) + sys.getsizeof(r.__dict__))  # ~200 bytes
print(sys.getsizeof(s))                                # ~56 bytes

# Especially impactful when creating millions of instances
```

## Your Task

1. `example_function()` - Demonstrate memory-efficient computation
2. `Iterator` class - Memory-efficient iterator pattern
   - Implement `__iter__` and `__next__` methods

## Testing
```bash
pytest exercises/42_memory/test_*.py -v
```
