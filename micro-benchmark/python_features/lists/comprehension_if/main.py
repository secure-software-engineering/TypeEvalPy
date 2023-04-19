# A comprehension calls two functions.


def func():
    return True


a = [a for a in range(10) if func()]
