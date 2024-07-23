# Call a function with keyword arguments.


def func1():
    return [42, 89, 79]


def func(a):
    return a()


c = func(a=func1)
