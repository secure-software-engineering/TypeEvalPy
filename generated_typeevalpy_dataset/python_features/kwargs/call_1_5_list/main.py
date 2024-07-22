# Call a function with keyword arguments.


def func1():
    return [54, 9, 18]


def func(a):
    return a()


c = func(a=func1)
