# Exercise 63: Packaging

## Concept

Python packaging enables sharing code as installable packages with dependencies and versioning.

### Key Concepts

1. **setup.py/pyproject.toml**: Package configuration
2. **Dependencies**: requirements and extras
3. **Versioning**: Semantic versioning
4. **Distribution**: PyPI, wheels

## AI/ML Application

- Sharing ML model packages
- Internal ML libraries
- Reproducible environments

## Code Examples

### Minimal pyproject.toml

```toml
[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.backends._legacy:_Backend"

[project]
name = "my-ml-toolkit"
version = "0.1.0"
description = "A small ML toolkit"
requires-python = ">=3.9"
dependencies = [
    "numpy>=1.24",
    "scikit-learn>=1.3",
]

[project.optional-dependencies]
dev = ["pytest>=7.0", "black"]
```

### Package Directory Structure

```
my_ml_toolkit/
├── pyproject.toml
├── README.md
├── src/
│   └── my_ml_toolkit/
│       ├── __init__.py       # from .model import train
│       ├── model.py          # Core ML logic
│       └── utils.py          # Helper functions
└── tests/
    ├── __init__.py
    └── test_model.py
```

### Entry Points — CLI Commands

```toml
# In pyproject.toml: make "ml-train" available as a shell command
[project.scripts]
ml-train = "my_ml_toolkit.cli:main"
```

```python
# src/my_ml_toolkit/cli.py
def main():
    """Entry point called when user runs 'ml-train' on the command line."""
    print("Starting training...")

if __name__ == "__main__":
    main()
```

### Versioning — Single Source of Truth

```python
# src/my_ml_toolkit/__init__.py
__version__ = "0.1.0"

# Access it programmatically:
# import my_ml_toolkit
# print(my_ml_toolkit.__version__)  # "0.1.0"
```

## Your Task

1. `MLComponent` class - Packageable component
2. `Pipeline` class - Pipeline module
3. `create_component(name)` - Factory
4. `validate_config(config)` - Validation

## Testing
```bash
pytest exercises/63_packaging/test_packaging.py -v
```
