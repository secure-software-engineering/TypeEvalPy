# A lambda is returned from a function and then called.


def func():
    return lambda x: x + 'xmrqd'


y = func()
a = y('xmrqd')
