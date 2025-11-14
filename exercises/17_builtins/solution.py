"""Exercise 17: Builtins"""
def count_items(items):
    return len(items)

def create_pairs(list1, list2):
    return list(zip(list1, list2))

def enumerate_items(items):
    return list(enumerate(items))

def check_type(obj, expected_type):
    return isinstance(obj, expected_type)

def get_attribute(obj, attr_name, default=None):
    return getattr(obj, attr_name, default)

def find_extremes(numbers):
    return {"min": min(numbers), "max": max(numbers), "sum": sum(numbers)}
