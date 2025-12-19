"""
Exercise 38: Metaclasses

Complete the implementations below. Run tests to verify your solution.
"""

class ModelRegistry(type):
    """TODO: Implement this class"""

    def __new__(mcs, name, bases, attrs):
        """TODO: Implement this method"""
        # TODO: Implement
        pass

class BaseModel:
    """TODO: Implement this class"""

class ResNet(BaseModel):
    """TODO: Implement this class"""

class VGG(BaseModel):
    """TODO: Implement this class"""

def get_registered_models():
    """TODO: Implement this function"""
    # TODO: Implement
    pass

class AutoRegister(type):
    """TODO: Implement this class"""

    def __init_subclass__(cls):
        """TODO: Implement this method"""
        # TODO: Implement
        pass
