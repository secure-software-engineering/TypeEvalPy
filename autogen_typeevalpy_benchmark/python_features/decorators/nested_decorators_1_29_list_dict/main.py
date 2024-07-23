# A function has two decorators, meaning that the first calls the second and the second calls the function.


def dec1(f):
    def inner():
        return f()

    return inner


def dec2(f):
    def inner():
        return [65, 35, 54]

    return inner


@dec1
@dec2
def func():
    return {'qclih': 99, 'hixqc': 75, 'ssrbd': 87}


a = func()
