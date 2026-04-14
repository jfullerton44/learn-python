# Exercise 51: Factory and Builder Patterns

## Concept

Factory and Builder patterns create objects flexibly without exposing complex construction logic.

### Key Concepts

1. **Factory Method**: Create objects without specifying exact class
2. **Abstract Factory**: Families of related objects
3. **Builder**: Step-by-step construction
4. **Registration**: Dynamic factory configuration

## AI/ML Application

- Model factories for different architectures
- Dataset builders with configurable options
- Optimizer factories

## Code Examples

### Factory Function

```python
class CSVLoader:
    def load(self, path): return f"CSV data from {path}"

class JSONLoader:
    def load(self, path): return f"JSON data from {path}"

def create_loader(file_type):
    """Factory function — caller doesn't need to know the concrete classes."""
    loaders = {"csv": CSVLoader, "json": JSONLoader}
    if file_type not in loaders:
        raise ValueError(f"Unknown type: {file_type}")
    return loaders[file_type]()

loader = create_loader("csv")
print(loader.load("data.csv"))  # "CSV data from data.csv"
```

### Builder Pattern with Method Chaining

```python
class QueryBuilder:
    def __init__(self):
        self._table = None
        self._conditions = []
        self._limit = None

    def table(self, name):
        self._table = name
        return self  # Return self to enable chaining

    def where(self, condition):
        self._conditions.append(condition)
        return self

    def limit(self, n):
        self._limit = n
        return self

    def build(self):
        query = f"SELECT * FROM {self._table}"
        if self._conditions:
            query += " WHERE " + " AND ".join(self._conditions)
        if self._limit:
            query += f" LIMIT {self._limit}"
        return query

# Fluent, step-by-step construction
query = (QueryBuilder()
         .table("users")
         .where("age > 18")
         .where("active = true")
         .limit(10)
         .build())
print(query)
# "SELECT * FROM users WHERE age > 18 AND active = true LIMIT 10"
```

### Registration-Based Factory

```python
class ModelRegistry:
    """Dynamic factory — register new types at runtime."""
    def __init__(self):
        self._registry = {}

    def register(self, name, cls):
        self._registry[name] = cls

    def create(self, name, **kwargs):
        if name not in self._registry:
            raise KeyError(f"Unknown model: {name}")
        return self._registry[name](**kwargs)

registry = ModelRegistry()
registry.register("linear", lambda **kw: {"type": "linear", **kw})
registry.register("tree", lambda **kw: {"type": "tree", **kw})

model = registry.create("linear", lr=0.01)
print(model)  # {"type": "linear", "lr": 0.01}
```

## Your Task

1. `MLComponent` class - Base class for factory-created components
2. `Pipeline` class - Builder pattern for pipeline construction
3. `create_component(name)` - Factory function
4. `validate_config(config)` - Config validation

## Testing
```bash
pytest exercises/51_factory_builder/test_factory_builder.py -v
```
