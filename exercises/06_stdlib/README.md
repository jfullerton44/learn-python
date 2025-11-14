# Exercise 6: Standard Library Essentials

## Concept
Master essential Python standard library modules: collections, datetime, re, os, sys, argparse, logging.

## AI/ML Application
- Experiment tracking with logging
- Data parsing with regex
- CLI tools with argparse
- Efficient data structures with collections

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
