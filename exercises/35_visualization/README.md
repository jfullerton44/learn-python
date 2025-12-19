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
