# Returning a lambda function from another function.


def func():
    return lambda x: x**2


f = func()
a = f(100)
b = f(43.52)
