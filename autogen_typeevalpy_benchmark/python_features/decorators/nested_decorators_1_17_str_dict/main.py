# A function has two decorators, meaning that the first calls the second and the second calls the function.


def dec1(f):
    def inner():
        return f()

    return inner


def dec2(f):
    def inner():
        return 'kyxhc'

    return inner


@dec1
@dec2
def func():
    return {'wfjjd': 75, 'rkrkm': 98, 'piwij': 14}


a = func()
