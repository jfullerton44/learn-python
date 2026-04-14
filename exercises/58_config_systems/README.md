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
# Simple config class backed by a dictionary
class Config:
    def __init__(self, defaults=None):
        self._data = defaults or {}

    def get(self, key, default=None):
        return self._data.get(key, default)

    def set(self, key, value):
        self._data[key] = value

cfg = Config({"learning_rate": 0.001, "epochs": 10})
print(cfg.get("learning_rate"))  # 0.001
print(cfg.get("batch_size", 32))  # 32 (default)
```

### Merge Configs — Hierarchical Overrides

```python
def merge_configs(base, overrides):
    """Deep-merge overrides into base config."""
    merged = base.copy()
    for key, value in overrides.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = merge_configs(merged[key], value)
        else:
            merged[key] = value
    return merged

base = {"model": {"layers": 3, "dropout": 0.1}, "lr": 0.001}
prod = {"model": {"dropout": 0.5}, "lr": 0.0001}

final = merge_configs(base, prod)
print(final)
# {'model': {'layers': 3, 'dropout': 0.5}, 'lr': 0.0001}
```

### Validate Config

```python
def validate_config(config, required_keys):
    """Raise an error if any required key is missing."""
    missing = [k for k in required_keys if k not in config]
    if missing:
        raise ValueError(f"Missing required config keys: {missing}")
    return True

config = {"model_name": "bert", "epochs": 5}
validate_config(config, ["model_name", "epochs"])  # OK
# validate_config(config, ["lr"])  # Raises ValueError
```

### Environment Override

```python
import os

def load_config_with_env(defaults):
    """Override config values with environment variables."""
    config = defaults.copy()
    for key in defaults:
        env_key = f"APP_{key.upper()}"
        env_val = os.environ.get(env_key)
        if env_val is not None:
            config[key] = type(defaults[key])(env_val)
    return config

defaults = {"batch_size": 32, "debug": "false"}
# If APP_BATCH_SIZE=64 is set in the environment, batch_size becomes 64
config = load_config_with_env(defaults)
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
