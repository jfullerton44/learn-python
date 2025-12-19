# Exercise 52: Strategy and Observer Patterns

## Concept

Strategy pattern enables runtime algorithm selection. Observer pattern implements event-driven communication.

### Key Concepts

1. **Strategy**: Interchangeable algorithms
2. **Observer**: Subscribe to events
3. **Pub/Sub**: Loose coupling between components
4. **Callbacks**: Event handling

## AI/ML Application

- Training callbacks (TensorBoard, checkpointing)
- Interchangeable optimizers
- Experiment tracking

## Your Task

1. `MLComponent` class - Component with strategy pattern
2. `Pipeline` class - Observable pipeline with callbacks
3. `create_component(name)` - Factory function
4. `validate_config(config)` - Validation

## Testing
```bash
pytest exercises/52_strategy_observer/test_strategy_observer.py -v
```
