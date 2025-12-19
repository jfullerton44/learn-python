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
