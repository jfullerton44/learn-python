"""Exercise 21: Pythonic Idioms"""
def eafp_file_read(filepath):
    """Easier to Ask Forgiveness than Permission"""
    try:
        with open(filepath) as f:
            return f.read()
    except FileNotFoundError:
        return None

def lbyl_file_read(filepath):
    """Look Before You Leap"""
    import os
    if os.path.exists(filepath):
        with open(filepath) as f:
            return f.read()
    return None

def duck_typing_len(obj):
    """If it has __len__, treat it as a sequence"""
    return len(obj)

def pythonic_swap(a, b):
    """Pythonic way to swap values"""
    return b, a

def list_comprehension_even(numbers):
    """Pythonic filtering"""
    return [n for n in numbers if n % 2 == 0]
