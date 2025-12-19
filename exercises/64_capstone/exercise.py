"""
Mini ML Framework - Capstone Project

This is a starter template. Students should expand this into a full framework.

Complete the implementations below. Run tests to verify your solution.
"""


class Tensor:
    """Basic tensor with autograd support"""

    def __init__(self, data, requires_grad=False):
        """TODO: Implement this method"""
        # TODO: Implement
        pass

    def backward(self):
        """TODO: Implement this method"""
        # TODO: Implement
        pass



class Model:
    """Base model class"""

    def forward(self, x):
        """TODO: Implement this method"""
        # TODO: Implement
        pass

    def parameters(self):
        """TODO: Implement this method"""
        # TODO: Implement
        pass



class Trainer:
    """Training loop orchestrator"""

    def __init__(self, model, optimizer):
        """TODO: Implement this method"""
        # TODO: Implement
        pass

    def add_callback(self, callback):
        """TODO: Implement this method"""
        # TODO: Implement
        pass

    def train(self, epochs):
        """TODO: Implement this method"""
        # TODO: Implement
        pass



class DataLoader:
    """Custom data loader with caching"""

    def __init__(self, dataset, batch_size=32, cache=True):
        """TODO: Implement this method"""
        # TODO: Implement
        pass

    def __iter__(self):
        """TODO: Implement this method"""
        # TODO: Implement
        pass

    def __len__(self):
        """TODO: Implement this method"""
        # TODO: Implement
        pass
