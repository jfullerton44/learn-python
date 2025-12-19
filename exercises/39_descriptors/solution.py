"""Exercise 39: Descriptors"""
class TypedProperty:
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.data = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(id(instance))

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type}")
        self.data[id(instance)] = value

class Model:
    learning_rate = TypedProperty(float)
    epochs = TypedProperty(int)

    def __init__(self, lr, epochs):
        self.learning_rate = lr
        self.epochs = epochs

class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(instance)
        setattr(instance, self.name, value)
        return value
