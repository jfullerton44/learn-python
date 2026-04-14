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

### Simple Function Composition Chain

```python
import functools

def compose(*functions):
    """Chain functions so each feeds into the next (left-to-right)."""
    def run(data):
        return functools.reduce(lambda v, f: f(v), functions, data)
    return run

strip_whitespace = lambda text: text.strip()
lowercase = lambda text: text.lower()
remove_punctuation = lambda text: "".join(c for c in text if c.isalnum() or c == " ")

clean = compose(strip_whitespace, lowercase, remove_punctuation)
print(clean("  Hello, World!  "))  # "hello world"
```

### DataFlow Class with Operator Chaining

```python
class DataFlow:
    """Chain transforms using the >> operator."""
    def __init__(self, func):
        self.func = func

    def __rshift__(self, other):
        """Enable flow1 >> flow2 syntax."""
        outer = self
        def combined(data):
            return other.func(outer.func(data))
        return DataFlow(combined)

    def run(self, data):
        return self.func(data)

tokenize = DataFlow(lambda s: s.split())
sort_words = DataFlow(lambda words: sorted(words))
join_csv = DataFlow(lambda words: ", ".join(words))

alphabetize = tokenize >> sort_words >> join_csv
print(alphabetize.run("banana cherry apple"))  # "apple, banana, cherry"
```

### Error-Aware Chain

```python
class SafeChain:
    """Chains transforms with per-step error handling."""
    def __init__(self):
        self._transforms = []

    def then(self, label, func):
        self._transforms.append((label, func))
        return self

    def run(self, data):
        for label, func in self._transforms:
            try:
                data = func(data)
            except Exception as exc:
                return {"error": f"'{label}' failed: {exc}", "last_good": data}
        return {"error": None, "result": data}

result = (SafeChain()
          .then("parse_ints", lambda xs: [int(x) for x in xs])
          .then("reciprocals", lambda xs: [1 / x for x in xs])
          .run(["4", "0", "2"]))
print(result)
# {'error': "'reciprocals' failed: division by zero", 'last_good': [4, 0, 2]}
```

### Lazy Stream Processing with Generators

```python
def stream_through(iterable, *transforms):
    """Push each item through all transforms one at a time (memory-efficient)."""
    for item in iterable:
        value = item
        for fn in transforms:
            value = fn(value)
        yield value

lines = ["  HELLO  ", " world ", "  PyThOn "]
cleaned = list(stream_through(
    lines,
    str.strip,
    str.lower,
    lambda s: s.capitalize(),
))
print(cleaned)  # ['Hello', 'World', 'Python']
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
