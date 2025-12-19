# Exercise 22: Basic Logging

## Concept

The logging module provides flexible event logging for applications. It's essential for debugging and monitoring ML training.

### Key Concepts

1. **Logger**: Named logging channel
2. **Handler**: Where logs are sent (console, file)
3. **Formatter**: Log message format
4. **Log Levels**: DEBUG, INFO, WARNING, ERROR, CRITICAL

## AI/ML Application

- Tracking training progress
- Recording experiment parameters
- Debugging model issues

## Your Task

1. `setup_basic_logger(name)` - Create and return a configured logger with StreamHandler
2. `log_training_progress(logger, epoch, loss)` - Log epoch and loss at INFO level
3. `log_error(logger, error_msg)` - Log error message at ERROR level
4. `log_debug(logger, msg)` - Log debug message at DEBUG level

## Testing
```bash
pytest exercises/22_logging_basics/test_logging.py -v
```
