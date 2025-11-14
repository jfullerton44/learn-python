"""Exercise 20: Dict/Set Advanced"""
def safe_get(d, key, default=None):
    return d.get(key, default)

def ensure_key(d, key, default_value):
    return d.setdefault(key, default_value)

def merge_dicts(d1, d2):
    return {**d1, **d2}

def set_union(s1, s2):
    return s1 | s2

def set_intersection(s1, s2):
    return s1 & s2

def set_difference(s1, s2):
    return s1 - s2
