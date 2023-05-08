# Applying multiple functions to a single argument using nested function calls.


def add_one(x):
    return x + 1


def double(x):
    return x * 2


result = double(add_one(5))
