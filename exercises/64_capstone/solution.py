"""
Mini ML Framework - Capstone Project

This is a starter template. Students should expand this into a full framework.
"""

class Tensor:
    """Basic tensor with autograd support"""
    def __init__(self, data, requires_grad=False):
        self.data = data
        self.grad = None
        self.requires_grad = requires_grad

    def backward(self):
        if self.requires_grad:
            self.grad = 1.0

class Model:
    """Base model class"""
    def forward(self, x):
        return x

    def parameters(self):
        return []

class Trainer:
    """Training loop orchestrator"""
    def __init__(self, model, optimizer):
        self.model = model
        self.optimizer = optimizer
        self.callbacks = []

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def train(self, epochs):
        for epoch in range(epochs):
            for callback in self.callbacks:
                callback.on_epoch_start(epoch)
            # Training logic here
            for callback in self.callbacks:
                callback.on_epoch_end(epoch)

class DataLoader:
    """Custom data loader with caching"""
    def __init__(self, dataset, batch_size=32, cache=True):
        self.dataset = dataset
        self.batch_size = batch_size
        self.cache = cache
        self._cache = {}

    def __iter__(self):
        for i in range(0, len(self.dataset), self.batch_size):
            yield self.dataset[i:i+self.batch_size]

    def __len__(self):
        return (len(self.dataset) + self.batch_size - 1) // self.batch_size
