# A simple function with a decorator.


def dec(f):
    def wrapper():
        return 'ejmfk'

    return wrapper


@dec
def func():
    pass


a = func()
