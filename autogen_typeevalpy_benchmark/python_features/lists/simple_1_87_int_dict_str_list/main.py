# Functions are assigned as elements of a list and then called.


def func1():
    return 14


def func2():
    return {'oiqek': 9, 'hibmv': 7, 'zlfwr': 55}


def func3():
    return 'jkiuv'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [63, 11, 24]


b = ["Hello"]
b[0] = func4

f = b[0]()
