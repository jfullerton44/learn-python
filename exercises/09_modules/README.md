# Exercise 9: Modules and Packages

## Concept
Creating modules, import patterns, __name__ == "__main__", package structure with __init__.py.

## AI/ML Application
- Organizing ML codebases into reusable modules
- Creating model libraries
- Separating data loading, training, and evaluation code

## Your Task
Create a package structure:
1. `models/` package with `__init__.py`
2. `models/base.py` with `BaseModel` class
3. `models/neural_net.py` with `NeuralNet` class (imports BaseModel)
4. `utils.py` module with helper functions
5. `main.py` that imports and uses the modules

Each module should have proper `if __name__ == "__main__"` guards.

## Testing
```bash
pytest exercises/09_modules/test_modules.py -v
```
