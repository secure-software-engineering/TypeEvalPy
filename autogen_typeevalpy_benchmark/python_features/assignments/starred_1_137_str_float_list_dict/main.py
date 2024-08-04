# Functions are assigned to variables via starred assignment
def func1():
    return 'zcrsh'


def func2():
    return 53.13


def func3():
    return [88, 21, 55]


def func4():
    return {'ltvqu': 15, 'qligk': 79, 'ubjqi': 52}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
