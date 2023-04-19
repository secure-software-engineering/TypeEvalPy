# A function defined inside another function's context serves as a decorator.


def dec(f):
    return f


def func():
    def dec(f):
        return f

    @dec
    def inner():
        return "Hello from inner"


a = func()
