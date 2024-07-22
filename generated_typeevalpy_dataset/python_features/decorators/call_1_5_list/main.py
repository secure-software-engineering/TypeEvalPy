# A simple function with a decorator.


def dec(f):
    def wrapper():
        return [24, 43, 54]

    return wrapper


@dec
def func():
    pass


a = func()
