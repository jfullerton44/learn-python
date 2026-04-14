# Exercise 6: Standard Library Essentials

## Concept
Master essential Python standard library modules: collections, datetime, re, os, sys, argparse, logging.

## AI/ML Application
- Experiment tracking with logging
- Data parsing with regex
- CLI tools with argparse
- Efficient data structures with collections

## Code Examples

### collections — Counter and defaultdict
```python
from collections import Counter, defaultdict

# Count occurrences of each item
words = ["the", "cat", "sat", "on", "the", "mat"]
counts = Counter(words)
print(counts.most_common(2))  # [('the', 2), ('cat', 1)]

# defaultdict provides a default value for missing keys
groups = defaultdict(list)
groups["optimizers"].append("adam")
groups["optimizers"].append("sgd")
groups["losses"].append("cross_entropy")
# {'optimizers': ['adam', 'sgd'], 'losses': ['cross_entropy']}
```

### datetime — Dates, Times, and Durations
```python
from datetime import datetime, timedelta

start = datetime(2024, 1, 15, 10, 0, 0)
end = datetime(2024, 1, 15, 12, 30, 0)
elapsed = end - start
print(elapsed)                # 2:30:00
print(elapsed.total_seconds())  # 9000.0

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))  # e.g. "2024-06-01 14:30"
```

### Regular Expressions
```python
import re

# Search for a pattern
line = "2024-01-15 10:30:00 INFO Training started"
match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)", line)
if match:
    timestamp, level, message = match.groups()
    # '2024-01-15 10:30:00', 'INFO', 'Training started'

# Find all occurrences
text = "Epochs: 10, LR: 0.001, Batch: 32"
numbers = re.findall(r"[\d.]+", text)
# ['10', '0.001', '32']
```

### logging — Structured Log Output
```python
import logging

logger = logging.getLogger("training")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.addHandler(handler)

logger.info("Epoch 1 complete, loss=0.42")
```

### argparse — Command-Line Interfaces
```python
import argparse

parser = argparse.ArgumentParser(description="Train a model")
parser.add_argument("--epochs", type=int, default=10)
parser.add_argument("--lr", type=float, default=0.001)
parser.add_argument("--model", type=str, default="resnet")

# In a script: args = parser.parse_args()
# Example usage: python train.py --epochs 20 --lr 0.01
```

## Your Task
1. `count_tokens(text)` - Use Counter to count word frequency
2. `create_default_config()` - Return defaultdict(list) for model configs
3. `parse_log_line(line)` - Extract timestamp and message using regex
4. `calculate_training_time(start, end)` - Return timedelta between datetimes
5. `setup_logger(name, level)` - Create and return configured logger
6. `parse_args_for_training()` - Create argparse parser for: --epochs, --lr, --model

## Testing
```bash
pytest exercises/06_stdlib/test_stdlib.py -v
```
