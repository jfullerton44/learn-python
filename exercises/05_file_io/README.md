# Exercise 5: File I/O Operations

## Concept
File operations for reading/writing text, CSV, JSON files. Use pathlib for modern path handling.

## AI/ML Application
- Loading datasets
- Saving model checkpoints
- Logging training results

## Code Examples

### Reading Text Files
```python
# Read entire file contents
with open("data.txt", "r") as f:
    content = f.read()

# Read line by line
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
```

### Writing Text Files
```python
# Write content to a file (overwrites existing)
with open("output.txt", "w") as f:
    f.write("Hello, world!\n")

# Append to an existing file
with open("log.txt", "a") as f:
    f.write("New log entry\n")
```

### CSV Operations
```python
import csv

# Read CSV into list of dicts
with open("data.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
# [{'name': 'Alice', 'score': '95'}, {'name': 'Bob', 'score': '87'}]

# Write list of dicts to CSV
data = [{"name": "Alice", "score": 95}, {"name": "Bob", "score": 87}]
with open("out.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(data)
```

### JSON File Operations
```python
import json

# Read JSON
with open("config.json", "r") as f:
    config = json.load(f)

# Write JSON (indent for readability)
config = {"epochs": 10, "lr": 0.001}
with open("config.json", "w") as f:
    json.dump(config, f, indent=2)
```

### pathlib for Paths
```python
from pathlib import Path

# Build paths in a cross-platform way
data_dir = Path("project") / "data"
filepath = data_dir / "train.csv"

# Create directories (including parents)
data_dir.mkdir(parents=True, exist_ok=True)

# Check if a file exists
if filepath.exists():
    text = filepath.read_text()
```

## Your Task
1. `read_text_file(filepath)` - Read and return file contents
2. `write_text_file(filepath, content)` - Write content to file
3. `read_csv_as_dicts(filepath)` - Read CSV, return list of dicts
4. `write_csv_from_dicts(filepath, data, fieldnames)` - Write list of dicts to CSV
5. `read_json(filepath)` - Read JSON file
6. `write_json(filepath, data)` - Write dict to JSON file
7. `append_to_log(filepath, message)` - Append message to log file
8. `ensure_directory_exists(dirpath)` - Create directory if it doesn't exist using pathlib

## Testing
```bash
pytest exercises/05_file_io/test_file_io.py -v
```
