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

## Code Examples

### Basic Coroutine with async/await

```python
import asyncio

async def fetch_data(source):
    print(f"Fetching from {source}...")
    await asyncio.sleep(1)  # Simulate async I/O
    return f"Data from {source}"

# Run a single coroutine
result = asyncio.run(fetch_data("database"))
print(result)  # "Data from database"
```

### Running Multiple Coroutines Concurrently with gather()

```python
import asyncio

async def download(url):
    await asyncio.sleep(0.5)
    return f"Downloaded {url}"

async def main():
    # gather() runs coroutines concurrently, not sequentially
    results = await asyncio.gather(
        download("page1.html"),
        download("page2.html"),
        download("page3.html"),
    )
    print(results)  # All three finish in ~0.5s, not ~1.5s

asyncio.run(main())
```

### Using asyncio.run() as the Entry Point

```python
import asyncio

async def greet(name):
    await asyncio.sleep(0.1)
    return f"Hello, {name}!"

# asyncio.run() creates an event loop, runs the coroutine, and cleans up
message = asyncio.run(greet("World"))
print(message)
```

### Async Context Manager

```python
import asyncio

class AsyncConnection:
    def __init__(self, host):
        self.host = host

    async def __aenter__(self):
        print(f"Connecting to {self.host}...")
        await asyncio.sleep(0.1)  # Simulate async connect
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.host}")
        await asyncio.sleep(0.1)  # Simulate async close

    async def query(self, sql):
        await asyncio.sleep(0.1)
        return f"Results for: {sql}"

async def main():
    async with AsyncConnection("localhost") as conn:
        result = await conn.query("SELECT * FROM users")
        print(result)

asyncio.run(main())
```

## Your Task

1. `worker_function()` - Sync worker for comparison
2. `async_worker()` - Async coroutine using `await asyncio.sleep()`
3. `ThreadPool` class - Thread-based pool for comparison

## Testing
```bash
pytest exercises/46_asyncio/test_*.py -v
```
