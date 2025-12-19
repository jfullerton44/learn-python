"""
Exercise 2: Exception Handling
Create exception handling utilities for an ML pipeline.

Complete the implementations below. Run tests to verify your solution.
"""
opened_resources = []
closed_resources = []

class DataLoadError(Exception):
    """Raised when data cannot be loaded."""

class ModelTrainingError(Exception):
    """Raised when model training fails."""

class ValidationError(ValueError):
    """Raised when validation fails."""

class DataLoader:
    """Data loader with exception handling."""

    def load_data(self, filepath: str):
        """Load data from filepath, raise DataLoadError if file doesn't exist."""
        # TODO: Implement
        pass

    def validate_data(self, data):
        """Validate data, raise ValidationError if empty or None."""
        # TODO: Implement
        pass

class ModelTrainer:
    """Model trainer with exception handling."""

    def train(self, data, epochs: int):
        """Train model on data for specified epochs.
Raises ModelTrainingError if epochs < 1.
Raises ValidationError if data is empty or None."""
        # TODO: Implement
        pass

    def safe_train(self, data, epochs: int):
        """Safely train model, catching exceptions and returning result dict.
Returns dict with: success (bool), message (str), error (Exception or None)"""
        # TODO: Implement
        pass

def safe_divide(a, b):
    """Safely divide a by b.
Returns result if successful, None if ZeroDivisionError.
Prints "Division successful" in else clause."""
    # TODO: Implement
    pass

def process_with_cleanup(resource_name: str):
    """Process resource with proper cleanup in finally block.
Raises ValueError if resource_name is "bad_resource".
Always appends to opened_resources and closed_resources lists."""
    # TODO: Implement
    pass
