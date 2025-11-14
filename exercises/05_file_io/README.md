# Exercise 5: File I/O Operations

## Concept
File operations for reading/writing text, CSV, JSON files. Use pathlib for modern path handling.

## AI/ML Application
- Loading datasets
- Saving model checkpoints
- Logging training results

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
