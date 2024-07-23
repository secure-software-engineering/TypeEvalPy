# Call a function with keyword arguments.


def func1():
    return False


def func(a):
    return a()


c = func(a=func1)
