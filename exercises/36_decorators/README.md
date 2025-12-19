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

## Your Task

1. `timer(func)` - Decorator that prints execution time
2. `repeat(n)` - Decorator factory that runs function n times, returns list of results
3. `log_calls(func)` - Decorator that logs function calls
4. Apply decorators to example functions

## Testing
```bash
pytest exercises/36_decorators/test_decorators.py -v
```
