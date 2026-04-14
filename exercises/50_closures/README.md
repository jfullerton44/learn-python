# Exercise 50: Closures

## Concept

Closures capture variables from enclosing scope, enabling factory functions and maintaining state.

### Key Concepts

1. **Nested functions**: Functions defined inside functions
2. **Captured variables**: Access outer scope
3. **State encapsulation**: Private variables
4. **Factory functions**: Create configured functions

## AI/ML Application

- Configurable processing functions
- Learning rate schedulers
- Parameterized loss functions

## Code Examples

### Simple Closure — Capturing a Variable

```python
def make_greeter(greeting):
    # 'greeting' is captured by the inner function
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

hello = make_greeter("Hello")
hola = make_greeter("Hola")
print(hello("Alice"))  # "Hello, Alice!"
print(hola("Bob"))     # "Hola, Bob!"
```

### Closure with Mutable State (Counter)

```python
def make_counter(start=0):
    count = start
    def counter():
        nonlocal count   # Required to modify the captured variable
        count += 1
        return count
    return counter

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

### State Encapsulation — Private Data

```python
def make_bank_account(initial_balance):
    balance = initial_balance  # Encapsulated; not accessible from outside

    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def get_balance():
        return balance

    return {"deposit": deposit, "get_balance": get_balance}

account = make_bank_account(100)
account["deposit"](50)
print(account["get_balance"]())  # 150
# 'balance' is private — there's no way to access it directly
```

### Factory Function Using Closures

```python
def make_validator(min_val, max_val):
    """Factory that creates range-checking functions."""
    def validate(value):
        if min_val <= value <= max_val:
            return True
        raise ValueError(f"{value} not in range [{min_val}, {max_val}]")
    return validate

check_percentage = make_validator(0, 100)
check_temperature = make_validator(-40, 60)

print(check_percentage(85))     # True
print(check_temperature(-10))   # True
# check_percentage(200)         # ValueError
```

## Your Task

1. `MLComponent` class - Component with closure-based configuration
2. `Pipeline` class - Pipeline using closures for state
3. `create_component(name)` - Closure-based factory
4. `validate_config(config)` - Closure for validation rules

## Testing
```bash
pytest exercises/50_closures/test_closures.py -v
```
