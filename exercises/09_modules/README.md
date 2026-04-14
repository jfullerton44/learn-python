# Exercise 9: Modules and Packages

## Concept
Creating modules, import patterns, __name__ == "__main__", package structure with __init__.py.

## AI/ML Application
- Organizing ML codebases into reusable modules
- Creating model libraries
- Separating data loading, training, and evaluation code

## Code Examples

### import Statements
```python
# Import an entire module
import math
print(math.sqrt(16))  # 4.0

# Alias a module for convenience
import numpy as np
arr = np.array([1, 2, 3])
```

### from ... import
```python
# Import specific names from a module
from os.path import join, exists
path = join("data", "train.csv")

# Import everything (use sparingly)
from math import *
```

### \_\_name\_\_ == "\_\_main\_\_"
```python
# Code inside this block only runs when the file is executed directly,
# not when it is imported as a module.
def train():
    print("Training...")

if __name__ == "__main__":
    train()
```

### Package Structure with \_\_init\_\_.py
```
mypackage/
    __init__.py        # Makes the directory a package
    module_a.py
    module_b.py
```
```python
# __init__.py controls what gets exported
# mypackage/__init__.py
from .module_a import func_a
from .module_b import func_b

# Now users can import directly from the package
# from mypackage import func_a, func_b
```

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
