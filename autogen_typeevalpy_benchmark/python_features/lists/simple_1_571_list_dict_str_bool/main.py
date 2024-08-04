# Functions are assigned as elements of a list and then called.


def func1():
    return [42, 28, 49]


def func2():
    return {'vdcqt': 91, 'fordj': 80, 'nkwgv': 16}


def func3():
    return 'mebkb'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
