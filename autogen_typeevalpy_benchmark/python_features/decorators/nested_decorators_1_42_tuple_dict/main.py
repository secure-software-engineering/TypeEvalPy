# A function has two decorators, meaning that the first calls the second and the second calls the function.


def dec1(f):
    def inner():
        return f()

    return inner


def dec2(f):
    def inner():
        return (17, 36, 91)

    return inner


@dec1
@dec2
def func():
    return {'xnbao': 7, 'oiaty': 64, 'vurfa': 95}


a = func()
