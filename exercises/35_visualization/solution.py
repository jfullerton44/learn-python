"""Exercise 35: Visualization"""
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import numpy as np

def create_line_plot(x, y, title="Line Plot"):
    """Create a simple line plot"""
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(title)
    return fig

def create_scatter_plot(x, y, title="Scatter Plot"):
    """Create a scatter plot"""
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_title(title)
    return fig

def create_histogram(data, bins=10, title="Histogram"):
    """Create a histogram"""
    fig, ax = plt.subplots()
    ax.hist(data, bins=bins)
    ax.set_title(title)
    return fig

def create_subplots(data_list, titles):
    """Create multiple subplots"""
    fig, axes = plt.subplots(1, len(data_list), figsize=(12, 4))
    for i, (data, title) in enumerate(zip(data_list, titles)):
        axes[i].plot(data)
        axes[i].set_title(title)
    return fig

def save_figure(fig, filename):
    """Save figure to file"""
    fig.savefig(filename)
    plt.close(fig)
