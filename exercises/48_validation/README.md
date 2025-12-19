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

## Your Task

1. `MLComponent` class - Base component with name and process method
2. `Pipeline` class - Component chain with add_step and execute
3. `create_component(name)` - Factory function
4. `validate_config(config)` - Validate config has 'model' and 'data' keys

## Testing
```bash
pytest exercises/48_validation/test_validation.py -v
```
