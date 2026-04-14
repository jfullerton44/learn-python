# Exercise 34: Jupyter Notebooks

## Concept

Jupyter notebooks are interactive computing environments combining code, text, and visualizations. This exercise simulates notebook concepts.

### Key Concepts

1. **Cell types**: Code and markdown cells
2. **Magic commands**: Special Jupyter commands
3. **Interactive execution**: Run code and see results
4. **Documentation**: Combine explanation with code

## AI/ML Application

- Exploratory data analysis
- Experiment documentation
- Interactive model development

## Code Examples

### Simulating Cell Execution

```python
# In Jupyter, each cell can be executed independently
# Code cells return the result of the last expression
def simulate_cell(code):
    """Simulate running a Jupyter code cell."""
    result = eval(code)
    print(f"Out: {result}")
    return result

simulate_cell("2 + 3")       # Out: 5
simulate_cell("[x**2 for x in range(5)]")  # Out: [0, 1, 4, 9, 16]
```

### Common Magic Commands

```python
# Magic commands are special Jupyter-only commands prefixed with % or %%
magic_commands = {
    "%timeit":      "Time a single line repeatedly for benchmarking",
    "%%time":       "Time the entire cell (runs once)",
    "%matplotlib":  "Set up matplotlib for inline display",
    "%run":         "Run an external Python script",
    "%who":         "List variables in the namespace",
    "%history":     "Show command history",
    "%pwd":         "Print the current working directory",
    "%%writefile":  "Write cell contents to a file",
}

# Example usage in a Jupyter notebook:
# %timeit sum(range(1000))
# %%time
# data = [x**2 for x in range(1_000_000)]
```

### Markdown and Code Cells

```python
# Jupyter notebooks are made of cells, each with a type
def create_markdown_cell(content):
    return {"cell_type": "markdown", "content": content}

def create_code_cell(code):
    return {"cell_type": "code", "content": code}

# Markdown cells support headers, lists, LaTeX, and more
intro = create_markdown_cell("# My Analysis\nThis notebook explores **sales data**.")
step1 = create_code_cell("import pandas as pd\ndf = pd.read_csv('sales.csv')")

print(intro)
# {'cell_type': 'markdown', 'content': '# My Analysis\nThis notebook explores **sales data**.'}
```

## Your Task

1. `simulate_cell_execution(code_string)` - Execute code string, return status and result
2. `list_magic_commands()` - Return list of common Jupyter magic commands
3. `create_markdown_cell(content)` - Return dict with cell_type and content
4. `create_code_cell(code)` - Return dict with cell_type and content

## Testing
```bash
pytest exercises/34_jupyter/test_jupyter.py -v
```
