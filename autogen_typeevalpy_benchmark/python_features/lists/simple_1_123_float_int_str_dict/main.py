# Functions are assigned as elements of a list and then called.


def func1():
    return 98.3


def func2():
    return 64


def func3():
    return 'aucxf'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ikiul': 2, 'xjxdi': 41, 'nskvs': 18}


b = ["Hello"]
b[0] = func4

f = b[0]()
