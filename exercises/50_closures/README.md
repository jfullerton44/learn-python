# Exercise 50: Closures

## Concept

Closures capture variables from enclosing scope, enabling factory functions and maintaining state.

### Key Concepts

1. **Nested functions**: Functions defined inside functions
2. **Captured variables**: Access outer scope
3. **State encapsulation**: Private variables
4. **Factory functions**: Create configured functions

## AI/ML Application

- Configurable processing functions
- Learning rate schedulers
- Parameterized loss functions

## Your Task

1. `MLComponent` class - Component with closure-based configuration
2. `Pipeline` class - Pipeline using closures for state
3. `create_component(name)` - Closure-based factory
4. `validate_config(config)` - Closure for validation rules

## Testing
```bash
pytest exercises/50_closures/test_closures.py -v
```
