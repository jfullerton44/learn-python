"""
Exercise 1: Object-Oriented Programming Basics
Create classes for a simple ML model management system.

Complete the implementations below. Run tests with:
    pytest test_oop.py -v
"""

class Model:
    """Base class for ML models.

    Attributes:
        name: Model name
        version: Model version
        parameters: Dictionary of model parameters
    """

    def __init__(self, name: str, version: str, parameters: dict):
        """Initialize a model with name, version, and parameters."""
        # TODO: Store the attributes
        pass

    def train(self, data):
        """Train the model on provided data.

        Should print and return: "Training {name}..."
        """
        # TODO: Implement training
        pass

    def predict(self, input_data):
        """Make a prediction on input data.

        Should return: "prediction for {input_data}"
        """
        # TODO: Implement prediction
        pass

    @classmethod
    def from_checkpoint(cls, checkpoint_dict: dict):
        """Create a Model instance from a checkpoint dictionary.

        The checkpoint_dict contains 'name', 'version', and 'parameters' keys.
        """
        # TODO: Create and return a Model from the checkpoint dict
        pass

    @staticmethod
    def validate_parameters(params):
        """Validate that parameters is a dictionary.

        Returns True if params is a dict, False otherwise.
        """
        # TODO: Implement validation
        pass

    def __str__(self):
        """Human-readable string representation.

        Should return: "{name} v{version}"
        """
        # TODO: Implement string representation
        pass

    def __repr__(self):
        """Developer-friendly representation.

        Should return: "Model(name={name}, version={version})"
        """
        # TODO: Implement repr
        pass

    def __eq__(self, other):
        """Check equality based on name and version."""
        # TODO: Implement equality check
        pass

class NeuralNetwork(Model):
    """Neural network model that inherits from Model.

    Additional attributes:
        layers: List of layer names
        activation: Activation function name
    """

    def __init__(self, name: str, version: str, parameters: dict, activation: str):
        """Initialize a neural network with additional activation attribute.

        Don't forget to call super().__init__() and initialize layers as empty list.
        """
        # TODO: Call parent __init__ and set layers and activation
        pass

    def add_layer(self, layer_name: str):
        """Add a layer to the neural network."""
        # TODO: Add layer to layers list
        pass

    def train(self, data):
        """Train the neural network, including layer information.

        Should print and return: "Training {name} with {num_layers} layers..."
        """
        # TODO: Override train to include layer count
        pass

class ModelRegistry:
    """Registry to manage multiple models.

    Attributes:
        models: Dictionary mapping model names to model instances
    """

    def __init__(self):
        """Initialize an empty model registry."""
        # TODO: Initialize models dict
        pass

    def register(self, model: Model):
        """Register a model in the registry using its name as key."""
        # TODO: Add model to registry
        pass

    def get_model(self, name: str):
        """Retrieve a model by name. Return None if not found."""
        # TODO: Return model or None
        pass

    def __len__(self):
        """Return the number of models in the registry."""
        # TODO: Return count
        pass

    def __contains__(self, name: str):
        """Check if a model name exists in the registry."""
        # TODO: Check if name in models
        pass
