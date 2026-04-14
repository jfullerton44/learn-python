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

## Code Examples

### Creating tensors (multi-dimensional arrays)

```python
import numpy as np

# 1D tensor (vector)
vector = np.array([1.0, 2.0, 3.0])

# 2D tensor (matrix)
matrix = np.zeros((3, 4))       # 3 rows, 4 columns of zeros
print(matrix.shape)              # (3, 4)

# 3D tensor (e.g., batch of images)
batch = np.random.randn(8, 28, 28)  # 8 images, 28×28 pixels
```

### Basic tensor operations

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 5.0, 6.0])

# Element-wise addition and multiplication
print(a + b)       # [5. 7. 9.]
print(a * b)       # [4. 10. 18.]

# Matrix multiplication
W = np.array([[1, 2], [3, 4], [5, 6]])  # 3×2
x = np.array([0.5, 1.5])                 # 2-element vector
result = np.matmul(W, x)                 # or W @ x
print(result)  # [ 3.5  7.5 11.5]
```

### Activation functions (ReLU)

```python
import numpy as np

def relu(x):
    """ReLU: returns x if positive, else 0. Adds non-linearity to networks."""
    return np.maximum(0, x)

values = np.array([-2.0, -0.5, 0.0, 1.0, 3.0])
print(relu(values))  # [0.  0.  0.  1.  3.]
```

### Simple neural network forward pass concept

```python
import numpy as np

def relu(x):
    return np.maximum(0, x)

# A 2-layer network: input(3) → hidden(4) → output(2)
input_data = np.array([0.5, 0.8, -0.2])
weights1 = np.random.randn(4, 3) * 0.1  # hidden layer weights
weights2 = np.random.randn(2, 4) * 0.1  # output layer weights

# Forward pass
hidden = relu(weights1 @ input_data)     # Layer 1 + activation
output = weights2 @ hidden               # Layer 2 (output)
print(output.shape)  # (2,)
```

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
