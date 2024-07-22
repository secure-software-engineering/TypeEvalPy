# Functions are assigned as elements of a list and then called.


def func1():
    return 'ptfcd'


def func2():
    return 72.95


def func3():
    return 69


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'tywin': 32, 'bsgkb': 80, 'odlvh': 90}


b = ["Hello"]
b[0] = func4

f = b[0]()
