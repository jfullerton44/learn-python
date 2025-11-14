"""Exercise 38: Metaclasses"""
class ModelRegistry(type):
    models = {}
    
    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        if name != 'BaseModel':
            mcs.models[name] = cls
        return cls

class BaseModel(metaclass=ModelRegistry):
    pass

class ResNet(BaseModel):
    pass

class VGG(BaseModel):
    pass

def get_registered_models():
    return ModelRegistry.models

class AutoRegister(type):
    def __init_subclass__(cls):
        print(f"Registering {cls.__name__}")
