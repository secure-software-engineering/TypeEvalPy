# Functions are assigned to variables via starred assignment
def func1():
    return 38.26


def func2():
    return {'lgefv': 30, 'ptzdj': 33, 'ogwoy': 21}


def func3():
    return [22, 20, 94]


def func4():
    return 26

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
