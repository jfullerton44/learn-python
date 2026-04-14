# Exercise 58: Config Systems

## Concept

Configuration systems manage settings across environments and provide validation and defaults.

### Key Concepts

1. **Hierarchical configs**: Override defaults
2. **Environment-specific**: Dev, staging, prod
3. **Validation**: Schema-based validation
4. **Formats**: YAML, TOML, JSON

## AI/ML Application

- Experiment configuration
- Hyperparameter management
- Deployment configs

## Code Examples

### Load Config from a Dictionary

```python
class Settings:
    """Simple settings container backed by a dictionary."""
    def __init__(self, defaults=None):
        self._store = defaults or {}

    def get(self, key, fallback=None):
        return self._store.get(key, fallback)

    def set(self, key, value):
        self._store[key] = value

app = Settings({"host": "localhost", "port": 8080})
print(app.get("host"))         # localhost
print(app.get("timeout", 30))  # 30 (fallback)
```

### Merge Configs — Hierarchical Overrides

```python
def deep_merge(base, overrides):
    """Recursively merge overrides into base config."""
    merged = base.copy()
    for key, value in overrides.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged

defaults = {"db": {"host": "localhost", "port": 5432}, "debug": True}
production = {"db": {"host": "db.prod.internal"}, "debug": False}

final = deep_merge(defaults, production)
print(final)
# {'db': {'host': 'db.prod.internal', 'port': 5432}, 'debug': False}
```

### Check Required Settings

```python
def check_settings(settings, required_keys):
    """Raise an error if any required key is missing from settings."""
    missing = [k for k in required_keys if k not in settings]
    if missing:
        raise ValueError(f"Missing required settings: {missing}")
    return True

settings = {"db_url": "sqlite:///app.db", "secret_key": "abc123"}
check_settings(settings, ["db_url", "secret_key"])  # OK
# check_settings(settings, ["redis_url"])  # Raises ValueError
```

### Environment Override

```python
import os

def apply_env_overrides(defaults, prefix="CFG"):
    """Override config values with environment variables."""
    config = defaults.copy()
    for key in defaults:
        env_key = f"{prefix}_{key.upper()}"
        env_val = os.environ.get(env_key)
        if env_val is not None:
            config[key] = type(defaults[key])(env_val)
    return config

defaults = {"workers": 4, "log_level": "info"}
# If CFG_WORKERS=8 is set in the environment, workers becomes 8
config = apply_env_overrides(defaults)
```

## Your Task

1. `MLComponent` class - Configurable component
2. `Pipeline` class - Config-driven pipeline
3. `create_component(name)` - Factory
4. `validate_config(config)` - Config validation with required keys

## Testing
```bash
pytest exercises/58_config_systems/test_config_systems.py -v
```
