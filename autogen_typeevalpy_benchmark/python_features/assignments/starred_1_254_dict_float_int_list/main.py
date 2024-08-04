# Functions are assigned to variables via starred assignment
def func1():
    return {'pbcdi': 57, 'einle': 36, 'lonkf': 69}


def func2():
    return 59.17


def func3():
    return 31


def func4():
    return [3, 33, 46]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
