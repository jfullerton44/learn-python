# Exercise 16: Argument Handling

## Concept

Python offers flexible argument handling with *args, **kwargs, keyword-only, and positional-only arguments for creating versatile function interfaces.

### Key Concepts

1. **`*args`**: Capture variable positional arguments as a tuple
2. **`**kwargs`**: Capture variable keyword arguments as a dict
3. **Keyword-only**: Arguments after `*` must be passed by keyword
4. **Positional-only**: Arguments before `/` must be passed by position (Python 3.8+)

## AI/ML Application

- Flexible model configuration functions
- Wrapper functions for training loops
- API design for ML libraries

## Code Examples

### `*args` — Variable Positional Arguments

```python
def total(*args):
    """Accepts any number of positional arguments as a tuple."""
    return sum(args)

print(total(1, 2, 3))      # 6
print(total(10, 20))        # 30
```

### `**kwargs` — Variable Keyword Arguments

```python
def print_settings(**kwargs):
    """Accepts any number of keyword arguments as a dict."""
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_settings(color="blue", size=12, bold=True)
# color = blue
# size = 12
# bold = True
```

### Default Values

```python
def connect(host: str, port: int = 5432, timeout: int = 30):
    return f"{host}:{port} (timeout={timeout}s)"

print(connect("localhost"))            # localhost:5432 (timeout=30s)
print(connect("db.example.com", 3306)) # db.example.com:3306 (timeout=30s)
```

### Keyword-Only Arguments (after `*`)

```python
def train(data, *, epochs=10, lr=0.001):
    """epochs and lr MUST be passed as keyword arguments."""
    return f"Training for {epochs} epochs at lr={lr}"

# train(data, 20)          # TypeError!
print(train("X", epochs=20, lr=0.01))  # OK
```

### Positional-Only Arguments (before `/`)

```python
def power(base, exp, /):
    """base and exp MUST be passed by position."""
    return base ** exp

print(power(2, 10))         # 1024
# power(base=2, exp=10)     # TypeError!
```

### Combining All Argument Types

```python
def example(pos_only, /, regular, *, kw_only):
    return f"{pos_only}, {regular}, {kw_only}"

print(example(1, regular=2, kw_only=3))  # 1, 2, 3
```

## Your Task

1. `sum_all(*args)` - Sum any number of arguments using *args
2. `create_model(**kwargs)` - Accept any keyword arguments, return as dict
3. `train_model(data, *, epochs, learning_rate)` - Keyword-only args after data
4. `process(x, y, /, z)` - x and y are positional-only, z can be keyword

## Testing
```bash
pytest exercises/16_arguments/test_arguments.py -v
```
