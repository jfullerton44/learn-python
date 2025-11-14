"""
Tests for Exercise 10: Virtual Environments and Dependencies
"""
import pytest
from solution import (
    create_requirements_dict, parse_requirements_file,
    generate_requirements_txt, check_package_installed, get_python_version
)


def test_create_requirements_dict():
    reqs = create_requirements_dict()
    assert isinstance(reqs, dict)
    assert "numpy" in reqs
    assert "pytest" in reqs
    assert all(isinstance(v, str) for v in reqs.values())


def test_parse_requirements_file():
    content = """
    numpy==1.24.0
    pandas==2.0.0
    # comment line
    scikit-learn==1.3.0
    """
    reqs = parse_requirements_file(content)
    assert reqs["numpy"] == "1.24.0"
    assert reqs["pandas"] == "2.0.0"
    assert reqs["scikit-learn"] == "1.3.0"
    assert len(reqs) == 3


def test_generate_requirements_txt():
    packages = {"numpy": "1.24.0", "pandas": "2.0.0"}
    result = generate_requirements_txt(packages)
    assert "numpy==1.24.0" in result
    assert "pandas==2.0.0" in result


def test_check_package_installed():
    # sys should always be available
    assert check_package_installed("sys") is True
    # Unlikely package name
    assert check_package_installed("nonexistent_package_xyz123") is False


def test_get_python_version():
    version = get_python_version()
    assert isinstance(version, str)
    parts = version.split('.')
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
