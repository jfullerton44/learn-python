"""Exercise 30: Algorithm Complexity"""
def constant_time(items):
    """O(1) - constant time"""
    return items[0] if items else None

def linear_search(items, target):
    """O(n) - linear time"""
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1

def quadratic_operation(n):
    """O(n^2) - quadratic time"""
    result = []
    for i in range(n):
        for j in range(n):
            result.append(i * j)
    return result

def logarithmic_search(sorted_items, target):
    """O(log n) - binary search"""
    left, right = 0, len(sorted_items) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_items[mid] == target:
            return mid
        elif sorted_items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def analyze_complexity(operation_type):
    """Return complexity of operation"""
    complexities = {
        'dict_lookup': 'O(1)',
        'list_search': 'O(n)',
        'binary_search': 'O(log n)',
        'nested_loop': 'O(n^2)'
    }
    return complexities.get(operation_type)
