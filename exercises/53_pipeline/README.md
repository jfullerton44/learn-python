# Exercise 53: Pipeline Pattern

## Concept

Pipeline pattern chains processing stages for clean data flow and separation of concerns.

### Key Concepts

1. **Stage chaining**: Sequential processing
2. **Composability**: Mix and match stages
3. **Lazy evaluation**: Process on demand
4. **Error handling**: Pipeline-wide error management

## AI/ML Application

- Data preprocessing pipelines
- Feature engineering chains
- Inference pipelines

## Code Examples

### Simple Pipeline with Stages

```python
def normalize(data):
    max_val = max(data)
    return [x / max_val for x in data]

def round_values(data):
    return [round(x, 2) for x in data]

class Pipeline:
    def __init__(self):
        self._stages = []

    def add_stage(self, func):
        self._stages.append(func)
        return self  # Enable chaining

    def execute(self, data):
        for stage in self._stages:
            data = stage(data)
        return data

result = (Pipeline()
          .add_stage(normalize)
          .add_stage(round_values)
          .execute([10, 20, 50, 30]))
print(result)  # [0.2, 0.4, 1.0, 0.6]
```

### Composable Pipeline with Operator Chaining

```python
class Stage:
    def __init__(self, func):
        self.func = func

    def __or__(self, other):
        """Enable stage1 | stage2 syntax."""
        def combined(data):
            return other.func(self.func(data))
        return Stage(combined)

    def __call__(self, data):
        return self.func(data)

to_upper = Stage(lambda s: s.upper())
add_exclaim = Stage(lambda s: s + "!")
repeat = Stage(lambda s: s * 2)

shout = to_upper | add_exclaim | repeat
print(shout("hello"))  # "HELLO!HELLO!"
```

### Error Handling in a Pipeline

```python
class SafePipeline:
    def __init__(self):
        self._stages = []

    def add_stage(self, name, func):
        self._stages.append((name, func))
        return self

    def execute(self, data):
        for name, func in self._stages:
            try:
                data = func(data)
            except Exception as e:
                return {"error": f"Stage '{name}' failed: {e}", "data": data}
        return {"error": None, "data": data}

result = (SafePipeline()
          .add_stage("double", lambda x: [v * 2 for v in x])
          .add_stage("invert", lambda x: [1 / v for v in x])  # May divide by zero
          .execute([1, 0, 3]))
print(result)
# {"error": "Stage 'invert' failed: division by zero", "data": [2, 0, 6]}
```

### Lazy Pipeline with Generators

```python
def lazy_pipeline(data, *stages):
    """Process items one at a time through all stages (memory-efficient)."""
    for item in data:
        result = item
        for stage in stages:
            result = stage(result)
        yield result

results = list(lazy_pipeline(
    range(5),
    lambda x: x ** 2,
    lambda x: x + 1,
))
print(results)  # [1, 2, 5, 10, 17]
```

## Your Task

1. `MLComponent` class - Pipeline stage component
2. `Pipeline` class - Chain stages with add_step() and execute()
3. `create_component(name)` - Create pipeline stages
4. `validate_config(config)` - Pipeline config validation

## Testing
```bash
pytest exercises/53_pipeline/test_pipeline.py -v
```
