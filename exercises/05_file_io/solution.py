"""
Exercise 5: File I/O Operations
"""
import csv
import json
from pathlib import Path
from typing import List, Dict, Any


def read_text_file(filepath: str) -> str:
    """Read and return file contents."""
    with open(filepath, 'r') as f:
        return f.read()


def write_text_file(filepath: str, content: str):
    """Write content to file."""
    with open(filepath, 'w') as f:
        f.write(content)


def read_csv_as_dicts(filepath: str) -> List[Dict[str, str]]:
    """Read CSV file and return list of dictionaries."""
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_csv_from_dicts(filepath: str, data: List[Dict], fieldnames: List[str]):
    """Write list of dicts to CSV file."""
    with open(filepath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def read_json(filepath: str) -> Any:
    """Read JSON file and return parsed data."""
    with open(filepath, 'r') as f:
        return json.load(f)


def write_json(filepath: str, data: Any):
    """Write data to JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)


def append_to_log(filepath: str, message: str):
    """Append message to log file."""
    with open(filepath, 'a') as f:
        f.write(message + '\n')


def ensure_directory_exists(dirpath: str):
    """Create directory if it doesn't exist using pathlib."""
    Path(dirpath).mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    # Example usage
    write_text_file("/tmp/test.txt", "Hello, World!")
    print(read_text_file("/tmp/test.txt"))
