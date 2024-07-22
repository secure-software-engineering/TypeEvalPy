# Returning a lambda function from another function.


def func():
    return lambda x: x**2


f = func()
a = f(1.95)
b = f(83)
