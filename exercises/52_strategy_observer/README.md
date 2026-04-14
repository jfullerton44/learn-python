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

## Code Examples

### Strategy Pattern — Swappable Algorithms

```python
def sort_by_name(items):
    return sorted(items, key=lambda x: x["name"])

def sort_by_price(items):
    return sorted(items, key=lambda x: x["price"])

class ProductList:
    def __init__(self, products):
        self.products = products
        self._sort_strategy = sort_by_name  # Default strategy

    def set_sort_strategy(self, strategy):
        """Swap the sorting algorithm at runtime."""
        self._sort_strategy = strategy

    def sorted_products(self):
        return self._sort_strategy(self.products)

products = ProductList([
    {"name": "Banana", "price": 1.20},
    {"name": "Apple", "price": 0.80},
])
print(products.sorted_products())            # Sorted by name
products.set_sort_strategy(sort_by_price)
print(products.sorted_products())            # Sorted by price
```

### Observer Pattern — Subscribe and Notify

```python
class EventEmitter:
    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        """Subscribe a callback to an event."""
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event, *args, **kwargs):
        """Notify all subscribers of an event."""
        for callback in self._listeners.get(event, []):
            callback(*args, **kwargs)

emitter = EventEmitter()
emitter.on("training_complete", lambda metrics: print(f"Accuracy: {metrics['acc']}"))
emitter.on("training_complete", lambda metrics: print(f"Logging metrics: {metrics}"))

emitter.emit("training_complete", {"acc": 0.95, "loss": 0.12})
# Accuracy: 0.95
# Logging metrics: {'acc': 0.95, 'loss': 0.12}
```

### Callback Pattern

```python
def train(epochs, on_epoch_end=None):
    """Training loop with an optional callback hook."""
    for epoch in range(1, epochs + 1):
        loss = 1.0 / epoch  # Simulated loss
        if on_epoch_end:
            on_epoch_end(epoch, loss)

def print_progress(epoch, loss):
    print(f"Epoch {epoch}: loss={loss:.4f}")

train(3, on_epoch_end=print_progress)
# Epoch 1: loss=1.0000
# Epoch 2: loss=0.5000
# Epoch 3: loss=0.3333
```

## Your Task

1. `MLComponent` class - Component with strategy pattern
2. `Pipeline` class - Observable pipeline with callbacks
3. `create_component(name)` - Factory function
4. `validate_config(config)` - Validation

## Testing
```bash
pytest exercises/52_strategy_observer/test_strategy_observer.py -v
```
