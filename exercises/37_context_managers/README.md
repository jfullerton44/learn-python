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

## Your Task

1. `FileManager` class - Context manager for file operations with `__enter__` and `__exit__`
2. `GPUMemoryManager` class - Simulates GPU allocation/release
3. `training_mode()` - Generator-based context manager using @contextmanager

## Testing
```bash
pytest exercises/37_context_managers/test_context_managers.py -v
```
