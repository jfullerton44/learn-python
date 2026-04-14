# Exercise 21: Pythonic Idioms

## Concept

Pythonic code follows Python's philosophy of readability and simplicity. Key idioms include EAFP vs LBYL, duck typing, and using language features effectively.

### Key Concepts

1. **EAFP (Easier to Ask Forgiveness than Permission)**: Try and catch exceptions
2. **LBYL (Look Before You Leap)**: Check conditions first
3. **Duck Typing**: "If it walks like a duck..." - focus on behavior, not type
4. **Zen of Python**: `import this` - guiding principles

## AI/ML Application

- Writing readable data processing pipelines
- Graceful error handling in training loops
- Clean, maintainable ML code

## Code Examples

### EAFP vs LBYL

```python
# LBYL — Look Before You Leap (check first)
def get_value_lbyl(data, key):
    if key in data:
        return data[key]
    return None

# EAFP — Easier to Ask Forgiveness than Permission (try first)
def get_value_eafp(data, key):
    try:
        return data[key]
    except KeyError:
        return None

# EAFP is preferred in Python — cleaner, and often faster for the common case
```

### Duck Typing — Focus on Behavior, Not Type

```python
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm quacking like a duck!"

def make_it_quack(thing):
    # Don't check the type — just call the method
    return thing.quack()

print(make_it_quack(Duck()))    # Quack!
print(make_it_quack(Person()))  # I'm quacking like a duck!
```

### List Comprehensions vs Loops

```python
# Non-pythonic — manual loop
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x ** 2)

# Pythonic — list comprehension
squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(squares)  # [0, 4, 16, 36, 64]
```

### Tuple Unpacking

```python
# Swap without a temp variable
a, b = 1, 2
a, b = b, a
print(a, b)  # 2 1

# Unpack in a loop
pairs = [("Alice", 85), ("Bob", 92)]
for name, score in pairs:
    print(f"{name}: {score}")
```

### Context Managers

```python
# Non-pythonic — manual open/close
f = open("data.txt", "w")
try:
    f.write("hello")
finally:
    f.close()

# Pythonic — context manager handles cleanup automatically
with open("data.txt", "w") as f:
    f.write("hello")
# File is automatically closed here, even if an error occurs
```

## Your Task

1. `eafp_file_read(filepath)` - Read file using try/except, return None if not found
2. `lbyl_file_read(filepath)` - Check if file exists before reading
3. `duck_typing_len(obj)` - Return length of any object with `__len__`
4. `pythonic_swap(a, b)` - Return swapped values using tuple unpacking
5. `list_comprehension_even(numbers)` - Filter even numbers using comprehension

## Testing
```bash
pytest exercises/21_pythonic/test_pythonic.py -v
```
