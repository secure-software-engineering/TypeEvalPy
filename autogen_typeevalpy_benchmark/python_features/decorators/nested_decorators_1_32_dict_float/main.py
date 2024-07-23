# A function has two decorators, meaning that the first calls the second and the second calls the function.


def dec1(f):
    def inner():
        return f()

    return inner


def dec2(f):
    def inner():
        return {'mkxjl': 9, 'ztbhs': 54, 'ijcdu': 87}

    return inner


@dec1
@dec2
def func():
    return 40.07


a = func()
