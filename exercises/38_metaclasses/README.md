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

## Your Task

1. `ModelRegistry` metaclass - Tracks all subclasses in a `models` dict
2. `BaseModel` class - Uses ModelRegistry metaclass
3. `ResNet`, `VGG` classes - Inherit from BaseModel (auto-registered)
4. `get_registered_models()` - Return the registered models dict

## Testing
```bash
pytest exercises/38_metaclasses/test_metaclasses.py -v
```
