# Exercise 63: Packaging

## Concept

Python packaging enables sharing code as installable packages with dependencies and versioning.

### Key Concepts

1. **setup.py/pyproject.toml**: Package configuration
2. **Dependencies**: requirements and extras
3. **Versioning**: Semantic versioning
4. **Distribution**: PyPI, wheels

## AI/ML Application

- Sharing ML model packages
- Internal ML libraries
- Reproducible environments

## Your Task

1. `MLComponent` class - Packageable component
2. `Pipeline` class - Pipeline module
3. `create_component(name)` - Factory
4. `validate_config(config)` - Validation

## Testing
```bash
pytest exercises/63_packaging/test_packaging.py -v
```
