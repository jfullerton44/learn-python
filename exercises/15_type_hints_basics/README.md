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

## Your Task

1. `process_numbers(numbers: List[int]) -> int` - Sum a list of integers
2. `get_config() -> Dict[str, any]` - Return a configuration dictionary
3. `find_item(items: List[str], target: str) -> Optional[int]` - Find index or return None
4. `split_data(data: List[float], ratio: float) -> Tuple[List[float], List[float]]` - Split data by ratio

## Testing
```bash
pytest exercises/15_type_hints_basics/test_type_hints.py -v
```
