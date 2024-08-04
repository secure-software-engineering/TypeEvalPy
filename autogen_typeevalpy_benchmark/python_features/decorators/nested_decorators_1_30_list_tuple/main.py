# A function has two decorators, meaning that the first calls the second and the second calls the function.


def dec1(f):
    def inner():
        return f()

    return inner


def dec2(f):
    def inner():
        return [45, 16, 82]

    return inner


@dec1
@dec2
def func():
    return (17, 42, 30)


a = func()
