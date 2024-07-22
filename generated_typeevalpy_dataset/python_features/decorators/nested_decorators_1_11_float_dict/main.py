# A function has two decorators, meaning that the first calls the second and the second calls the function.


def dec1(f):
    def inner():
        return f()

    return inner


def dec2(f):
    def inner():
        return 82.22

    return inner


@dec1
@dec2
def func():
    return {'ubgmz': 9, 'ytbir': 86, 'jczca': 28}


a = func()
