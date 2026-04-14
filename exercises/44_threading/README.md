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

## Code Examples

### Creating and Starting a Thread

```python
import threading

def greet(name):
    print(f"Hello from {name}")

# Create and start a thread
thread = threading.Thread(target=greet, args=("worker-1",))
thread.start()
thread.join()  # Wait for thread to finish
print("Thread completed")
```

### Joining Multiple Threads

```python
import threading
import time

def download(url):
    time.sleep(0.5)  # Simulate I/O work
    return f"Downloaded {url}"

threads = []
for url in ["page1.html", "page2.html", "page3.html"]:
    t = threading.Thread(target=download, args=(url,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()
print("All downloads complete")
```

### Using a Lock for Thread-Safe Access

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000):
        with lock:  # Only one thread enters this block at a time
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Counter: {counter}")  # Always 5000 with the lock
```

### Simple Thread Pool Pattern

```python
import threading
from concurrent.futures import ThreadPoolExecutor

def process_item(item):
    return item * 2

# ThreadPoolExecutor manages a pool of worker threads
with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(process_item, [1, 2, 3, 4, 5]))
print(results)  # [2, 4, 6, 8, 10]
```

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
