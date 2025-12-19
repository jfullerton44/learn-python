# Exercise 40: Profiling

## Concept

Profiling identifies performance bottlenecks in your code. Python provides tools like cProfile, timeit, and line_profiler.

### Key Concepts

1. **cProfile**: Built-in profiler for function-level timing
2. **timeit**: Measure small code snippets
3. **Identifying bottlenecks**: Focus optimization efforts
4. **Baseline measurements**: Profile before optimizing

## AI/ML Application

- Finding slow functions in training loops
- Optimizing data preprocessing
- Measuring inference latency

## Your Task

1. `example_function()` - Create a function to profile (e.g., sum of range)
2. `Iterator` class - Custom iterator to understand iteration overhead
   - Implement `__iter__` and `__next__` methods

## Testing
```bash
pytest exercises/40_profiling/test_*.py -v
```
