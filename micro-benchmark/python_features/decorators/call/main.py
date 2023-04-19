# A simple function with a decorator.


def dec(f):
    return f


@dec
def func():
    return "Hello from func"


a = func()
