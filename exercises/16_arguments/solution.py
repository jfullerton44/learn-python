"""Exercise 16: Arguments"""
def sum_all(*args):
    return sum(args)

def create_model(**kwargs):
    return kwargs

def train_model(data, *, epochs, learning_rate):
    return f"Training for {epochs} epochs with lr={learning_rate}"

def process(x, y, /, z):
    """x and y are positional-only, z can be keyword"""
    return x + y + z
