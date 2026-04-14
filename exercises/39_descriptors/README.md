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
class Verbose:
    """A non-data descriptor that logs attribute access."""
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = obj.__dict__.get(self.name, "N/A")
        print(f"Accessing '{self.name}' -> {value}")
        return value

class Person:
    name = Verbose()

p = Person()
p.__dict__["name"] = "Alice"
print(p.name)
# Accessing 'name' -> Alice
# Alice
```

### Data Descriptor with Validation

```python
class TypedProperty:
    """A data descriptor that enforces type on assignment."""
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name} must be {self.expected_type.__name__}, "
                f"got {type(value).__name__}"
            )
        obj.__dict__[self.name] = value

class Model:
    learning_rate = TypedProperty(float)
    epochs = TypedProperty(int)

m = Model()
m.learning_rate = 0.001  # OK
m.epochs = 10            # OK
# m.epochs = 3.5         # TypeError: epochs must be int, got float
```

### Lazy Property Pattern

```python
class LazyProperty:
    """Compute a value once, then cache it on the instance."""
    def __init__(self, func):
        self.func = func
        self.attr_name = func.__name__

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        # Compute once and store directly on the instance
        value = self.func(obj)
        setattr(obj, self.attr_name, value)
        return value

class DataSet:
    def __init__(self, raw):
        self.raw = raw

    @LazyProperty
    def processed(self):
        print("Computing (only runs once)...")
        return [x * 2 for x in self.raw]

ds = DataSet([1, 2, 3])
print(ds.processed)  # Computing (only runs once)... -> [2, 4, 6]
print(ds.processed)  # [2, 4, 6]  (cached, no recomputation)
```

## Your Task

1. `TypedProperty` class - Descriptor that validates type on assignment
2. `Model` class - Uses TypedProperty for learning_rate (float) and epochs (int)
3. `LazyProperty` class - Descriptor that computes value once and caches it

## Testing
```bash
pytest exercises/39_descriptors/test_descriptors.py -v
```
