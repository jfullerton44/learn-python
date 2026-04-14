# Exercise 39: Descriptors

## Concept

Descriptors control attribute access using `__get__`, `__set__`, and `__delete__`. They power properties, methods, and static/class methods.

### Key Concepts

1. **Descriptor protocol**: `__get__`, `__set__`, `__delete__`
2. **Data descriptors**: Define both `__get__` and `__set__`
3. **Non-data descriptors**: Define only `__get__`
4. **Lazy properties**: Compute once, cache result

## AI/ML Application

- Type-validated model parameters
- Lazy loading of model weights
- Computed properties with caching

## Code Examples

### Simple Descriptor Class

```python
class ReadOnly:
    """A data descriptor that prevents modification after initial set."""
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if self.name in obj.__dict__:
            raise AttributeError(f"'{self.name}' is read-only after creation")
        obj.__dict__[self.name] = value

class DatabaseRecord:
    record_id = ReadOnly()

row = DatabaseRecord()
row.record_id = 101      # OK — first assignment
print(row.record_id)     # 101
# row.record_id = 999    # AttributeError: 'record_id' is read-only after creation
```

### Data Descriptor with Validation

```python
class RangeValidator:
    """A data descriptor that enforces a numeric range on assignment."""
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not (self.minimum <= value <= self.maximum):
            raise ValueError(
                f"{self.name} must be between {self.minimum} and "
                f"{self.maximum}, got {value}"
            )
        obj.__dict__[self.name] = value

class Product:
    price = RangeValidator(0.01, 10_000)
    quantity = RangeValidator(0, 999)

item = Product()
item.price = 19.99     # OK
item.quantity = 5       # OK
# item.price = -1       # ValueError: price must be between 0.01 and 10000, got -1
# item.quantity = 2000  # ValueError: quantity must be between 0 and 999, got 2000
```

### Cached Property Pattern

```python
class CachedProperty:
    """Compute a value once on first access, then cache it on the instance."""
    def __init__(self, func):
        self.func = func
        self.attr_name = func.__name__

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = self.func(obj)
        setattr(obj, self.attr_name, value)  # store directly → skips descriptor next time
        return value

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @CachedProperty
    def area(self):
        print("Computing area (runs only once)...")
        return math.pi * self.radius ** 2

c = Circle(5)
print(c.area)  # Computing area (runs only once)... → 78.539...
print(c.area)  # 78.539...  (cached — no recomputation)
```

## Your Task

1. `TypedProperty` class - Descriptor that validates type on assignment
2. `Model` class - Uses TypedProperty for learning_rate (float) and epochs (int)
3. `LazyProperty` class - Descriptor that computes value once and caches it

## Testing
```bash
pytest exercises/39_descriptors/test_descriptors.py -v
```
