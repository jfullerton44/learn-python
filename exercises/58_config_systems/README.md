# Exercise 58: Config Systems

## Concept

Configuration systems manage settings across environments and provide validation and defaults.

### Key Concepts

1. **Hierarchical configs**: Override defaults
2. **Environment-specific**: Dev, staging, prod
3. **Validation**: Schema-based validation
4. **Formats**: YAML, TOML, JSON

## AI/ML Application

- Experiment configuration
- Hyperparameter management
- Deployment configs

## Your Task

1. `MLComponent` class - Configurable component
2. `Pipeline` class - Config-driven pipeline
3. `create_component(name)` - Factory
4. `validate_config(config)` - Config validation with required keys

## Testing
```bash
pytest exercises/58_config_systems/test_config_systems.py -v
```
