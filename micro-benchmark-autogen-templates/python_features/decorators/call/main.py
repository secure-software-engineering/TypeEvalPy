# A simple function with a decorator.


def dec(f):
    def wrapper():
        return "Hello from dec"

    return wrapper


@dec
def func():
    pass


a = func()
