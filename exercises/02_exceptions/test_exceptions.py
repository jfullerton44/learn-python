"""
Tests for Exercise 2: Exception Handling
"""
import pytest
import os
import tempfile
from exercise import (
    DataLoadError, ModelTrainingError, ValidationError,
    DataLoader, ModelTrainer, safe_divide, process_with_cleanup,
    opened_resources, closed_resources
)


class TestCustomExceptions:
    """Tests for custom exception classes."""

    def test_data_load_error(self):
        """Test that DataLoadError can be raised and caught."""
        with pytest.raises(DataLoadError):
            raise DataLoadError("Test error")

    def test_model_training_error(self):
        """Test that ModelTrainingError can be raised and caught."""
        with pytest.raises(ModelTrainingError):
            raise ModelTrainingError("Training failed")

    def test_validation_error_inherits_value_error(self):
        """Test that ValidationError inherits from ValueError."""
        assert issubclass(ValidationError, ValueError)

    def test_validation_error(self):
        """Test that ValidationError can be raised and caught."""
        with pytest.raises(ValidationError):
            raise ValidationError("Validation failed")


class TestDataLoader:
    """Tests for the DataLoader class."""

    def test_load_data_success(self):
        """Test loading data from an existing file."""
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp_path = tmp.name

        try:
            loader = DataLoader()
            result = loader.load_data(tmp_path)
            assert "Data loaded" in result
            assert tmp_path in result
        finally:
            os.unlink(tmp_path)

    def test_load_data_file_not_found(self):
        """Test that DataLoadError is raised for non-existent file."""
        loader = DataLoader()
        with pytest.raises(DataLoadError) as exc_info:
            loader.load_data("nonexistent_file.csv")
        assert "not found" in str(exc_info.value).lower()

    def test_validate_data_none(self):
        """Test that ValidationError is raised for None data."""
        loader = DataLoader()
        with pytest.raises(ValidationError) as exc_info:
            loader.validate_data(None)
        assert "None" in str(exc_info.value)

    def test_validate_data_empty_list(self):
        """Test that ValidationError is raised for empty list."""
        loader = DataLoader()
        with pytest.raises(ValidationError) as exc_info:
            loader.validate_data([])
        assert "empty" in str(exc_info.value).lower()

    def test_validate_data_empty_dict(self):
        """Test that ValidationError is raised for empty dict."""
        loader = DataLoader()
        with pytest.raises(ValidationError):
            loader.validate_data({})

    def test_validate_data_success(self):
        """Test that validate_data returns True for valid data."""
        loader = DataLoader()
        assert loader.validate_data([1, 2, 3]) is True
        assert loader.validate_data({"key": "value"}) is True
        assert loader.validate_data("data") is True


class TestModelTrainer:
    """Tests for the ModelTrainer class."""

    def test_train_success(self):
        """Test successful training."""
        trainer = ModelTrainer()
        result = trainer.train([1, 2, 3], epochs=5)
        assert "Training completed" in result
        assert "5 epochs" in result

    def test_train_invalid_epochs(self):
        """Test that ModelTrainingError is raised for invalid epochs."""
        trainer = ModelTrainer()
        with pytest.raises(ModelTrainingError):
            trainer.train([1, 2, 3], epochs=0)

        with pytest.raises(ModelTrainingError):
            trainer.train([1, 2, 3], epochs=-1)

    def test_train_empty_data(self):
        """Test that ValidationError is raised for empty data."""
        trainer = ModelTrainer()
        with pytest.raises(ValidationError):
            trainer.train([], epochs=5)

        with pytest.raises(ValidationError):
            trainer.train(None, epochs=5)

    def test_safe_train_success(self):
        """Test safe_train with successful training."""
        trainer = ModelTrainer()
        result = trainer.safe_train([1, 2, 3], epochs=5)

        assert result["success"] is True
        assert "Training completed" in result["message"]
        assert result["error"] is None

    def test_safe_train_training_error(self):
        """Test safe_train catches ModelTrainingError."""
        trainer = ModelTrainer()
        result = trainer.safe_train([1, 2, 3], epochs=0)

        assert result["success"] is False
        assert result["error"] is not None
        assert isinstance(result["error"], ModelTrainingError)

    def test_safe_train_validation_error(self):
        """Test safe_train catches ValidationError."""
        trainer = ModelTrainer()
        result = trainer.safe_train([], epochs=5)

        assert result["success"] is False
        assert result["error"] is not None
        assert isinstance(result["error"], ValidationError)


class TestSafeDivide:
    """Tests for the safe_divide function."""

    def test_safe_divide_success(self, capsys):
        """Test successful division."""
        result = safe_divide(10, 2)
        assert result == 5.0

        captured = capsys.readouterr()
        assert "Division successful" in captured.out

    def test_safe_divide_zero_division(self, capsys):
        """Test division by zero returns None."""
        result = safe_divide(10, 0)
        assert result is None

        captured = capsys.readouterr()
        assert "Division successful" not in captured.out

    def test_safe_divide_float_result(self):
        """Test division with float result."""
        result = safe_divide(7, 2)
        assert result == 3.5


class TestProcessWithCleanup:
    """Tests for the process_with_cleanup function."""

    def setup_method(self):
        """Clear resource lists before each test."""
        opened_resources.clear()
        closed_resources.clear()

    def test_process_with_cleanup_success(self):
        """Test successful resource processing."""
        result = process_with_cleanup("good_resource")

        assert result == "Processed good_resource"
        assert "good_resource" in opened_resources
        assert "good_resource" in closed_resources

    def test_process_with_cleanup_error(self):
        """Test that cleanup happens even on error."""
        with pytest.raises(ValueError):
            process_with_cleanup("bad_resource")

        assert "bad_resource" in opened_resources
        assert "bad_resource" in closed_resources

    def test_process_with_cleanup_multiple_resources(self):
        """Test processing multiple resources."""
        process_with_cleanup("resource1")
        process_with_cleanup("resource2")

        assert len(opened_resources) == 2
        assert len(closed_resources) == 2
        assert opened_resources == ["resource1", "resource2"]
        assert closed_resources == ["resource1", "resource2"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
