# Exercise 14: Scoping and Namespaces

## Concept

Python uses the LEGB rule to resolve variable names: Local, Enclosing, Global, Built-in. Understanding scope is essential for writing correct code with functions and closures.

### Key Concepts

1. **LEGB Rule**: Python looks up names in this order:
   - **L**ocal: Inside the current function
   - **E**nclosing: Inside enclosing functions (for nested functions)
   - **G**lobal: At the module level
   - **B**uilt-in: Python's built-in names

2. **global keyword**: Declare a variable as global from within a function
3. **nonlocal keyword**: Reference a variable from an enclosing scope

## AI/ML Application

- Maintaining state across function calls (counters, caches)
- Creating closures for hyperparameter configuration
- Managing shared state in training loops

## Code Examples

### LEGB Rule — Variable Resolution Order

```python
x = "global"  # Global scope

def outer():
    x = "enclosing"  # Enclosing scope

    def inner():
        x = "local"  # Local scope
        print(x)      # "local" — Local is checked first

    inner()
    print(x)  # "enclosing" — inner's local doesn't affect this scope

outer()
print(x)  # "global" — outer's enclosing doesn't affect this scope
```

### Built-in scope

```python
# Python checks built-in scope last
print(len([1, 2, 3]))  # 3 — len is a built-in name

# Shadowing a built-in (avoid this!)
len = 10
# print(len([1, 2, 3]))  # TypeError — len is now an int
del len  # Restore access to the built-in
```

### The `global` keyword

```python
counter = 0

def increment():
    global counter  # Declare intent to modify the global variable
    counter += 1

increment()
increment()
print(counter)  # 2
```

### The `nonlocal` keyword

```python
def make_greeting(prefix):
    message = prefix

    def update(new_prefix):
        nonlocal message  # Modify the enclosing scope's variable
        message = new_prefix

    update("Hello")
    return message

print(make_greeting("Hi"))  # "Hello"
```

### Closures — Functions That Remember Their Enclosing Scope

```python
def create_counter(start=0):
    count = start

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = create_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

## Your Task

1. `demonstrate_legb()` - Create a function that returns a local variable to show local scope
2. `use_global()` - Use the `global` keyword to modify a global variable
3. `use_nonlocal()` - Create nested functions using `nonlocal` to modify enclosing scope
4. `create_counter()` - Create a closure that maintains count state using `nonlocal`

## Testing
```bash
pytest exercises/14_scoping/test_scoping.py -v
```
