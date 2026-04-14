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

## Code Examples

### Basic Logger Setup

```python
import logging

# Create a named logger
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)  # Capture all levels

# Add a console handler
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

logger.info("Application started")
```

### Log Levels

```python
import logging

logger = logging.getLogger("levels_demo")

logger.debug("Variable x = 42")           # Detailed diagnostic info
logger.info("Training started")            # General operational events
logger.warning("GPU memory running low")   # Something unexpected
logger.error("Failed to load dataset")     # A function failed
logger.critical("System out of memory")    # Program may crash
```

### Custom Formatter

```python
import logging

logger = logging.getLogger("formatted")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Training epoch 1 complete")
# Output: 2024-03-15 14:30:00,000 - formatted - INFO - Training epoch 1 complete
```

### File Handler — Log to a File

```python
import logging

logger = logging.getLogger("file_demo")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logger.addHandler(file_handler)

logger.info("This message goes to app.log")
```

## Your Task

1. `setup_basic_logger(name)` - Create and return a configured logger with StreamHandler
2. `log_training_progress(logger, epoch, loss)` - Log epoch and loss at INFO level
3. `log_error(logger, error_msg)` - Log error message at ERROR level
4. `log_debug(logger, msg)` - Log debug message at DEBUG level

## Testing
```bash
pytest exercises/22_logging_basics/test_logging.py -v
```
