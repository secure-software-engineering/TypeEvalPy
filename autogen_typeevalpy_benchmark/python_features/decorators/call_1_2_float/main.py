# A simple function with a decorator.


def dec(f):
    def wrapper():
        return 45.8

    return wrapper


@dec
def func():
    pass


a = func()
