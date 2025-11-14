# Exercise 10: Virtual Environments and Dependencies

## Concept
Using venv/virtualenv, pip, requirements.txt for reproducible Python environments.

## AI/ML Application
- Reproducible ML environments
- Managing project dependencies
- Isolating project dependencies

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
