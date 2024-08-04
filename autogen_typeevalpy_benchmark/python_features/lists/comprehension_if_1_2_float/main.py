# A comprehension calls two functions.


def func():
    return 34.01


a = [a for a in range(10) if func()]
