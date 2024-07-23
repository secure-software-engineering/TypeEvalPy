# Functions are assigned as elements of a list and then called.


def func1():
    return 'izwfx'


def func2():
    return (1, 64, 58)


def func3():
    return 24


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'kplyj': 81, 'ofnka': 14, 'eipao': 60}


b = ["Hello"]
b[0] = func4

f = b[0]()
