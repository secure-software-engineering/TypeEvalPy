# A function has two decorators, meaning that the first calls the second and the second calls the function.


def dec1(f):
    def inner():
        return f()

    return inner


def dec2(f):
    def inner():
        return {'immup': 84, 'hgutp': 76, 'uajtw': 40}

    return inner


@dec1
@dec2
def func():
    return 4


a = func()
