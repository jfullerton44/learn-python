# Exercise 44: Threading

## Concept

Threading enables concurrent execution within a single process. Useful for I/O-bound tasks due to Python's GIL.

### Key Concepts

1. **Thread**: Concurrent execution unit
2. **threading module**: Create and manage threads
3. **GIL (Global Interpreter Lock)**: Limits CPU-bound parallelism
4. **Thread synchronization**: Locks, events, conditions

## AI/ML Application

- Parallel data loading
- Concurrent API requests
- Background logging during training

## Your Task

1. `worker_function()` - Simple worker that returns "completed"
2. `async_worker()` - Async version of worker function
3. `ThreadPool` class - Simple thread pool with:
   - `__init__(self, workers=4)`: Store worker count
   - `map(self, func, items)`: Apply function to items using threads

## Testing
```bash
pytest exercises/44_threading/test_*.py -v
```
