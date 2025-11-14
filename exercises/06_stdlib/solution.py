"""
Exercise 6: Standard Library Essentials
"""
import re
import argparse
import logging
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from typing import Dict, List


def count_tokens(text: str) -> Counter:
    """Use Counter to count word frequency."""
    words = text.lower().split()
    return Counter(words)


def create_default_config() -> defaultdict:
    """Return defaultdict(list) for model configs."""
    return defaultdict(list)


def parse_log_line(line: str) -> Dict[str, str]:
    """
    Extract timestamp and message from log line using regex.
    Expected format: "2024-01-15 10:30:45 - Message here"
    Returns dict with 'timestamp' and 'message' keys.
    """
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (.+)'
    match = re.search(pattern, line)
    if match:
        return {'timestamp': match.group(1), 'message': match.group(2)}
    return {'timestamp': '', 'message': ''}


def calculate_training_time(start: datetime, end: datetime) -> timedelta:
    """Return timedelta between start and end datetimes."""
    return end - start


def setup_logger(name: str, level: str = 'INFO') -> logging.Logger:
    """Create and return configured logger."""
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level))

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def parse_args_for_training(args_list=None):
    """Create argparse parser for training parameters."""
    parser = argparse.ArgumentParser(description='Train a model')
    parser.add_argument('--epochs', type=int, required=True, help='Number of epochs')
    parser.add_argument('--lr', type=float, required=True, help='Learning rate')
    parser.add_argument('--model', type=str, required=True, help='Model name')
    return parser.parse_args(args_list)


if __name__ == "__main__":
    print("Token count:", count_tokens("hello world hello"))
    print("Default config:", create_default_config())
    print("Parse log:", parse_log_line("2024-01-15 10:30:45 - Training started"))
