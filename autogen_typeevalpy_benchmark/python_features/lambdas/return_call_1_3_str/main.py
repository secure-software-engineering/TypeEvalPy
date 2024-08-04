# A lambda is returned from a function and then called.


def func():
    return lambda x: x + 'hgeco'


y = func()
a = y('hgeco')
