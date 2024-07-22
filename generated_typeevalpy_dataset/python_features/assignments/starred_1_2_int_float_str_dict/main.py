# Functions are assigned to variables via starred assignment
def func1():
    return 37


def func2():
    return 27.68


def func3():
    return 'fwrbi'


def func4():
    return {'fydcl': 29, 'bsxoi': 41, 'xvudb': 24}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
