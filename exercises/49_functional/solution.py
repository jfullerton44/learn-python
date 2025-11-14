"""Solution implementation"""
from typing import Any, Callable, Dict, List
import functools

class MLComponent:
    """Base class for ML components"""
    def __init__(self, name: str):
        self.name = name
    
    def process(self, data: Any) -> Any:
        return data
    
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name})"

class Pipeline:
    """ML Pipeline implementation"""
    def __init__(self):
        self.steps = []
    
    def add_step(self, component: MLComponent):
        self.steps.append(component)
        return self
    
    def execute(self, data: Any) -> Any:
        for step in self.steps:
            data = step.process(data)
        return data

def create_component(name: str) -> MLComponent:
    """Factory function"""
    return MLComponent(name)

# Additional utilities
def validate_config(config: Dict) -> bool:
    """Validate configuration dictionary"""
    required_keys = ['model', 'data']
    return all(k in config for k in required_keys)

def decorator_factory(param):
    """Decorator factory pattern"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Param: {param}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
