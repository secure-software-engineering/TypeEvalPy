# Functions are assigned as elements of a list and then called.


def func1():
    return (100, 29, 89)


def func2():
    return {'hgans': 28, 'eixdy': 16, 'roidy': 9}


def func3():
    return 31.8


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 24


b = ["Hello"]
b[0] = func4

f = b[0]()
