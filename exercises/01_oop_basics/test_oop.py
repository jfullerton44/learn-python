"""
Tests for Exercise 1: Object-Oriented Programming Basics
"""
import pytest
from solution import Model, NeuralNetwork, ModelRegistry


class TestModel:
    """Tests for the Model class."""

    def test_model_initialization(self):
        """Test that Model initializes correctly."""
        model = Model(name="TestModel", version="1.0", parameters={"param1": 1})
        assert model.name == "TestModel"
        assert model.version == "1.0"
        assert model.parameters == {"param1": 1}

    def test_model_train(self):
        """Test the train method."""
        model = Model(name="TestModel", version="1.0", parameters={})
        result = model.train(["data"])
        assert "Training TestModel" in result

    def test_model_predict(self):
        """Test the predict method."""
        model = Model(name="TestModel", version="1.0", parameters={})
        result = model.predict("test_input")
        assert result == "prediction for test_input"

    def test_model_from_checkpoint(self):
        """Test the from_checkpoint class method."""
        checkpoint = {"name": "CheckpointModel", "version": "2.0", "parameters": {"lr": 0.01}}
        model = Model.from_checkpoint(checkpoint)
        assert model.name == "CheckpointModel"
        assert model.version == "2.0"
        assert model.parameters == {"lr": 0.01}

    def test_model_validate_parameters(self):
        """Test the validate_parameters static method."""
        assert Model.validate_parameters({"param": 1}) is True
        assert Model.validate_parameters({}) is True
        assert Model.validate_parameters([]) is False
        assert Model.validate_parameters("not a dict") is False

    def test_model_str(self):
        """Test the __str__ method."""
        model = Model(name="TestModel", version="1.0", parameters={})
        assert str(model) == "TestModel v1.0"

    def test_model_repr(self):
        """Test the __repr__ method."""
        model = Model(name="TestModel", version="1.0", parameters={})
        assert repr(model) == "Model(name=TestModel, version=1.0)"

    def test_model_equality(self):
        """Test the __eq__ method."""
        model1 = Model(name="TestModel", version="1.0", parameters={"a": 1})
        model2 = Model(name="TestModel", version="1.0", parameters={"b": 2})
        model3 = Model(name="OtherModel", version="1.0", parameters={"a": 1})

        assert model1 == model2  # Same name and version
        assert model1 != model3  # Different name
        assert model1 != "not a model"  # Different type


class TestNeuralNetwork:
    """Tests for the NeuralNetwork class."""

    def test_neural_network_initialization(self):
        """Test that NeuralNetwork initializes correctly."""
        nn = NeuralNetwork(name="MLP", version="1.0", parameters={}, activation="relu")
        assert nn.name == "MLP"
        assert nn.version == "1.0"
        assert nn.activation == "relu"
        assert nn.layers == []

    def test_neural_network_inheritance(self):
        """Test that NeuralNetwork inherits from Model."""
        nn = NeuralNetwork(name="MLP", version="1.0", parameters={}, activation="relu")
        assert isinstance(nn, Model)

    def test_add_layer(self):
        """Test adding layers to the neural network."""
        nn = NeuralNetwork(name="MLP", version="1.0", parameters={}, activation="relu")
        nn.add_layer("dense_1")
        nn.add_layer("dense_2")
        assert len(nn.layers) == 2
        assert nn.layers == ["dense_1", "dense_2"]

    def test_neural_network_train(self):
        """Test that train method is overridden correctly."""
        nn = NeuralNetwork(name="MLP", version="1.0", parameters={}, activation="relu")
        nn.add_layer("dense_1")
        nn.add_layer("dense_2")
        result = nn.train(["data"])
        assert "Training MLP" in result
        assert "2 layers" in result

    def test_neural_network_inherits_predict(self):
        """Test that predict method is inherited."""
        nn = NeuralNetwork(name="MLP", version="1.0", parameters={}, activation="relu")
        result = nn.predict("input")
        assert result == "prediction for input"


class TestModelRegistry:
    """Tests for the ModelRegistry class."""

    def test_registry_initialization(self):
        """Test that ModelRegistry initializes correctly."""
        registry = ModelRegistry()
        assert registry.models == {}

    def test_register_model(self):
        """Test registering a model."""
        registry = ModelRegistry()
        model = Model(name="TestModel", version="1.0", parameters={})
        registry.register(model)
        assert "TestModel" in registry.models
        assert registry.models["TestModel"] == model

    def test_get_model(self):
        """Test retrieving a model by name."""
        registry = ModelRegistry()
        model = Model(name="TestModel", version="1.0", parameters={})
        registry.register(model)
        retrieved = registry.get_model("TestModel")
        assert retrieved == model

    def test_get_nonexistent_model(self):
        """Test retrieving a model that doesn't exist."""
        registry = ModelRegistry()
        retrieved = registry.get_model("NonExistent")
        assert retrieved is None

    def test_registry_len(self):
        """Test the __len__ method."""
        registry = ModelRegistry()
        assert len(registry) == 0

        model1 = Model(name="Model1", version="1.0", parameters={})
        registry.register(model1)
        assert len(registry) == 1

        model2 = Model(name="Model2", version="1.0", parameters={})
        registry.register(model2)
        assert len(registry) == 2

    def test_registry_contains(self):
        """Test the __contains__ method."""
        registry = ModelRegistry()
        model = Model(name="TestModel", version="1.0", parameters={})
        registry.register(model)

        assert "TestModel" in registry
        assert "NonExistent" not in registry


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
