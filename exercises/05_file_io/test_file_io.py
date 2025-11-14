"""
Tests for Exercise 5: File I/O Operations
"""
import pytest
import os
import tempfile
import json
from pathlib import Path
from solution import (
    read_text_file, write_text_file, read_csv_as_dicts, write_csv_from_dicts,
    read_json, write_json, append_to_log, ensure_directory_exists
)


def test_read_write_text_file():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        filepath = f.name

    try:
        write_text_file(filepath, "Test content")
        assert read_text_file(filepath) == "Test content"
    finally:
        os.unlink(filepath)


def test_csv_operations():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
        filepath = f.name

    try:
        data = [
            {'name': 'Alice', 'score': '95'},
            {'name': 'Bob', 'score': '87'}
        ]
        write_csv_from_dicts(filepath, data, ['name', 'score'])
        result = read_csv_as_dicts(filepath)
        assert len(result) == 2
        assert result[0]['name'] == 'Alice'
        assert result[1]['score'] == '87'
    finally:
        os.unlink(filepath)


def test_json_operations():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        filepath = f.name

    try:
        data = {'model': 'ResNet', 'accuracy': 0.95}
        write_json(filepath, data)
        result = read_json(filepath)
        assert result == data
    finally:
        os.unlink(filepath)


def test_append_to_log():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        filepath = f.name

    try:
        append_to_log(filepath, "Line 1")
        append_to_log(filepath, "Line 2")
        content = read_text_file(filepath)
        assert "Line 1\n" in content
        assert "Line 2\n" in content
    finally:
        os.unlink(filepath)


def test_ensure_directory_exists():
    with tempfile.TemporaryDirectory() as tmpdir:
        new_dir = Path(tmpdir) / "subdir" / "nested"
        ensure_directory_exists(str(new_dir))
        assert new_dir.exists()
        assert new_dir.is_dir()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
