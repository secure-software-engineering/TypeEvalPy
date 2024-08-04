# A lambda is returned from a function and then called.


def func():
    return lambda x: x + 43


y = func()
a = y(43)
