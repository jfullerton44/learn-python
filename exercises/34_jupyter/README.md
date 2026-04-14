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
def run_expression(expr_string):
    """Demonstrate how Jupyter evaluates and displays results."""
    try:
        output = eval(expr_string)
        return {"status": "ok", "output": output}
    except Exception as e:
        return {"status": "error", "output": str(e)}

print(run_expression("3 * 7"))            # {'status': 'ok', 'output': 21}
print(run_expression("1 / 0"))            # {'status': 'error', 'output': 'division by zero'}
```

### Common Magic Commands

```python
# Magic commands are special Jupyter-only commands prefixed with % or %%
jupyter_specials = [
    ("%timeit",     "Benchmark a single line by running it many times"),
    ("%%time",      "Measure wall time for an entire cell"),
    ("%matplotlib", "Enable inline plotting"),
    ("%run",        "Execute an external .py script"),
    ("%who",        "Show all variables in the current namespace"),
    ("%history",    "Display input history"),
    ("%pwd",        "Print current working directory"),
    ("%%writefile", "Save cell contents to a file on disk"),
]

# Example usage in a Jupyter notebook:
# %timeit sorted(range(1000))
# %%time
# results = [n ** 0.5 for n in range(1_000_000)]
```

### Markdown and Code Cells

```python
# Jupyter notebooks are JSON files with a list of cell dicts
# Each cell has a "cell_type" and source content

# A notebook is essentially a list of cell structures:
notebook_cells = [
    {"cell_type": "markdown", "content": "# Experiment Log\nResults from **trial 3**."},
    {"cell_type": "code",     "content": "import numpy as np\ndata = np.random.randn(100)"},
    {"cell_type": "markdown", "content": "## Summary\nMean and std of the sample:"},
    {"cell_type": "code",     "content": "print(f'mean={data.mean():.2f}, std={data.std():.2f}')"},
]

for cell in notebook_cells:
    print(f"[{cell['cell_type'].upper()}] {cell['content'][:40]}...")
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
