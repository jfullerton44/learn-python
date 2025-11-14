"""Exercise 15: Type Hints"""
from typing import List, Dict, Optional, Tuple

def process_numbers(numbers: List[int]) -> int:
    return sum(numbers)

def get_config() -> Dict[str, any]:
    return {"model": "resnet", "lr": 0.001}

def find_item(items: List[str], target: str) -> Optional[int]:
    try:
        return items.index(target)
    except ValueError:
        return None

def split_data(data: List[float], ratio: float) -> Tuple[List[float], List[float]]:
    split_point = int(len(data) * ratio)
    return data[:split_point], data[split_point:]
