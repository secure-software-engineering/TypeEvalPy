# A function has two decorators, meaning that the first calls the second and the second calls the function.


def dec1(f):
    def inner():
        return f()

    return inner


def dec2(f):
    def inner():
        return 'xtdym'

    return inner


@dec1
@dec2
def func():
    return {'eccex': 85, 'aodmv': 51, 'yzogk': 67}


a = func()
