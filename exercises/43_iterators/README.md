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
