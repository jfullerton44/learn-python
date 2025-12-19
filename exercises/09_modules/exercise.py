"""
Exercise 9: Modules and Packages

This exercise demonstrates module organization.
The actual module files should be created separately:
- models/__init__.py
- models/base.py
- models/neural_net.py
- utils.py

Complete the implementations below. Run tests to verify your solution.
"""


class BaseModel:
    """Base model class."""

    def __init__(self, name):
        """TODO: Implement this method"""
        # TODO: Implement
        pass

    def train(self):
        """TODO: Implement this method"""
        # TODO: Implement
        pass



class NeuralNet(BaseModel):
    """Neural network model."""

    def __init__(self, name, layers):
        """TODO: Implement this method"""
        # TODO: Implement
        pass

    def forward(self, x):
        """TODO: Implement this method"""
        # TODO: Implement
        pass



def load_data(path):
    """Load data from path."""
    # TODO: Implement
    pass



def save_checkpoint(model, path):
    """Save model checkpoint."""
    # TODO: Implement
    pass
