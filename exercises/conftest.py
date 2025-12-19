"""
Pytest configuration for learn-python exercises.

Each exercise directory is treated as an independent module namespace.
This allows tests to import from 'exercise' without conflicts.
"""
import sys
from pathlib import Path

import pytest


def pytest_configure(config):
    """Configure pytest for per-exercise imports."""
    # Remove any cached 'exercise' modules at the start
    for name in list(sys.modules.keys()):
        if name == 'exercise' or name == 'solution':
            del sys.modules[name]


@pytest.hookimpl(tryfirst=True)
def pytest_collect_file(parent, file_path):
    """Hook into collection to set up proper import paths."""
    if file_path.name.startswith('test_') and file_path.suffix == '.py':
        test_dir = file_path.parent

        # Clear any cached exercise/solution modules
        for name in list(sys.modules.keys()):
            if name == 'exercise' or name == 'solution':
                del sys.modules[name]

        # Add test directory to path for this collection
        if str(test_dir) not in sys.path:
            sys.path.insert(0, str(test_dir))


@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item, nextitem):
    """Clean up sys.path after running tests."""
    test_dir = Path(item.fspath).parent

    # Clear cached imports
    modules_to_remove = [
        name for name in sys.modules
        if name == 'exercise' or name == 'solution'
    ]
    for name in modules_to_remove:
        del sys.modules[name]

