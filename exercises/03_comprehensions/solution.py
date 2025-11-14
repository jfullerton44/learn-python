"""
Exercise 3: List/Dict/Set Comprehensions
Implement functions using comprehensions for data transformation.
"""
from typing import List, Dict, Set


def square_numbers(numbers: List[int]) -> List[int]:
    """Return list of squared numbers using list comprehension."""
    return [n ** 2 for n in numbers]


def filter_even(numbers: List[int]) -> List[int]:
    """Return list of only even numbers using list comprehension."""
    return [n for n in numbers if n % 2 == 0]


def create_feature_dict(names: List[str], values: List[float]) -> Dict[str, float]:
    """Create dictionary mapping names to values using dict comprehension."""
    return {name: value for name, value in zip(names, values)}


def extract_labels(data_dicts: List[Dict]) -> List:
    """Extract 'label' field from each dict in list."""
    return [d['label'] for d in data_dicts]


def flatten_matrix(matrix: List[List[int]]) -> List[int]:
    """Flatten 2D list into 1D list using nested comprehension."""
    return [item for row in matrix for item in row]


def unique_lengths(strings: List[str]) -> Set[int]:
    """Return set of unique string lengths using set comprehension."""
    return {len(s) for s in strings}


def conditional_transform(numbers: List[int]) -> List[int]:
    """Square if even, cube if odd using conditional comprehension."""
    return [n ** 2 if n % 2 == 0 else n ** 3 for n in numbers]


def batch_normalize(values: List[float], mean: float, std: float) -> List[float]:
    """Normalize values: (x - mean) / std."""
    return [(x - mean) / std for x in values]


# Example usage
if __name__ == "__main__":
    print("Square numbers:", square_numbers([1, 2, 3, 4]))
    print("Filter even:", filter_even([1, 2, 3, 4, 5]))
    print("Feature dict:", create_feature_dict(['a', 'b'], [1.0, 2.0]))
    print("Extract labels:", extract_labels([{'label': 'A'}, {'label': 'B'}]))
    print("Flatten:", flatten_matrix([[1, 2], [3, 4]]))
    print("Unique lengths:", unique_lengths(['a', 'ab', 'abc', 'ab']))
    print("Conditional transform:", conditional_transform([1, 2, 3, 4]))
    print("Batch normalize:", batch_normalize([1.0, 2.0, 3.0], mean=2.0, std=1.0))
