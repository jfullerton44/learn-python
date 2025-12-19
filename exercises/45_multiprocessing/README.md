# Exercise 45: Multiprocessing

## Concept

Multiprocessing uses separate processes for true parallelism, bypassing the GIL for CPU-bound tasks.

### Key Concepts

1. **Process**: Independent execution with own memory
2. **Pool**: Manage multiple worker processes
3. **Data sharing**: Queues, Pipes, shared memory
4. **Process vs Thread**: When to use each

## AI/ML Application

- Parallel data preprocessing
- Distributed model training
- CPU-intensive feature extraction

## Your Task

1. `worker_function()` - Process worker returning "completed"
2. `async_worker()` - Async version for comparison
3. `ThreadPool` class - Pool implementation (can use threads for simplicity)
   - `__init__(self, workers=4)`: Initialize worker count
   - `map(self, func, items)`: Map function over items

## Testing
```bash
pytest exercises/45_multiprocessing/test_*.py -v
```
