# A function has two decorators, meaning that the first calls the second and the second calls the function.


def dec1(f):
    def inner():
        return f()

    return inner


def dec2(f):
    def inner():
        return [60, 49, 47]

    return inner


@dec1
@dec2
def func():
    return {'qduuu': 8, 'enhpo': 99, 'xvrtw': 1}


a = func()
