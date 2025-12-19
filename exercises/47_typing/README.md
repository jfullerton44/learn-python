# Exercise 47: Advanced Typing

## Concept

Advanced type hints enable static type checking and better code documentation for complex ML systems.

### Key Concepts

1. **Generic types**: TypeVar, Generic classes
2. **Callable types**: Function signatures
3. **Type guards**: Narrow types at runtime
4. **Protocol**: Structural subtyping

## AI/ML Application

- Type-safe ML pipelines
- Well-documented APIs
- Static analysis for bug prevention

## Your Task

1. `MLComponent` class - Base class with name attribute and `process(data)` method
2. `Pipeline` class - Chain of components with `add_step()` and `execute()` methods
3. `create_component(name)` - Factory function returning MLComponent
4. `validate_config(config)` - Check if config dict has required keys

## Testing
```bash
pytest exercises/47_typing/test_typing.py -v
```
