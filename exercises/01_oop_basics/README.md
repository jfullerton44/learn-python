# Exercise 1: Object-Oriented Programming Basics

## Concept

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around "objects" - data structures that contain both data (attributes) and code (methods). Python supports OOP with classes, inheritance, and special methods.

### Key Concepts

1. **Classes and Instances**
   - Classes are blueprints for creating objects
   - Instances are individual objects created from a class
   - The `__init__` method initializes new instances

2. **Methods**
   - **Instance methods**: Operate on instance data, take `self` as first parameter
   - **Class methods**: Operate on class data, decorated with `@classmethod`, take `cls` as first parameter
   - **Static methods**: Don't access instance or class data, decorated with `@staticmethod`

3. **Inheritance**
   - Single inheritance: Class inherits from one parent
   - Multiple inheritance: Class inherits from multiple parents
   - `super()`: Calls methods from parent classes

4. **Special Methods (Dunder Methods)**
   - `__init__`: Constructor
   - `__str__`: Human-readable string representation
   - `__repr__`: Developer-friendly representation
   - `__eq__`: Equality comparison
   - `__len__`: Length of object
   - Many more for operator overloading, iteration, etc.

## AI/ML Application

In machine learning, OOP is fundamental:
- **Model classes**: Define neural network architectures (e.g., PyTorch `nn.Module`)
- **Dataset classes**: Encapsulate data loading logic
- **Custom layers**: Extend base classes to create new layer types
- **Training classes**: Organize training loops and state

## Your Task

Create the following classes for a simple ML model management system:

1. **`Model` class**: Base class for ML models
   - Attributes: `name`, `version`, `parameters` (dict)
   - Instance method: `train(data)` - prints training message
   - Instance method: `predict(input)` - returns "prediction for {input}"
   - Class method: `from_checkpoint(checkpoint_dict)` - creates Model from dict
   - Static method: `validate_parameters(params)` - checks if params is a dict
   - Special methods: `__str__`, `__repr__`, `__eq__`

2. **`NeuralNetwork` class**: Inherits from Model
   - Additional attributes: `layers` (list), `activation`
   - Override `train` to include layer information
   - Method: `add_layer(layer_name)` - adds layer to layers list
   - Use `super()` to call parent's `__init__`

3. **`ModelRegistry` class**: Manages multiple models
   - Attribute: `models` (dict mapping name to model)
   - Method: `register(model)` - adds model to registry
   - Method: `get_model(name)` - retrieves model by name
   - Special method: `__len__` - returns number of models
   - Special method: `__contains__` - checks if model name exists

## Example Usage

```python
# Create a model
model = Model(name="LogisticRegression", version="1.0", parameters={"C": 1.0})
print(model)  # Model(name=LogisticRegression, version=1.0)
print(str(model))  # LogisticRegression v1.0

# Create a neural network
nn = NeuralNetwork(name="MLP", version="2.0", parameters={}, activation="relu")
nn.add_layer("dense_1")
nn.add_layer("dense_2")
nn.train(["data"])  # Training MLP with 2 layers...

# Use class method
checkpoint = {"name": "ResNet", "version": "1.0", "parameters": {"depth": 50}}
model2 = Model.from_checkpoint(checkpoint)

# Use static method
is_valid = Model.validate_parameters({"lr": 0.01})  # True

# Model registry
registry = ModelRegistry()
registry.register(model)
registry.register(nn)
print(len(registry))  # 2
print("MLP" in registry)  # True
```

## Testing

Run the tests with:
```bash
pytest exercises/01_oop_basics/test_oop.py -v
```

## Additional Resources

- [Python Classes Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Real Python OOP Tutorial](https://realpython.com/python3-object-oriented-programming/)

## Common Pitfalls

1. Forgetting `self` as the first parameter in instance methods
2. Not calling `super().__init__()` in child class constructors
3. Confusing `__str__` and `__repr__` - str for end users, repr for developers
4. Not understanding method resolution order (MRO) in multiple inheritance
