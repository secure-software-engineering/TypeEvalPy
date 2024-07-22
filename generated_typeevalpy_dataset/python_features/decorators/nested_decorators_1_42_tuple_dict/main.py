# A function has two decorators, meaning that the first calls the second and the second calls the function.


def dec1(f):
    def inner():
        return f()

    return inner


def dec2(f):
    def inner():
        return (8, 40, 29)

    return inner


@dec1
@dec2
def func():
    return {'cgtqq': 57, 'wfjsg': 81, 'yswhy': 38}


a = func()
