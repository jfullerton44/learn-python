# Exercise 13: Basic Testing

## Concept
Writing unit tests with pytest, assertions, test organization.

## Code Examples

### pytest Assertions
```python
# test_math.py
def test_addition():
    assert 2 + 3 == 5

def test_string_upper():
    assert "hello".upper() == "HELLO"

def test_list_contains():
    fruits = ["apple", "banana", "cherry"]
    assert "banana" in fruits
```

### Test Functions — Testing Your Own Code
```python
# calculator.py
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# test_calculator.py
import pytest
from calculator import divide

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

### Test Organization — Group Related Tests
```python
# Use descriptive names: test_<function>_<scenario>
def test_divide_positive_numbers():
    assert divide(10, 2) == 5.0

def test_divide_negative_numbers():
    assert divide(-10, 2) == -5.0

def test_divide_returns_float():
    result = divide(7, 2)
    assert result == 3.5
    assert isinstance(result, float)
```

### Edge Case Testing
```python
def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(1, 0)

def test_divide_zero_numerator():
    assert divide(0, 5) == 0.0

def test_divide_large_numbers():
    assert divide(1_000_000, 1_000) == 1_000.0

def test_divide_small_floats():
    result = divide(1, 3)
    assert abs(result - 0.3333) < 0.001  # approximate comparison
```

## Your Task
Create `calculator.py` with functions to test:
1. `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, `divide(a, b)`
2. Write comprehensive tests in `test_testing_basics.py`
3. Test edge cases (division by zero, negative numbers, etc.)
