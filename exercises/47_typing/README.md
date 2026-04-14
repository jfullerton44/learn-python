# Exercise 47: Advanced Typing

## Concept

Advanced type hints enable static type checking and better code documentation for complex ML systems.

### Key Concepts

1. **Generic types**: TypeVar, Generic classes
2. **Callable types**: Function signatures
3. **Type guards**: Narrow types at runtime
4. **Protocol**: Structural subtyping

## AI/ML Application

- Type-safe ML pipelines
- Well-documented APIs
- Static analysis for bug prevention

## Code Examples

### Generic Function with TypeVar

```python
from typing import TypeVar, List

T = TypeVar("T")

def first_element(items: List[T]) -> T:
    """Returns the first element, preserving the input type."""
    return items[0]

name: str = first_element(["alice", "bob"])   # T inferred as str
value: int = first_element([10, 20, 30])      # T inferred as int
```

### Generic Class

```python
from typing import TypeVar, Generic, List

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

int_stack: Stack[int] = Stack()
int_stack.push(42)
value = int_stack.pop()  # type checker knows this is int
```

### Callable Type Annotations

```python
from typing import Callable

# A function that accepts another function as a parameter
def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))

def add_one(x: int) -> int:
    return x + 1

result = apply_twice(add_one, 5)  # 7
```

### Protocol for Structural Subtyping

```python
from typing import Protocol

class Trainable(Protocol):
    def fit(self, data: list) -> None: ...
    def predict(self, inputs: list) -> list: ...

# Any class with fit() and predict() satisfies Trainable — no inheritance needed
class LinearModel:
    def fit(self, data: list) -> None:
        self.weights = [1.0] * len(data)

    def predict(self, inputs: list) -> list:
        return [x * 2 for x in inputs]

def train_model(model: Trainable, data: list) -> list:
    model.fit(data)
    return model.predict(data)

result = train_model(LinearModel(), [1, 2, 3])
```

## Your Task

1. `MLComponent` class - Base class with name attribute and `process(data)` method
2. `Pipeline` class - Chain of components with `add_step()` and `execute()` methods
3. `create_component(name)` - Factory function returning MLComponent
4. `validate_config(config)` - Check if config dict has required keys

## Testing
```bash
pytest exercises/47_typing/test_typing.py -v
```
