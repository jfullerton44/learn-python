# Exercise 2: Exception Handling

## Concept

Exception handling allows you to gracefully handle errors and unexpected situations in your code. Python uses try/except blocks to catch and handle exceptions.

### Key Concepts

1. **Basic Exception Handling**
   - `try`: Code that might raise an exception
   - `except`: Code to handle the exception
   - `finally`: Code that always runs (cleanup)
   - `else`: Code that runs if no exception occurred

2. **Exception Types**
   - Built-in exceptions: `ValueError`, `TypeError`, `KeyError`, `FileNotFoundError`, etc.
   - Exception hierarchy: All exceptions inherit from `BaseException`
   - Specific vs general exception catching

3. **Raising Exceptions**
   - `raise` keyword to throw exceptions
   - Creating custom exception classes
   - Re-raising exceptions with `raise` (no arguments)

4. **Best Practices**
   - Catch specific exceptions, not broad `Exception`
   - Use `finally` for cleanup (closing files, connections)
   - Don't silence exceptions without good reason
   - Custom exceptions for domain-specific errors

## AI/ML Application

In ML systems, exception handling is crucial for:
- **Data loading errors**: Handle missing files, corrupted data
- **Training failures**: Catch NaN losses, OOM errors, convergence issues
- **Model errors**: Invalid inputs, dimension mismatches
- **Graceful degradation**: Fallback to simpler models when advanced ones fail

## Your Task

Create the following exception handling utilities for an ML pipeline:

1. **Custom Exceptions**:
   - `DataLoadError`: Raised when data cannot be loaded
   - `ModelTrainingError`: Raised when training fails
   - `ValidationError`: Raised when validation fails (inherit from ValueError)

2. **`DataLoader` class**:
   - Method: `load_data(filepath)` - raises `DataLoadError` if file doesn't exist
   - Method: `validate_data(data)` - raises `ValidationError` if data is empty or None

3. **`ModelTrainer` class**:
   - Method: `train(data, epochs)` - raises `ModelTrainingError` if epochs < 1
   - Method: `safe_train(data, epochs)` - catches exceptions and returns dict with:
     - `"success": bool`, `"message": str`, `"error": Exception or None`

4. **Function: `safe_divide(a, b)`**:
   - Returns `a / b` if successful
   - Catches `ZeroDivisionError` and returns `None`
   - Uses `else` clause to print "Division successful"

5. **Function: `process_with_cleanup(resource_name)`**:
   - Uses try/except/finally
   - Simulates opening a resource (append to a list called `opened_resources`)
   - Simulates error if resource_name is "bad_resource"
   - Finally block always closes resource (append to `closed_resources` list)

## Example Usage

```python
# Custom exceptions
try:
    loader = DataLoader()
    loader.load_data("nonexistent.csv")
except DataLoadError as e:
    print(f"Error: {e}")

# Safe training
trainer = ModelTrainer()
result = trainer.safe_train([], epochs=10)
print(result)  # {"success": False, "message": "...", "error": ValidationError(...)}

# Safe divide
result = safe_divide(10, 2)  # Returns 5.0, prints "Division successful"
result = safe_divide(10, 0)  # Returns None
```

## Testing

```bash
pytest exercises/02_exceptions/test_exceptions.py -v
```

## Additional Resources

- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

## Common Pitfalls

1. Catching too broad exceptions (`except Exception`)
2. Empty except blocks that silence errors
3. Not using `finally` for cleanup operations
4. Raising generic exceptions instead of specific ones
