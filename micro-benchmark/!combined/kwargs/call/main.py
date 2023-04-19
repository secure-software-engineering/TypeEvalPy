# Call a function with keyword arguments.


def func4():
    pass


def func2():
    pass


def func3():
    return "Hello from func3"


def func(a, b, c):
    a()
    b()
    return c()


c = func(func2, c=func4, b=func3)
