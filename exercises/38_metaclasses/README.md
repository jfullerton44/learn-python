# Exercise 38: Metaclasses

## Concept

Metaclasses are "classes of classes" - they control class creation. Advanced technique for frameworks and automatic registration.

### Key Concepts

1. **type**: The default metaclass
2. **Custom metaclass**: Override `__new__` to modify class creation
3. **Class registration**: Auto-register classes in a registry

## AI/ML Application

- Model registries for experiment tracking
- Plugin systems for data loaders
- Framework architecture

## Code Examples

### Using type() to Create a Class Dynamically

```python
# type(name, bases, namespace) is the default metaclass
# Normally we write: class Dog: ...
# Equivalent using type():
Dog = type("Dog", (), {
    "species": "Canine",
    "bark": lambda self: "Woof!",
})

d = Dog()
print(d.species)  # Canine
print(d.bark())   # Woof!
print(type(Dog))  # <class 'type'>
```

### Custom Metaclass with __new__

```python
class UpperAttrMeta(type):
    """Metaclass that converts all attributes to uppercase."""
    def __new__(mcs, name, bases, namespace):
        uppercase_attrs = {
            key.upper() if not key.startswith("__") else key: val
            for key, val in namespace.items()
        }
        return super().__new__(mcs, name, bases, uppercase_attrs)

class Config(metaclass=UpperAttrMeta):
    host = "localhost"
    port = 8080

print(Config.HOST)  # localhost
print(Config.PORT)  # 8080
```

### Class Registry Pattern

```python
class RegistryMeta(type):
    """Metaclass that auto-registers subclasses in a dict."""
    registry = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        # Don't register the base class itself
        if bases:
            mcs.registry[name] = cls
        return cls

class Plugin(metaclass=RegistryMeta):
    """Base class — subclasses are auto-registered."""
    pass

class JSONLoader(Plugin):
    pass

class CSVLoader(Plugin):
    pass

print(RegistryMeta.registry)
# {'JSONLoader': <class 'JSONLoader'>, 'CSVLoader': <class 'CSVLoader'>}
```

## Your Task

1. `ModelRegistry` metaclass - Tracks all subclasses in a `models` dict
2. `BaseModel` class - Uses ModelRegistry metaclass
3. `ResNet`, `VGG` classes - Inherit from BaseModel (auto-registered)
4. `get_registered_models()` - Return the registered models dict

## Testing
```bash
pytest exercises/38_metaclasses/test_metaclasses.py -v
```
