# Call a function with keyword arguments.


def func1():
    return (40, 75, 46)


def func(a):
    return a()


c = func(a=func1)
