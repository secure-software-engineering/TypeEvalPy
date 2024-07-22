# A lambda is returned from a function and then called.


def func():
    return lambda x: x + 16.82


y = func()
a = y(16.82)
