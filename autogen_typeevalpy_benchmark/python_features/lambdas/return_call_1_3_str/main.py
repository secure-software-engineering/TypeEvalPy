# A lambda is returned from a function and then called.


def func():
    return lambda x: x + 'csuqe'


y = func()
a = y('csuqe')
