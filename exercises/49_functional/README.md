# Exercise 49: Functional Programming

## Concept

Functional programming emphasizes pure functions, immutability, and function composition for cleaner, more testable code.

### Key Concepts

1. **Pure functions**: No side effects
2. **Immutability**: Don't modify data
3. **Higher-order functions**: Functions as arguments/returns
4. **Function composition**: Chain functions together

## AI/ML Application

- Data transformation pipelines
- Reproducible computations
- Parallel-safe operations

## Code Examples

### Pure vs Impure Functions

```python
# IMPURE — modifies external state
total = 0
def add_to_total(x):
    global total
    total += x     # Side effect: changes global variable
    return total

# PURE — same inputs always produce the same output, no side effects
def add(a, b):
    return a + b   # No external state modified

print(add(3, 4))   # Always 7
print(add(3, 4))   # Always 7
```

### Higher-Order Functions

```python
# A function that takes a function as an argument
def apply_to_all(func, items):
    return [func(item) for item in items]

print(apply_to_all(str.upper, ["hello", "world"]))  # ["HELLO", "WORLD"]
print(apply_to_all(lambda x: x ** 2, [1, 2, 3]))    # [1, 4, 9]

# A function that returns a function
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)
print(double(5))   # 10
```

### Function Composition

```python
def compose(*funcs):
    """Compose functions right-to-left: compose(f, g)(x) == f(g(x))."""
    def composed(value):
        for func in reversed(funcs):
            value = func(value)
        return value
    return composed

def strip_whitespace(s): return s.strip()
def lowercase(s): return s.lower()
def remove_punctuation(s): return "".join(c for c in s if c.isalnum() or c == " ")

clean = compose(remove_punctuation, lowercase, strip_whitespace)
print(clean("  Hello, World!  "))  # "hello world"
```

### Partial Application with functools.partial

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(3))    # 27
```

## Your Task

1. `MLComponent` class - Functional component with pure process method
2. `Pipeline` class - Compose components functionally
3. `create_component(name)` - Factory function
4. `validate_config(config)` - Functional validation

## Testing
```bash
pytest exercises/49_functional/test_functional.py -v
```
