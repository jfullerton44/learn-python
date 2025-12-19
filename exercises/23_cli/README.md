# Exercise 23: Command Line Interfaces

## Concept

argparse module creates user-friendly command-line interfaces for Python scripts.

### Key Concepts

1. **ArgumentParser**: Main class for parsing arguments
2. **add_argument()**: Define expected arguments
3. **Required vs optional**: Flags and positional arguments
4. **Types and defaults**: Type conversion and default values

## AI/ML Application

- Training scripts with configurable hyperparameters
- Model inference tools
- Data processing pipelines

## Your Task

1. `create_training_parser()` - Create an ArgumentParser with:
   - `--model` (required string)
   - `--epochs` (int, default 10)
   - `--lr` (float, default 0.001)
   - `--verbose` (boolean flag)
2. `parse_training_args(args_list=None)` - Parse and return arguments

## Testing
```bash
pytest exercises/23_cli/test_cli.py -v
```
