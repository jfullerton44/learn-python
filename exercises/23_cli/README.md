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

## Code Examples

### Creating a Basic Parser

```python
import argparse

parser = argparse.ArgumentParser(description="A simple CLI tool")
args = parser.parse_args()  # Parses sys.argv by default
```

### Positional Arguments

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Path to the input file")
parser.add_argument("output", help="Path to the output file")

args = parser.parse_args(["data.csv", "results.json"])
print(args.filename)  # data.csv
print(args.output)    # results.json
```

### Optional Arguments with Defaults and Types

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--epochs", type=int, default=10, help="Number of epochs")
parser.add_argument("--lr", type=float, default=0.001, help="Learning rate")
parser.add_argument("--model", type=str, required=True, help="Model name")

args = parser.parse_args(["--model", "resnet", "--epochs", "50"])
print(args.model)   # resnet
print(args.epochs)  # 50
print(args.lr)      # 0.001 — uses default
```

### Boolean Flags with `store_true`

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
parser.add_argument("--no-cache", action="store_true", help="Disable caching")

args = parser.parse_args(["--verbose"])
print(args.verbose)   # True
print(args.no_cache)  # False — flag not provided
```

### Putting It All Together

```python
import argparse

parser = argparse.ArgumentParser(description="Train a model")
parser.add_argument("dataset", help="Path to training data")
parser.add_argument("--epochs", type=int, default=10)
parser.add_argument("--lr", type=float, default=0.001)
parser.add_argument("--verbose", action="store_true")

args = parser.parse_args(["train.csv", "--epochs", "25", "--verbose"])
print(f"Data: {args.dataset}, Epochs: {args.epochs}, LR: {args.lr}, Verbose: {args.verbose}")
# Data: train.csv, Epochs: 25, LR: 0.001, Verbose: True
```

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
