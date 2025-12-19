# Exercise 14: Scoping and Namespaces

## Concept

Python uses the LEGB rule to resolve variable names: Local, Enclosing, Global, Built-in. Understanding scope is essential for writing correct code with functions and closures.

### Key Concepts

1. **LEGB Rule**: Python looks up names in this order:
   - **L**ocal: Inside the current function
   - **E**nclosing: Inside enclosing functions (for nested functions)
   - **G**lobal: At the module level
   - **B**uilt-in: Python's built-in names

2. **global keyword**: Declare a variable as global from within a function
3. **nonlocal keyword**: Reference a variable from an enclosing scope

## AI/ML Application

- Maintaining state across function calls (counters, caches)
- Creating closures for hyperparameter configuration
- Managing shared state in training loops

## Your Task

1. `demonstrate_legb()` - Create a function that returns a local variable to show local scope
2. `use_global()` - Use the `global` keyword to modify a global variable
3. `use_nonlocal()` - Create nested functions using `nonlocal` to modify enclosing scope
4. `create_counter()` - Create a closure that maintains count state using `nonlocal`

## Testing
```bash
pytest exercises/14_scoping/test_scoping.py -v
```
