# A lambda is returned from a function and then called.


def func():
    return lambda x: x + 20.93


y = func()
a = y(20.93)
