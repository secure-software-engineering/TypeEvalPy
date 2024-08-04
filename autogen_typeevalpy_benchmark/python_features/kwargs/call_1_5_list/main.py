# Call a function with keyword arguments.


def func1():
    return [10, 45, 61]


def func(a):
    return a()


c = func(a=func1)
