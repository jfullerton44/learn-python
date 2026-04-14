# Exercise 10: Virtual Environments and Dependencies

## Concept
Using venv/virtualenv, pip, requirements.txt for reproducible Python environments.

## AI/ML Application
- Reproducible ML environments
- Managing project dependencies
- Isolating project dependencies

## Code Examples

### Creating and Activating a Virtual Environment
```bash
# Create a virtual environment
python -m venv myenv

# Activate it (Linux / macOS)
source myenv/bin/activate

# Activate it (Windows)
myenv\Scripts\activate

# Deactivate when done
deactivate
```

### pip — Installing and Managing Packages
```bash
# Install a package
pip install requests

# Install a specific version
pip install numpy==1.26.0

# List installed packages
pip list

# Show details about a package
pip show pandas
```

### requirements.txt Format
```text
# Pin exact versions for reproducibility
numpy==1.26.0
pandas==2.1.4
scikit-learn>=1.3,<1.5
requests~=2.31.0
```
```bash
# Install all dependencies from a requirements file
pip install -r requirements.txt

# Freeze current environment to a file
pip freeze > requirements.txt
```

### Checking Installed Packages from Python
```python
import importlib

# Check if a package is installed
try:
    importlib.import_module("numpy")
    print("numpy is installed")
except ImportError:
    print("numpy is NOT installed")

# Get Python version
import sys
print(sys.version)  # e.g. '3.11.5 (main, Sep 11 2023, ...)'
```

## Your Task
1. `create_requirements_dict()` - Return dict of package:version for ML project
2. `parse_requirements_file(content)` - Parse requirements.txt content into dict
3. `generate_requirements_txt(packages)` - Generate requirements.txt format string
4. `check_package_installed(package_name)` - Check if package is available
5. `get_python_version()` - Return Python version string

## Testing
```bash
pytest exercises/10_venv/test_venv.py -v
```
