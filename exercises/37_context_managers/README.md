# Exercise 37: Context Managers

## Concept

Context managers handle resource setup and cleanup using `with` statements. They ensure resources are properly released even if exceptions occur.

### Key Concepts

1. **`__enter__`/`__exit__`**: Protocol for context managers
2. **contextlib.contextmanager**: Decorator for generator-based context managers
3. **Resource management**: Files, connections, GPU memory

## AI/ML Application

- GPU memory management
- Database connections
- Training mode switching
- Timer contexts

## Code Examples

### Class-Based Context Manager (__enter__ / __exit__)

```python
class ManagedFile:
    """Context manager that safely opens and closes a file."""
    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file  # This is bound to the 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Returning False re-raises any exception; True suppresses it
        return False

# Usage: file is guaranteed to close even if an error occurs
with ManagedFile("example.txt", "w") as f:
    f.write("Hello, context managers!")
```

### Generator-Based Context Manager (contextlib)

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(label):
    """Time a block of code using a with statement."""
    start = time.time()
    yield  # Code inside the 'with' block runs here
    elapsed = time.time() - start
    print(f"{label}: {elapsed:.4f}s")

with timer("Processing"):
    total = sum(range(1_000_000))
# Processing: 0.0289s
```

### Practical Resource Management

```python
from contextlib import contextmanager

@contextmanager
def database_connection(db_name):
    """Simulate acquiring and releasing a database connection."""
    print(f"Connecting to {db_name}...")
    conn = {"db": db_name, "connected": True}
    try:
        yield conn  # Provide the connection to the with-block
    finally:
        # Cleanup always runs, even on exceptions
        conn["connected"] = False
        print(f"Disconnected from {db_name}")

with database_connection("users_db") as conn:
    print(f"Querying {conn['db']}...")
# Connecting to users_db...
# Querying users_db...
# Disconnected from users_db
```

## Your Task

1. `FileManager` class - Context manager for file operations with `__enter__` and `__exit__`
2. `GPUMemoryManager` class - Simulates GPU allocation/release
3. `training_mode()` - Generator-based context manager using @contextmanager

## Testing
```bash
pytest exercises/37_context_managers/test_context_managers.py -v
```
