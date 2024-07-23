# A function has two decorators, meaning that the first calls the second and the second calls the function.


def dec1(f):
    def inner():
        return f()

    return inner


def dec2(f):
    def inner():
        return {'mttmu': 63, 'aneqp': 6, 'tusbi': 72}

    return inner


@dec1
@dec2
def func():
    return [89, 96, 65]


a = func()
