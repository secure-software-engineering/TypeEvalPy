# A lambda is returned from a function and then called.


def func():
    return lambda x: x + <value1>


y = func()
a = y(<value1>)
