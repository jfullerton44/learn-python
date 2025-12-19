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

## Your Task

1. `example_function()` - Demonstrate memory-efficient computation
2. `Iterator` class - Memory-efficient iterator pattern
   - Implement `__iter__` and `__next__` methods

## Testing
```bash
pytest exercises/42_memory/test_*.py -v
```
