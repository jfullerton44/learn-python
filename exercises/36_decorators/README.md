# Exercise 36: Decorators

## Concept

Decorators modify or enhance functions without changing their code. They're essential for cross-cutting concerns like logging, timing, and caching.

### Key Concepts

1. **Basic decorators**: Wrap functions to add behavior
2. **functools.wraps**: Preserve function metadata
3. **Decorators with arguments**: Create decorator factories
4. **Stacking decorators**: Apply multiple decorators

## AI/ML Application

- Timing training functions
- Logging function calls
- Retry logic for API calls
- Caching expensive computations

## Code Examples

### Basic Decorator

```python
import time

def timer(func):
    """Decorator that measures execution time."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

slow_sum(1_000_000)  # slow_sum took 0.0312s
```

### Preserving Metadata with functools.wraps

```python
import functools

def log_calls(func):
    @functools.wraps(func)  # Preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}({args}, {kwargs})")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}!"

# Without @wraps, these would show 'wrapper' info instead
print(greet.__name__)  # greet
print(greet.__doc__)   # Return a greeting string.
```

### Decorator Factory (Decorator with Arguments)

```python
import functools

def repeat(n):
    """Decorator factory: run the function n times, return list of results."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(n)]
        return wrapper
    return decorator

@repeat(3)
def roll_dice():
    import random
    return random.randint(1, 6)

print(roll_dice())  # e.g. [4, 2, 6]
```

### Stacking Decorators

```python
import functools

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

# Decorators apply bottom-up: italic first, then bold wraps the result
@bold
@italic
def say(text):
    return text

print(say("hello"))  # <b><i>hello</i></b>
```

## Your Task

1. `timer(func)` - Decorator that prints execution time
2. `repeat(n)` - Decorator factory that runs function n times, returns list of results
3. `log_calls(func)` - Decorator that logs function calls
4. Apply decorators to example functions

## Testing
```bash
pytest exercises/36_decorators/test_decorators.py -v
```
