"""
Exercise 2: Exception Handling
Create exception handling utilities for an ML pipeline.
"""
import os


# Custom Exceptions
class DataLoadError(Exception):
    """Raised when data cannot be loaded."""
    pass


class ModelTrainingError(Exception):
    """Raised when model training fails."""
    pass


class ValidationError(ValueError):
    """Raised when validation fails."""
    pass


# Global lists for tracking resource management
opened_resources = []
closed_resources = []


class DataLoader:
    """Data loader with exception handling."""

    def load_data(self, filepath: str):
        """Load data from filepath, raise DataLoadError if file doesn't exist."""
        if not os.path.exists(filepath):
            raise DataLoadError(f"File not found: {filepath}")
        return f"Data loaded from {filepath}"

    def validate_data(self, data):
        """Validate data, raise ValidationError if empty or None."""
        if data is None:
            raise ValidationError("Data cannot be None")
        if isinstance(data, (list, dict, str)) and len(data) == 0:
            raise ValidationError("Data cannot be empty")
        return True


class ModelTrainer:
    """Model trainer with exception handling."""

    def train(self, data, epochs: int):
        """
        Train model on data for specified epochs.
        Raises ModelTrainingError if epochs < 1.
        Raises ValidationError if data is empty or None.
        """
        if epochs < 1:
            raise ModelTrainingError(f"Epochs must be >= 1, got {epochs}")

        if data is None or (isinstance(data, (list, dict)) and len(data) == 0):
            raise ValidationError("Cannot train on empty data")

        return f"Training completed for {epochs} epochs"

    def safe_train(self, data, epochs: int) -> dict:
        """
        Safely train model, catching exceptions and returning result dict.
        Returns dict with: success (bool), message (str), error (Exception or None)
        """
        try:
            result = self.train(data, epochs)
            return {
                "success": True,
                "message": result,
                "error": None
            }
        except (ModelTrainingError, ValidationError) as e:
            return {
                "success": False,
                "message": str(e),
                "error": e
            }


def safe_divide(a, b):
    """
    Safely divide a by b.
    Returns result if successful, None if ZeroDivisionError.
    Prints "Division successful" in else clause.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    else:
        print("Division successful")
        return result


def process_with_cleanup(resource_name: str):
    """
    Process resource with proper cleanup in finally block.
    Raises ValueError if resource_name is "bad_resource".
    Always appends to opened_resources and closed_resources lists.
    """
    try:
        # Simulate opening resource
        opened_resources.append(resource_name)

        # Simulate processing that might fail
        if resource_name == "bad_resource":
            raise ValueError(f"Cannot process {resource_name}")

        return f"Processed {resource_name}"

    except ValueError:
        raise  # Re-raise the exception

    finally:
        # Cleanup always happens
        closed_resources.append(resource_name)


# Example usage
if __name__ == "__main__":
    # Custom exceptions
    loader = DataLoader()
    try:
        loader.load_data("nonexistent.csv")
    except DataLoadError as e:
        print(f"Caught DataLoadError: {e}")

    # Validation
    try:
        loader.validate_data([])
    except ValidationError as e:
        print(f"Caught ValidationError: {e}")

    # Safe training
    trainer = ModelTrainer()
    result = trainer.safe_train([], epochs=10)
    print(f"Safe train result: {result}")

    result = trainer.safe_train([1, 2, 3], epochs=5)
    print(f"Safe train success: {result}")

    # Safe divide
    print(safe_divide(10, 2))  # 5.0
    print(safe_divide(10, 0))  # None

    # Resource cleanup
    opened_resources.clear()
    closed_resources.clear()

    process_with_cleanup("good_resource")
    print(f"Opened: {opened_resources}")
    print(f"Closed: {closed_resources}")

    try:
        process_with_cleanup("bad_resource")
    except ValueError as e:
        print(f"Error: {e}")
    print(f"After error - Opened: {opened_resources}, Closed: {closed_resources}")
