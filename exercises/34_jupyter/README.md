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

## Your Task

1. `simulate_cell_execution(code_string)` - Execute code string, return status and result
2. `list_magic_commands()` - Return list of common Jupyter magic commands
3. `create_markdown_cell(content)` - Return dict with cell_type and content
4. `create_code_cell(code)` - Return dict with cell_type and content

## Testing
```bash
pytest exercises/34_jupyter/test_jupyter.py -v
```
