# Exercise 51: Factory and Builder Patterns

## Concept

Factory and Builder patterns create objects flexibly without exposing complex construction logic.

### Key Concepts

1. **Factory Method**: Create objects without specifying exact class
2. **Abstract Factory**: Families of related objects
3. **Builder**: Step-by-step construction
4. **Registration**: Dynamic factory configuration

## AI/ML Application

- Model factories for different architectures
- Dataset builders with configurable options
- Optimizer factories

## Your Task

1. `MLComponent` class - Base class for factory-created components
2. `Pipeline` class - Builder pattern for pipeline construction
3. `create_component(name)` - Factory function
4. `validate_config(config)` - Config validation

## Testing
```bash
pytest exercises/51_factory_builder/test_factory_builder.py -v
```
