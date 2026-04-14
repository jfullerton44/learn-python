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

## Code Examples

### Creating a Process

```python
import multiprocessing

def compute(n):
    print(f"Process computing {n} ** 2 = {n ** 2}")

# Each process runs in its own memory space
p = multiprocessing.Process(target=compute, args=(10,))
p.start()
p.join()  # Wait for process to finish
```

### Using Pool.map() for Parallel Work

```python
from multiprocessing import Pool

def square(x):
    return x ** 2

# Pool distributes work across multiple processes
if __name__ == "__main__":
    with Pool(processes=4) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
    print(results)  # [1, 4, 9, 16, 25]
```

### Sharing Data Between Processes with a Queue

```python
from multiprocessing import Process, Queue

def producer(queue):
    for item in ["apple", "banana", "cherry"]:
        queue.put(item)

def consumer(queue, results):
    while not queue.empty():
        results.append(queue.get())

if __name__ == "__main__":
    queue = Queue()
    p = Process(target=producer, args=(queue,))
    p.start()
    p.join()
    # Now consume the items
    while not queue.empty():
        print(queue.get())
```

### Process vs Thread — When to Use Each

```python
# Use THREADS for I/O-bound tasks (network, file I/O)
# The GIL allows threads to release during I/O waits
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(lambda url: url, ["url1", "url2"])

# Use PROCESSES for CPU-bound tasks (math, data crunching)
# Each process has its own Python interpreter and GIL
from concurrent.futures import ProcessPoolExecutor
def heavy_math(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(heavy_math, [10**6, 10**6]))
```

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
