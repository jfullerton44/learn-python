"""
Exercise 3: List/Dict/Set Comprehensions
Implement functions using comprehensions for data transformation.

Complete the implementations below. Run tests to verify your solution.
"""

def square_numbers(numbers):
    """Return list of squared numbers using list comprehension."""
    return [x**2 for x in numbers]

def filter_even(numbers):
    """Return list of only even numbers using list comprehension."""
    return [x for x in numbers if x%2 == 0]

def create_feature_dict(names, values):
    """Create dictionary mapping names to values using dict comprehension."""
    return {name: value for name, value in zip(names, values)}

def extract_labels(data_dicts):
    """Extract 'label' field from each dict in list."""
    return [item['label'] for item in data_dicts]
    pass

def flatten_matrix(matrix):
    """Flatten 2D list into 1D list using nested comprehension."""
    return [item for row in matrix for item in row]

def unique_lengths(strings):
    """Return set of unique string lengths using set comprehension."""
    return {len(s) for s in strings}

def conditional_transform(numbers):
    """Square if even, cube if odd using conditional comprehension."""
    return [x**2 if x%2 == 0 else x**3 for x in numbers]
    

def batch_normalize(values, mean: float, std: float):
    """Normalize values: (x - mean) / std."""
    return [(x- mean)/ std for x in values]
    
