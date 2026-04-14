# Exercise 13: Basic Testing

## Concept
Writing unit tests with pytest, assertions, test organization.

## Code Examples

### pytest Assertions
```python
# test_basics.py
def test_arithmetic():
    assert 7 * 6 == 42

def test_string_lower():
    assert "WORLD".lower() == "world"

def test_dict_has_key():
    config = {"host": "localhost", "port": 8080}
    assert "port" in config
```

### Test Functions — Testing Your Own Code
```python
# temperature.py
def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise TypeError("Temperature must be a number")
    return celsius * 9 / 5 + 32

# test_temperature.py
import pytest
from temperature import celsius_to_fahrenheit

def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212

def test_invalid_input():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("hot")
```

### Test Organization — Group Related Tests
```python
# Use descriptive names: test_<function>_<scenario>
def test_freezing_point():
    assert celsius_to_fahrenheit(0) == 32

def test_negative_temperature():
    assert celsius_to_fahrenheit(-40) == -40.0

def test_returns_numeric():
    result = celsius_to_fahrenheit(25)
    assert result == 77.0
    assert isinstance(result, (int, float))
```

### Edge Case Testing
```python
def test_invalid_type_raises():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(None)

def test_absolute_zero():
    assert celsius_to_fahrenheit(-273.15) == pytest.approx(-459.67)

def test_body_temperature():
    assert celsius_to_fahrenheit(37) == pytest.approx(98.6)

def test_fractional_degrees():
    result = celsius_to_fahrenheit(0.5)
    assert abs(result - 32.9) < 0.01  # approximate comparison
```

## Your Task
Create `calculator.py` with functions to test:
1. `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, `divide(a, b)`
2. Write comprehensive tests in `test_testing_basics.py`
3. Test edge cases (division by zero, negative numbers, etc.)
