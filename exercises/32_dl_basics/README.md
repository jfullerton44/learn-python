# Exercise 32: Deep Learning Basics

## Concept

Deep learning fundamentals using NumPy as a proxy for tensor operations. Understanding core concepts before using frameworks.

### Key Concepts

1. **Tensors**: Multi-dimensional arrays
2. **Basic operations**: Add, multiply, matmul
3. **Neural network structure**: Weights, forward pass
4. **Activation functions**: ReLU

## AI/ML Application

- Understanding tensor operations
- Building intuition for neural networks
- Foundation for PyTorch/TensorFlow

## Your Task

1. `create_tensor(shape)` - Create a zero tensor of given shape
2. `tensor_add(a, b)` - Add two tensors
3. `tensor_multiply(a, b)` - Element-wise multiplication
4. `matrix_multiply(a, b)` - Matrix multiplication
5. `SimpleNeuralNet` class - Simple 2-layer network with forward pass
6. `create_network(input_size, hidden_size, output_size)` - Create neural network

## Testing
```bash
pytest exercises/32_dl_basics/test_dl.py -v
```
