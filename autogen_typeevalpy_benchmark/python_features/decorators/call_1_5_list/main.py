# A simple function with a decorator.


def dec(f):
    def wrapper():
        return [22, 41, 90]

    return wrapper


@dec
def func():
    pass


a = func()
