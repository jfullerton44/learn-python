# Exercise 15: Basic Type Hints

## Concept

Type hints add optional static type information to Python code. They improve code readability, enable better IDE support, and can be checked with tools like mypy.

### Key Concepts

1. **Basic Types**: `int`, `str`, `float`, `bool`
2. **Generic Types**: `List[T]`, `Dict[K, V]`, `Tuple[T, ...]`
3. **Optional**: `Optional[T]` for values that could be None
4. **Function Annotations**: Parameter and return type hints

## AI/ML Application

- Documenting expected tensor shapes and data types
- Ensuring correct data pipeline types
- Improving code maintainability in large ML projects

## Code Examples

### Basic Type Hints on Functions

```python
def greet(name: str, age: int) -> str:
    return f"Hello, {name}! You are {age} years old."

def is_passing(score: float, threshold: float = 60.0) -> bool:
    return score >= threshold
```

### Using `List`, `Dict`, and `Tuple`

```python
from typing import List, Dict, Tuple

def average(scores: List[float]) -> float:
    return sum(scores) / len(scores)

def build_profile(name: str, email: str) -> Dict[str, str]:
    return {"name": name, "email": email}

def min_max(values: List[int]) -> Tuple[int, int]:
    return min(values), max(values)
```

### Using `Optional` for Values That May Be None

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)  # Returns None if not found

result: Optional[str] = find_user(99)
print(result)  # None
```

### Annotating Variables

```python
from typing import List

names: List[str] = ["Alice", "Bob", "Charlie"]
count: int = len(names)
ratio: float = 0.8
verbose: bool = True
```

## Your Task

1. `process_numbers(numbers: List[int]) -> int` - Sum a list of integers
2. `get_config() -> Dict[str, any]` - Return a configuration dictionary
3. `find_item(items: List[str], target: str) -> Optional[int]` - Find index or return None
4. `split_data(data: List[float], ratio: float) -> Tuple[List[float], List[float]]` - Split data by ratio

## Testing
```bash
pytest exercises/15_type_hints_basics/test_type_hints.py -v
```
