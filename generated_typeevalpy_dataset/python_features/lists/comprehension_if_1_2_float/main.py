# A comprehension calls two functions.


def func():
    return 47.95


a = [a for a in range(10) if func()]
