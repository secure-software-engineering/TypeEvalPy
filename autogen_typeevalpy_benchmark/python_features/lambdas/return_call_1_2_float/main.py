# A lambda is returned from a function and then called.


def func():
    return lambda x: x + 86.9


y = func()
a = y(86.9)
