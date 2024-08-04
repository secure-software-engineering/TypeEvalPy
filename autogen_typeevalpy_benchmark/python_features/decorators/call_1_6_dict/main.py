# A simple function with a decorator.


def dec(f):
    def wrapper():
        return {'xrcrb': 12, 'pvvrq': 23, 'upwzo': 86}

    return wrapper


@dec
def func():
    pass


a = func()
