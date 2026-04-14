# Exercise 26: Environment Variables

## Concept

Environment variables store configuration outside code. Essential for managing secrets and environment-specific settings.

### Key Concepts

1. **os.environ**: Dictionary-like access to environment variables
2. **os.environ.get()**: Safe access with defaults
3. **Configuration patterns**: API keys, paths, feature flags

## AI/ML Application

- Managing API keys securely
- Environment-specific model paths
- Debug mode configuration

## Code Examples

### Reading environment variables safely with `os.getenv()`

```python
import os

# Returns None if not set
api_key = os.getenv("API_KEY")

# Provide a default value to avoid None
db_host = os.getenv("DB_HOST", "localhost")
print(db_host)  # 'localhost' if DB_HOST is not set
```

### Setting environment variables

```python
import os

os.environ["MODEL_PATH"] = "/models/v2/checkpoint.pt"
print(os.environ["MODEL_PATH"])  # '/models/v2/checkpoint.pt'

# Can also use os.getenv to read it back
print(os.getenv("MODEL_PATH"))  # '/models/v2/checkpoint.pt'
```

### Building configuration from environment variables

```python
import os

def load_config():
    return {
        "debug": os.getenv("DEBUG", "false").lower() == "true",
        "port": int(os.getenv("PORT", "8080")),
        "api_key": os.getenv("API_KEY", "default_key"),
    }

config = load_config()
print(config)  # {'debug': False, 'port': 8080, 'api_key': 'default_key'}
```

## Your Task

1. `get_env_var(var_name, default=None)` - Get env var with optional default
2. `set_env_var(var_name, value)` - Set an environment variable
3. `get_api_key()` - Get 'API_KEY' env var with 'default_key' as default
4. `get_model_path()` - Get 'MODEL_PATH' with '/default/path' as default
5. `load_env_config()` - Return dict with 'debug' (bool) and 'port' (int) from env

## Testing
```bash
pytest exercises/26_env_vars/test_env_vars.py -v
```
