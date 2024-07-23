# Functions are assigned to variables via starred assignment
def func1():
    return 59


def func2():
    return {'cohms': 12, 'uixdq': 43, 'uppqf': 95}


def func3():
    return [27, 84, 3]


def func4():
    return 'ucckc'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
