"""
Exercise 1: Object-Oriented Programming Basics
Create classes for a simple ML model management system.
"""


class Model:
    """Base class for ML models."""

    def __init__(self, name: str, version: str, parameters: dict):
        """Initialize a model with name, version, and parameters."""
        self.name = name
        self.version = version
        self.parameters = parameters

    def train(self, data):
        """Train the model on provided data."""
        print(f"Training {self.name}...")
        return f"Training {self.name}..."

    def predict(self, input_data):
        """Make a prediction on input data."""
        return f"prediction for {input_data}"

    @classmethod
    def from_checkpoint(cls, checkpoint_dict: dict):
        """Create a Model instance from a checkpoint dictionary."""
        return cls(
            name=checkpoint_dict["name"],
            version=checkpoint_dict["version"],
            parameters=checkpoint_dict["parameters"]
        )

    @staticmethod
    def validate_parameters(params):
        """Validate that parameters is a dictionary."""
        return isinstance(params, dict)

    def __str__(self):
        """Human-readable string representation."""
        return f"{self.name} v{self.version}"

    def __repr__(self):
        """Developer-friendly representation."""
        return f"Model(name={self.name}, version={self.version})"

    def __eq__(self, other):
        """Check equality based on name and version."""
        if not isinstance(other, Model):
            return False
        return self.name == other.name and self.version == other.version


class NeuralNetwork(Model):
    """Neural network model that inherits from Model."""

    def __init__(self, name: str, version: str, parameters: dict, activation: str):
        """Initialize a neural network with additional activation attribute."""
        super().__init__(name, version, parameters)
        self.layers = []
        self.activation = activation

    def add_layer(self, layer_name: str):
        """Add a layer to the neural network."""
        self.layers.append(layer_name)

    def train(self, data):
        """Train the neural network, including layer information."""
        num_layers = len(self.layers)
        message = f"Training {self.name} with {num_layers} layers..."
        print(message)
        return message


class ModelRegistry:
    """Registry to manage multiple models."""

    def __init__(self):
        """Initialize an empty model registry."""
        self.models = {}

    def register(self, model: Model):
        """Register a model in the registry."""
        self.models[model.name] = model

    def get_model(self, name: str):
        """Retrieve a model by name."""
        return self.models.get(name)

    def __len__(self):
        """Return the number of models in the registry."""
        return len(self.models)

    def __contains__(self, name: str):
        """Check if a model name exists in the registry."""
        return name in self.models


# Example usage
if __name__ == "__main__":
    # Create a model
    model = Model(name="LogisticRegression", version="1.0", parameters={"C": 1.0})
    print(model)  # LogisticRegression v1.0
    print(repr(model))  # Model(name=LogisticRegression, version=1.0)

    # Create a neural network
    nn = NeuralNetwork(name="MLP", version="2.0", parameters={}, activation="relu")
    nn.add_layer("dense_1")
    nn.add_layer("dense_2")
    nn.train(["data"])  # Training MLP with 2 layers...

    # Use class method
    checkpoint = {"name": "ResNet", "version": "1.0", "parameters": {"depth": 50}}
    model2 = Model.from_checkpoint(checkpoint)
    print(model2)

    # Use static method
    is_valid = Model.validate_parameters({"lr": 0.01})
    print(f"Parameters valid: {is_valid}")  # True

    # Model registry
    registry = ModelRegistry()
    registry.register(model)
    registry.register(nn)
    print(f"Registry size: {len(registry)}")  # 2
    print(f"MLP in registry: {'MLP' in registry}")  # True
