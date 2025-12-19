# Exercise 62: Debugging

## Concept

Debugging techniques for finding and fixing issues in ML code, from print statements to advanced debuggers.

### Key Concepts

1. **pdb**: Python debugger
2. **Breakpoints**: Pause execution
3. **Logging**: Strategic log placement
4. **Profiling**: Identify bottlenecks

## AI/ML Application

- Debugging training issues
- Finding NaN/Inf values
- Memory leak detection

## Your Task

1. `MLComponent` class - Debuggable component
2. `Pipeline` class - Pipeline with debug hooks
3. `create_component(name)` - Factory
4. `validate_config(config)` - Validation

## Testing
```bash
pytest exercises/62_debugging/test_debugging.py -v
```
