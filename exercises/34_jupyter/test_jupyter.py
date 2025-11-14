"""Tests for Exercise 34"""
import pytest
from solution import simulate_cell_execution, list_magic_commands, create_markdown_cell, create_code_cell

def test_simulate_cell_execution():
    result = simulate_cell_execution("2 + 2")
    assert result["status"] == "success"
    assert result["result"] == 4

def test_list_magic_commands():
    commands = list_magic_commands()
    assert "%timeit" in commands
    assert "%matplotlib" in commands

def test_create_markdown_cell():
    cell = create_markdown_cell("# Header")
    assert cell["cell_type"] == "markdown"
    assert "Header" in cell["content"]

def test_create_code_cell():
    cell = create_code_cell("print('hello')")
    assert cell["cell_type"] == "code"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
