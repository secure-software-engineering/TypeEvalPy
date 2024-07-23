# A simple function with a decorator.


def dec(f):
    def wrapper():
        return {'msmzw': 81, 'diraj': 28, 'txrla': 33}

    return wrapper


@dec
def func():
    pass


a = func()
