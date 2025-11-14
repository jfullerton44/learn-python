"""
Exercise 4: Lambda Functions and Basic Functional Programming
"""
import math
from functools import reduce
from typing import List, Dict, Callable


def apply_activation(values: List[float], activation_name: str) -> List[float]:
    """Apply activation function using lambda and map()."""
    activations = {
        "relu": lambda x: max(0, x),
        "sigmoid": lambda x: 1 / (1 + math.exp(-x))
    }
    return list(map(activations[activation_name], values))


def filter_by_threshold(predictions: List[float], threshold: float) -> List[float]:
    """Filter predictions >= threshold using filter() and lambda."""
    return list(filter(lambda x: x >= threshold, predictions))


def sort_by_confidence(predictions: List[Dict[str, float]]) -> List[Dict[str, float]]:
    """Sort predictions by 'confidence' key in descending order."""
    return sorted(predictions, key=lambda x: x['confidence'], reverse=True)


def compute_total_loss(losses: List[float]) -> float:
    """Compute total loss using reduce()."""
    return reduce(lambda acc, x: acc + x, losses, 0.0)


def create_scaler(factor: float) -> Callable[[float], float]:
    """Return a lambda function that multiplies input by factor."""
    return lambda x: x * factor


# Example usage
if __name__ == "__main__":
    print("ReLU:", apply_activation([-1, 0, 1, 2], "relu"))
    print("Sigmoid:", apply_activation([0, 1, 2], "sigmoid"))
    print("Filter:", filter_by_threshold([0.3, 0.7, 0.5, 0.9], 0.6))
    print("Sort:", sort_by_confidence([
        {'pred': 'A', 'confidence': 0.7},
        {'pred': 'B', 'confidence': 0.9}
    ]))
    print("Total loss:", compute_total_loss([0.5, 0.3, 0.2]))
    scaler = create_scaler(10)
    print("Scaled:", scaler(5))
