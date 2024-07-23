# A function has two decorators, meaning that the first calls the second and the second calls the function.


def dec1(f):
    def inner():
        return f()

    return inner


def dec2(f):
    def inner():
        return {'tqifk': 5, 'zhofl': 39, 'sgarq': 54}

    return inner


@dec1
@dec2
def func():
    return (81, 51, 23)


a = func()
