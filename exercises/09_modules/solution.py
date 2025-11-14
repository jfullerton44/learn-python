"""
Exercise 9: Modules and Packages

This exercise demonstrates module organization.
The actual module files should be created separately:
- models/__init__.py
- models/base.py
- models/neural_net.py
- utils.py
"""


# models/base.py content
class BaseModel:
    """Base model class."""
    def __init__(self, name):
        self.name = name

    def train(self):
        return f"Training {self.name}"


# models/neural_net.py content
class NeuralNet(BaseModel):
    """Neural network model."""
    def __init__(self, name, layers):
        super().__init__(name)
        self.layers = layers

    def forward(self, x):
        return f"Forward pass through {len(self.layers)} layers"


# utils.py content
def load_data(path):
    """Load data from path."""
    return f"Data loaded from {path}"


def save_checkpoint(model, path):
    """Save model checkpoint."""
    return f"Saved {model.name} to {path}"


# Main script demonstration
if __name__ == "__main__":
    model = NeuralNet("MLP", [64, 128, 64])
    print(model.train())
    print(model.forward("input"))
    print(load_data("/data/train.csv"))
    print(save_checkpoint(model, "/checkpoints/model.pt"))
