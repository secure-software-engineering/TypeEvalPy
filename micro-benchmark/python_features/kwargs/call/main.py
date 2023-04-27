# Call a function with keyword arguments.


def func1():
    return "Hello from func1"


def func(a):
    return a()


c = func(a=func1)
