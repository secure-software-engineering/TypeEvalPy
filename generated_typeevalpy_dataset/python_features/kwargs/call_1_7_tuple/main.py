# Call a function with keyword arguments.


def func1():
    return (61, 25, 47)


def func(a):
    return a()


c = func(a=func1)
