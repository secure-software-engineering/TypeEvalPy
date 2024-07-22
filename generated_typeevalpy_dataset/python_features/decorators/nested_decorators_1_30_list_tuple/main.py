# A function has two decorators, meaning that the first calls the second and the second calls the function.


def dec1(f):
    def inner():
        return f()

    return inner


def dec2(f):
    def inner():
        return [95, 78, 21]

    return inner


@dec1
@dec2
def func():
    return (64, 58, 91)


a = func()
