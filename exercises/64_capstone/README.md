# Exercise 64: Build a Mini ML Framework

## Project Goal
Build a lightweight ML framework combining all learned concepts.

## Requirements
1. Auto-differentiation engine
2. Configurable training loops with callbacks  
3. Custom dataset loaders with caching
4. Async inference server
5. Distributed training coordinator
6. Comprehensive test suite

## Structure
```
64_capstone/
├── README.md
├── framework/
│   ├── __init__.py
│   ├── autograd.py
│   ├── training.py
│   ├── data.py
│   └── server.py
├── tests/
│   └── test_framework.py
└── examples/
    └── train_model.py
```

## Code Examples

### Simple Auto-Differentiation Concept

```python
class Value:
    """A scalar value that tracks computation for automatic gradient computation."""
    def __init__(self, data, _children=(), _op=""):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None
        self._children = set(_children)

    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), "+")
        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward
        return out

    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), "*")
        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward
        return out

# Forward pass
a = Value(2.0)
b = Value(3.0)
c = a * b + b  # c = 2*3 + 3 = 9
c.grad = 1.0
c._backward()
print(f"c = {c.data}, da = {a.grad}")  # c = 9.0, da = 3.0 (dc/da = b)
```

### Callback Pattern in a Training Loop

```python
class PrintCallback:
    def on_epoch_end(self, epoch, logs):
        print(f"Epoch {epoch}: loss={logs.get('loss', '?'):.4f}")

class EarlyStopping:
    def __init__(self, patience=3):
        self.patience = patience
        self.best_loss = float("inf")
        self.counter = 0
        self.should_stop = False

    def on_epoch_end(self, epoch, logs):
        loss = logs.get("loss", float("inf"))
        if loss < self.best_loss:
            self.best_loss = loss
            self.counter = 0
        else:
            self.counter += 1
            if self.counter >= self.patience:
                self.should_stop = True
                print(f"Early stopping at epoch {epoch}")

def train(epochs, callbacks=None):
    callbacks = callbacks or []
    for epoch in range(epochs):
        loss = 1.0 / (epoch + 1)  # Simulated decreasing loss
        for cb in callbacks:
            cb.on_epoch_end(epoch, {"loss": loss})
            if getattr(cb, "should_stop", False):
                return

train(10, callbacks=[PrintCallback(), EarlyStopping(patience=2)])
```

### Async Server Endpoint Pattern

```python
import asyncio

# Conceptual async inference server
async def predict(model, input_data):
    """Simulate an async prediction endpoint."""
    await asyncio.sleep(0.01)  # Simulate model inference time
    return {"input": input_data, "prediction": sum(input_data) / len(input_data)}

async def handle_requests(model, requests):
    """Process multiple inference requests concurrently."""
    tasks = [predict(model, req) for req in requests]
    results = await asyncio.gather(*tasks)
    return results

async def main():
    model = "my_model"  # Placeholder
    requests = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    results = await handle_requests(model, requests)
    for r in results:
        print(r)

# asyncio.run(main())
```

## Testing
```bash
pytest exercises/64_capstone/tests/ -v
```
