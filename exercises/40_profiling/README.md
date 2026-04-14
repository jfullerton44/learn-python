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

## Code Examples

### Using cProfile

```python
import cProfile

def compute():
    total = sum(x * x for x in range(100_000))
    return total

# Profile a function and print a summary of calls and timings
cProfile.run("compute()")
# Output shows: ncalls, tottime, percall, cumtime, etc.

# Save profiling results to a file for later analysis
cProfile.run("compute()", "profile_output.prof")

# For finer control, use the Profile object directly
profiler = cProfile.Profile()
profiler.enable()
compute()
profiler.disable()
profiler.print_stats(sort="cumulative")
```

### Using timeit

```python
import timeit

# Time a small code snippet (runs many iterations for accuracy)
elapsed = timeit.timeit("sum(range(1000))", number=10_000)
print(f"10,000 runs took {elapsed:.4f}s")

# Compare two approaches
time_loop = timeit.timeit(
    "total = 0\nfor i in range(1000): total += i",
    number=10_000,
)
time_builtin = timeit.timeit("sum(range(1000))", number=10_000)

print(f"Manual loop: {time_loop:.4f}s")
print(f"Built-in sum: {time_builtin:.4f}s")
# Built-in sum is typically much faster
```

### Interpreting Profiling Results

```python
import cProfile
import pstats
import io

def slow_function():
    return sorted([i ** 0.5 for i in range(50_000)])

def fast_function():
    return list(range(50_000))

def main():
    slow_function()
    fast_function()

# Capture and sort profiling stats programmatically
stream = io.StringIO()
profiler = cProfile.Profile()
profiler.enable()
main()
profiler.disable()

stats = pstats.Stats(profiler, stream=stream)
stats.sort_stats("cumulative")
stats.print_stats(5)  # Show top 5 functions by cumulative time
print(stream.getvalue())
# Focus optimization on functions with the highest cumtime
```

## Your Task

1. `example_function()` - Create a function to profile (e.g., sum of range)
2. `Iterator` class - Custom iterator to understand iteration overhead
   - Implement `__iter__` and `__next__` methods

## Testing
```bash
pytest exercises/40_profiling/test_*.py -v
```
