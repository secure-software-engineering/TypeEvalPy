# A simple function with a decorator.


def dec(f):
    def wrapper():
        return [36, 89, 7]

    return wrapper


@dec
def func():
    pass


a = func()
