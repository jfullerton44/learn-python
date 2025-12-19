# Exercise 21: Pythonic Idioms

## Concept

Pythonic code follows Python's philosophy of readability and simplicity. Key idioms include EAFP vs LBYL, duck typing, and using language features effectively.

### Key Concepts

1. **EAFP (Easier to Ask Forgiveness than Permission)**: Try and catch exceptions
2. **LBYL (Look Before You Leap)**: Check conditions first
3. **Duck Typing**: "If it walks like a duck..." - focus on behavior, not type
4. **Zen of Python**: `import this` - guiding principles

## AI/ML Application

- Writing readable data processing pipelines
- Graceful error handling in training loops
- Clean, maintainable ML code

## Your Task

1. `eafp_file_read(filepath)` - Read file using try/except, return None if not found
2. `lbyl_file_read(filepath)` - Check if file exists before reading
3. `duck_typing_len(obj)` - Return length of any object with `__len__`
4. `pythonic_swap(a, b)` - Return swapped values using tuple unpacking
5. `list_comprehension_even(numbers)` - Filter even numbers using comprehension

## Testing
```bash
pytest exercises/21_pythonic/test_pythonic.py -v
```
