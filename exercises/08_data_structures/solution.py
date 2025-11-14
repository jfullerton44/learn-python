"""
Exercise 8: Basic Data Structures
"""
from collections import deque
from typing import List, Tuple, Dict, Any, Callable


def store_predictions(predictions: List, labels: List) -> List[Tuple]:
    """Return list of tuples pairing predictions with labels."""
    return list(zip(predictions, labels))


def manage_hyperparams() -> Dict:
    """Return dictionary with nested hyperparameter structure."""
    return {
        "model": {
            "type": "neural_network",
            "layers": [64, 128, 64],
            "activation": "relu"
        },
        "training": {
            "epochs": 100,
            "batch_size": 32,
            "learning_rate": 0.001
        }
    }


def deduplicate_samples(samples: List) -> List:
    """Use set to remove duplicates while preserving order."""
    seen = set()
    result = []
    for sample in samples:
        if sample not in seen:
            seen.add(sample)
            result.append(sample)
    return result


def cache_results(func: Callable, args_list: List[Any]) -> Dict[Any, Any]:
    """Cache function results in dictionary."""
    cache = {}
    for arg in args_list:
        if arg not in cache:
            cache[arg] = func(arg)
    return cache


class Stack:
    """Simple stack implementation using list."""
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def implement_stack():
    """Return a Stack instance."""
    return Stack()


class Queue:
    """Queue implementation using collections.deque."""
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def implement_queue():
    """Return a Queue instance."""
    return Queue()


if __name__ == "__main__":
    print(store_predictions([1, 0, 1], [1, 0, 0]))
    print(manage_hyperparams())
    print(deduplicate_samples([1, 2, 2, 3, 1, 4]))
    print(cache_results(lambda x: x**2, [1, 2, 3, 2, 1]))
