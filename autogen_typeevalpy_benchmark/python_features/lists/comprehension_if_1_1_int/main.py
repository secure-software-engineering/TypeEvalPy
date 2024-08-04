# A comprehension calls two functions.


def func():
    return 99


a = [a for a in range(10) if func()]
