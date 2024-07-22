# Returning a lambda function from another function.


def func():
    return lambda x: x**2


f = func()
a = f(<value1>)
b = f(<value2>)
