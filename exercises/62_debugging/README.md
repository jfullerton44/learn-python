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

## Code Examples

### Using breakpoint() for Interactive Debugging

```python
def compute_loss(predictions, targets):
    """Insert breakpoint() to inspect variables at runtime."""
    total = 0.0
    for i, (pred, target) in enumerate(zip(predictions, targets)):
        diff = pred - target
        # Uncomment breakpoint() to pause and inspect:
        # breakpoint()  # Opens pdb; use 'p diff', 'n' to step, 'c' to continue
        total += diff ** 2
    return total / len(predictions)

loss = compute_loss([2.5, 0.0, 2.1], [3.0, -0.5, 2.0])
print(f"MSE Loss: {loss:.4f}")
```

### Logging-Based Debugging

```python
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def train_step(epoch, data):
    logger.debug(f"Epoch {epoch}: input shape = {len(data)} samples")
    result = sum(data) / len(data)
    if result > 100:
        logger.warning(f"Epoch {epoch}: unusually high mean = {result}")
    logger.info(f"Epoch {epoch}: mean = {result:.4f}")
    return result

train_step(1, [1.0, 2.0, 3.0])
# DEBUG: Epoch 1: input shape = 3 samples
# INFO: Epoch 1: mean = 2.0000
```

### Systematic Debugging Approach

```python
def debug_nan_in_pipeline(data):
    """Strategy: add checkpoints to isolate where NaN appears."""
    import math

    # Step 1: Validate input
    assert all(not math.isnan(x) for x in data), "NaN in input!"

    # Step 2: Apply transforms with checks after each step
    normalized = [(x - min(data)) / (max(data) - min(data)) for x in data]
    assert all(not math.isnan(x) for x in normalized), "NaN after normalization!"

    # Step 3: Compute result
    result = sum(x ** 2 for x in normalized)
    assert not math.isnan(result), "NaN in final result!"

    return result

print(debug_nan_in_pipeline([10, 20, 30, 40]))  # 2.0
```

## Your Task

1. `MLComponent` class - Debuggable component
2. `Pipeline` class - Pipeline with debug hooks
3. `create_component(name)` - Factory
4. `validate_config(config)` - Validation

## Testing
```bash
pytest exercises/62_debugging/test_debugging.py -v
```
