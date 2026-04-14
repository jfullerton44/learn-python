# Exercise 48: Data Validation

## Concept

Data validation ensures inputs meet expected constraints before processing. Critical for robust ML systems.

### Key Concepts

1. **Schema validation**: Define expected structure
2. **Type checking**: Verify data types
3. **Constraint validation**: Range, format checks
4. **Error messages**: Clear validation failures

## AI/ML Application

- Validating model inputs
- Config file validation
- API request validation

## Code Examples

### Schema Validation for a Dictionary

```python
def validate_schema(data, schema):
    """Check that data contains all required keys with correct types."""
    errors = []
    for key, expected_type in schema.items():
        if key not in data:
            errors.append(f"Missing required key: '{key}'")
        elif not isinstance(data[key], expected_type):
            errors.append(f"'{key}' must be {expected_type.__name__}, got {type(data[key]).__name__}")
    return errors

schema = {"name": str, "age": int, "scores": list}
errors = validate_schema({"name": "Alice", "age": "old"}, schema)
print(errors)
# ["'age' must be int, got str", "Missing required key: 'scores'"]
```

### Runtime Type Checking

```python
def ensure_type(value, expected_type, field_name="value"):
    """Raise a clear error if the value is the wrong type."""
    if not isinstance(value, expected_type):
        raise TypeError(
            f"{field_name} must be {expected_type.__name__}, "
            f"got {type(value).__name__}: {value!r}"
        )
    return value

ensure_type(42, int, "age")          # OK — returns 42
# ensure_type("hello", int, "age")   # TypeError: age must be int, got str
```

### Constraint Validation (Range and Format)

```python
def validate_constraints(value, *, min_val=None, max_val=None, pattern=None):
    """Validate a value against numeric or pattern constraints."""
    import re
    errors = []
    if min_val is not None and value < min_val:
        errors.append(f"Value {value} is below minimum {min_val}")
    if max_val is not None and value > max_val:
        errors.append(f"Value {value} exceeds maximum {max_val}")
    if pattern and isinstance(value, str) and not re.match(pattern, value):
        errors.append(f"Value '{value}' does not match pattern '{pattern}'")
    return errors

print(validate_constraints(150, min_val=0, max_val=100))
# ["Value 150 exceeds maximum 100"]
print(validate_constraints("bad-email", pattern=r"^[\w.]+@[\w.]+$"))
# ["Value 'bad-email' does not match pattern ..."]
```

### Collecting Multiple Validation Errors

```python
def validate_user(data):
    """Collect all errors instead of failing on the first one."""
    errors = []
    if not isinstance(data.get("name"), str) or not data["name"].strip():
        errors.append("'name' is required and must be a non-empty string")
    if not isinstance(data.get("age"), int) or data["age"] < 0:
        errors.append("'age' must be a non-negative integer")
    if not isinstance(data.get("email"), str) or "@" not in data.get("email", ""):
        errors.append("'email' must be a valid email address")
    return errors

errors = validate_user({"name": "", "age": -5, "email": "nope"})
print(errors)
# ['name' is required..., 'age' must be..., 'email' must be...]
```

## Your Task

1. `MLComponent` class - Base component with name and process method
2. `Pipeline` class - Component chain with add_step and execute
3. `create_component(name)` - Factory function
4. `validate_config(config)` - Validate config has 'model' and 'data' keys

## Testing
```bash
pytest exercises/48_validation/test_validation.py -v
```
