# Exercise 60: Distributed Computing

## Concept

Distributed computing patterns for scaling ML workloads across multiple machines.

### Key Concepts

1. **Data parallelism**: Split data across workers
2. **Model parallelism**: Split model across devices
3. **Message passing**: Inter-process communication
4. **Coordination**: Synchronization and consensus

## AI/ML Application

- Distributed training
- Parallel preprocessing
- Inference scaling

## Code Examples

### Simulated Data Parallel Pattern

```python
import threading

def train_on_shard(worker_id, data_shard, results):
    """Simulate training on a data shard and returning gradients."""
    gradient = sum(data_shard) / len(data_shard)  # Fake gradient
    results[worker_id] = gradient

data = list(range(100))
num_workers = 4
shard_size = len(data) // num_workers
results = {}

threads = []
for i in range(num_workers):
    shard = data[i * shard_size : (i + 1) * shard_size]
    t = threading.Thread(target=train_on_shard, args=(i, shard, results))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Aggregate gradients from all workers
avg_gradient = sum(results.values()) / num_workers
print(f"Worker gradients: {results}")
print(f"Averaged gradient: {avg_gradient}")
```

### Message Passing Concept

```python
import queue
import threading

def producer(msg_queue, messages):
    """Send messages to other workers via a shared queue."""
    for msg in messages:
        msg_queue.put(msg)
    msg_queue.put(None)  # Sentinel to signal completion

def consumer(msg_queue):
    """Receive and process messages from the queue."""
    received = []
    while True:
        msg = msg_queue.get()
        if msg is None:
            break
        received.append(msg)
    return received

msg_queue = queue.Queue()
threading.Thread(target=producer, args=(msg_queue, ["grad_1", "grad_2"])).start()

# Consumer reads messages
results = consumer(msg_queue)
print(results)  # ['grad_1', 'grad_2']
```

### Coordinator Pattern

```python
import threading

class TrainingCoordinator:
    """Synchronize workers: all must finish before moving to next step."""
    def __init__(self, num_workers):
        self.barrier = threading.Barrier(num_workers)
        self.results = {}

    def worker_step(self, worker_id, data):
        # Each worker computes locally
        self.results[worker_id] = sum(data)
        # Wait for all workers to finish this step
        self.barrier.wait()

coord = TrainingCoordinator(num_workers=3)
threads = [
    threading.Thread(target=coord.worker_step, args=(i, [i, i + 1]))
    for i in range(3)
]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(coord.results)  # {0: 1, 1: 3, 2: 5}
```

## Your Task

1. `MLComponent` class - Distributed component
2. `Pipeline` class - Distributed pipeline
3. `create_component(name)` - Factory
4. `validate_config(config)` - Validation

## Testing
```bash
pytest exercises/60_distributed/test_distributed.py -v
```
