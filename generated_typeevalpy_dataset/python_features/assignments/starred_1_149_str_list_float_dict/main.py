# Functions are assigned to variables via starred assignment
def func1():
    return 'uahva'


def func2():
    return [95, 36, 77]


def func3():
    return 14.89


def func4():
    return {'rakat': 12, 'kuxxc': 37, 'frpei': 28}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
