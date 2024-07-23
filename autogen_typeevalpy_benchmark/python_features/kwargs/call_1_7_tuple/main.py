# Call a function with keyword arguments.


def func1():
    return (97, 96, 39)


def func(a):
    return a()


c = func(a=func1)
