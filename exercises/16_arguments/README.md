# Exercise 16: Argument Handling

## Concept

Python offers flexible argument handling with *args, **kwargs, keyword-only, and positional-only arguments for creating versatile function interfaces.

### Key Concepts

1. **`*args`**: Capture variable positional arguments as a tuple
2. **`**kwargs`**: Capture variable keyword arguments as a dict
3. **Keyword-only**: Arguments after `*` must be passed by keyword
4. **Positional-only**: Arguments before `/` must be passed by position (Python 3.8+)

## AI/ML Application

- Flexible model configuration functions
- Wrapper functions for training loops
- API design for ML libraries

## Your Task

1. `sum_all(*args)` - Sum any number of arguments using *args
2. `create_model(**kwargs)` - Accept any keyword arguments, return as dict
3. `train_model(data, *, epochs, learning_rate)` - Keyword-only args after data
4. `process(x, y, /, z)` - x and y are positional-only, z can be keyword

## Testing
```bash
pytest exercises/16_arguments/test_arguments.py -v
```
