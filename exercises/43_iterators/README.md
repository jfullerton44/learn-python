# Exercise 43: Iterators and Generators

## Concept

Iterators and generators enable lazy evaluation and memory-efficient data processing.

### Key Concepts

1. **Iterator protocol**: `__iter__` and `__next__`
2. **Generators**: Functions with `yield`
3. **Generator expressions**: Lazy comprehensions
4. **itertools**: Advanced iteration utilities

## AI/ML Application

- Lazy data loading
- Infinite data streams
- Memory-efficient batch processing

## Code Examples

### Custom Iterator Class

```python
class Countdown:
    """Iterator that counts down from a start number to 1."""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for num in Countdown(5):
    print(num, end=" ")  # 5 4 3 2 1
```

### Generator Function with yield

```python
def fibonacci(limit):
    """Generate Fibonacci numbers up to a limit."""
    a, b = 0, 1
    while a < limit:
        yield a        # Pause here, return value, resume on next call
        a, b = b, a + b

for num in fibonacci(50):
    print(num, end=" ")  # 0 1 1 2 3 5 8 13 21 34

# Generators are lazy — values are computed on demand, not stored in memory
```

### Generator Expressions

```python
# Generator expressions look like list comprehensions but use ()
squares_list = [x**2 for x in range(10)]   # Creates a list in memory
squares_gen  = (x**2 for x in range(10))   # Creates a lazy generator

print(type(squares_gen))  # <class 'generator'>
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1

# Useful for large data — process without loading everything into memory
total = sum(x**2 for x in range(1_000_000))  # Memory-efficient
```

### itertools Utilities

```python
import itertools

# chain: combine multiple iterables into one sequence
combined = list(itertools.chain([1, 2], [3, 4], [5]))
print(combined)  # [1, 2, 3, 4, 5]

# islice: take a slice from any iterable (like slicing a generator)
first_five = list(itertools.islice(range(100), 5))
print(first_five)  # [0, 1, 2, 3, 4]

# product: cartesian product of iterables
pairs = list(itertools.product("AB", [1, 2]))
print(pairs)  # [('A', 1), ('A', 2), ('B', 1), ('B', 2)]

# count: infinite counter (use with islice to limit)
evens = list(itertools.islice(itertools.count(0, 2), 5))
print(evens)  # [0, 2, 4, 6, 8]
```

## Your Task

1. `example_function()` - Demonstrate efficient iteration
2. `Iterator` class - Custom iterator implementation
   - `__init__(self, data)`: Store data and initialize index
   - `__iter__(self)`: Return self
   - `__next__(self)`: Return next item or raise StopIteration

## Testing
```bash
pytest exercises/43_iterators/test_*.py -v
```
