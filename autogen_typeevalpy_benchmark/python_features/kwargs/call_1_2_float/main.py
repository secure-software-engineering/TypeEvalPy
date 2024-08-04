# Call a function with keyword arguments.


def func1():
    return 82.08


def func(a):
    return a()


c = func(a=func1)
