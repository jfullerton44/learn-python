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
def debug(func):
    """Decorator that prints arguments and return value."""
    def wrapper(*args, **kwargs):
        arg_str = ", ".join(
            [repr(a) for a in args] +
            [f"{k}={v!r}" for k, v in kwargs.items()]
        )
        print(f"→ {func.__name__}({arg_str})")
        result = func(*args, **kwargs)
        print(f"← {func.__name__} returned {result!r}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

add(3, 7)
# → add(3, 7)
# ← add returned 10
```

### Preserving Metadata with functools.wraps

```python
import functools

def count_calls(func):
    """Decorator that tracks how many times a function is called."""
    @functools.wraps(func)  # Preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"{func.__name__} has been called {wrapper.call_count} time(s)")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@count_calls
def compute_area(radius):
    """Compute the area of a circle."""
    return 3.14159 * radius ** 2

compute_area(5)   # compute_area has been called 1 time(s)
compute_area(10)  # compute_area has been called 2 time(s)

# Without @wraps, these would show 'wrapper' info instead
print(compute_area.__name__)  # compute_area
print(compute_area.__doc__)   # Compute the area of a circle.
```

### Decorator Factory (Decorator with Arguments)

```python
import functools

def require_role(role):
    """Decorator factory: only run the function if user has the right role."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") != role:
                raise PermissionError(
                    f"{func.__name__} requires role '{role}', "
                    f"got '{user.get('role')}'"
                )
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def delete_record(user, record_id):
    return f"Record {record_id} deleted by {user['name']}"

admin = {"name": "Alice", "role": "admin"}
print(delete_record(admin, 42))  # Record 42 deleted by Alice

guest = {"name": "Bob", "role": "viewer"}
# delete_record(guest, 42)  # PermissionError
```

### Stacking Decorators

```python
import functools

def memoize(func):
    """Cache results based on arguments."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
@debug          # using debug from above
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# debug runs first (inner), then memoize caches the result (outer)
print(fibonacci(6))  # 8 — debug prints only on cache misses
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
