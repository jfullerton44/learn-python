"""
Exercise 10: Virtual Environments and Dependencies
"""
import sys
import importlib.util
from typing import Dict


def create_requirements_dict() -> Dict[str, str]:
    """Return dictionary of package:version for ML project."""
    return {
        "numpy": "1.24.0",
        "pandas": "2.0.0",
        "scikit-learn": "1.3.0",
        "torch": "2.0.0",
        "pytest": "7.4.0"
    }


def parse_requirements_file(content: str) -> Dict[str, str]:
    """
    Parse requirements.txt content into dictionary.
    Format: package==version
    """
    requirements = {}
    for line in content.strip().split('\n'):
        line = line.strip()
        if line and not line.startswith('#'):
            if '==' in line:
                package, version = line.split('==')
                requirements[package.strip()] = version.strip()
    return requirements


def generate_requirements_txt(packages: Dict[str, str]) -> str:
    """Generate requirements.txt format string from dict."""
    lines = [f"{package}=={version}" for package, version in packages.items()]
    return '\n'.join(lines)


def check_package_installed(package_name: str) -> bool:
    """Check if a package is installed/available."""
    return importlib.util.find_spec(package_name) is not None


def get_python_version() -> str:
    """Return Python version string."""
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


if __name__ == "__main__":
    print("Requirements:", create_requirements_dict())
    print("Python version:", get_python_version())
    print("pytest installed:", check_package_installed("pytest"))
