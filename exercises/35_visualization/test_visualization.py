"""Tests for Exercise 35"""
import pytest
import numpy as np
import tempfile
import os
from solution import create_line_plot, create_scatter_plot, create_histogram, create_subplots, save_figure

def test_create_line_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig = create_line_plot(x, y)
    assert fig is not None

def test_create_scatter_plot():
    x = np.random.rand(50)
    y = np.random.rand(50)
    fig = create_scatter_plot(x, y)
    assert fig is not None

def test_create_histogram():
    data = np.random.normal(0, 1, 1000)
    fig = create_histogram(data)
    assert fig is not None

def test_create_subplots():
    data_list = [np.sin(np.linspace(0, 10, 100)), np.cos(np.linspace(0, 10, 100))]
    titles = ["Sin", "Cos"]
    fig = create_subplots(data_list, titles)
    assert fig is not None

def test_save_figure():
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "test.png")
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        fig = create_line_plot(x, y)
        save_figure(fig, filepath)
        assert os.path.exists(filepath)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
