"""Exercise 28: Slicing"""
def get_every_nth(items, n):
    return items[::n]

def reverse_list(items):
    return items[::-1]

def get_last_n(items, n):
    return items[-n:]

def get_middle_section(items, start_frac=0.25, end_frac=0.75):
    start = int(len(items) * start_frac)
    end = int(len(items) * end_frac)
    return items[start:end]

def create_slice_object(start, stop, step=1):
    return slice(start, stop, step)

def apply_slice(items, slice_obj):
    return items[slice_obj]
