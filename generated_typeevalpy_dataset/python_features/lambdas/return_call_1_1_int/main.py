# A lambda is returned from a function and then called.


def func():
    return lambda x: x + 59


y = func()
a = y(59)
