"""Exercise 32: DL Basics (using NumPy as proxy for tensors)"""
import numpy as np

def create_tensor(shape):
    """Create a tensor (array) of given shape"""
    return np.zeros(shape)

def tensor_add(a, b):
    """Add two tensors"""
    return a + b

def tensor_multiply(a, b):
    """Element-wise multiplication"""
    return a * b

def matrix_multiply(a, b):
    """Matrix multiplication"""
    return np.matmul(a, b)

class SimpleNeuralNet:
    """Conceptual neural network"""
    def __init__(self, input_size, hidden_size, output_size):
        self.w1 = np.random.randn(input_size, hidden_size) * 0.01
        self.w2 = np.random.randn(hidden_size, output_size) * 0.01
    
    def forward(self, x):
        """Forward pass"""
        hidden = np.maximum(0, np.dot(x, self.w1))  # ReLU
        output = np.dot(hidden, self.w2)
        return output

def create_network(input_size, hidden_size, output_size):
    return SimpleNeuralNet(input_size, hidden_size, output_size)
