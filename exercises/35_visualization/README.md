# Exercise 35: Matplotlib/Seaborn Basics

## Concept

Matplotlib is Python's core plotting library. Learn to create common visualizations for data analysis and model evaluation.

### Key Concepts

1. **Line plots**: Trends and time series
2. **Scatter plots**: Relationships between variables
3. **Histograms**: Data distributions
4. **Subplots**: Multiple plots in one figure
5. **Saving figures**: Export to files

## AI/ML Application

- Visualizing training curves
- Plotting model predictions
- Exploratory data analysis

## Code Examples

### Line Plot

```python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(x, y, color="blue", linestyle="--", marker="o", label="y = x²")
ax.set_title("Line Plot Example")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.show()
```

### Scatter Plot

```python
import matplotlib.pyplot as plt
import random

heights = [150 + random.gauss(0, 10) for _ in range(50)]
weights = [h * 0.6 + random.gauss(0, 5) for h in heights]

fig, ax = plt.subplots()
ax.scatter(heights, weights, alpha=0.7, edgecolors="black")
ax.set_title("Height vs Weight")
ax.set_xlabel("Height (cm)")
ax.set_ylabel("Weight (kg)")
plt.show()
```

### Histogram

```python
import matplotlib.pyplot as plt
import random

scores = [random.gauss(75, 10) for _ in range(200)]

fig, ax = plt.subplots()
ax.hist(scores, bins=20, color="skyblue", edgecolor="black")
ax.set_title("Exam Score Distribution")
ax.set_xlabel("Score")
ax.set_ylabel("Frequency")
plt.show()
```

### Subplots

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot([1, 2, 3], [1, 4, 9])
axes[0].set_title("Line")

axes[1].bar(["A", "B", "C"], [5, 7, 3])
axes[1].set_title("Bar")

axes[2].scatter([1, 2, 3, 4], [10, 20, 25, 30])
axes[2].set_title("Scatter")

fig.suptitle("Multiple Subplots")
plt.tight_layout()
plt.show()
```

### Saving a Figure

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
ax.set_title("Saved Plot")

# Save as PNG with high resolution
fig.savefig("my_plot.png", dpi=150, bbox_inches="tight")

# Save as PDF for publication
fig.savefig("my_plot.pdf", bbox_inches="tight")

plt.close(fig)  # Close to free memory
```

## Your Task

1. `create_line_plot(x, y, title)` - Create and return a line plot figure
2. `create_scatter_plot(x, y, title)` - Create and return a scatter plot
3. `create_histogram(data, bins, title)` - Create histogram
4. `create_subplots(data_list, titles)` - Create multiple subplots
5. `save_figure(fig, filename)` - Save figure to file

## Testing
```bash
pytest exercises/35_visualization/test_visualization.py -v
```
