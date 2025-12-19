# Exercise 46: Async/Await

## Concept

Asyncio enables asynchronous programming for efficient I/O operations using coroutines and an event loop.

### Key Concepts

1. **async/await**: Define and call coroutines
2. **Event loop**: Manages coroutine execution
3. **asyncio.gather()**: Run multiple coroutines concurrently
4. **Async context managers**: async with

## AI/ML Application

- Async API calls for inference
- Concurrent data fetching
- Non-blocking I/O operations

## Your Task

1. `worker_function()` - Sync worker for comparison
2. `async_worker()` - Async coroutine using `await asyncio.sleep()`
3. `ThreadPool` class - Thread-based pool for comparison

## Testing
```bash
pytest exercises/46_asyncio/test_*.py -v
```
