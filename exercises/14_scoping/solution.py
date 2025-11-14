"""Exercise 14: Scoping"""
global_var = "global"

def demonstrate_legb():
    local_var = "local"
    return local_var

def use_global():
    global global_var
    global_var = "modified"
    return global_var

def use_nonlocal():
    x = "enclosing"
    def inner():
        nonlocal x
        x = "modified"
        return x
    return inner()

def create_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
