# Functions are assigned to variables via starred assignment
def func1():
    return {'ethwu': 55, 'ysijw': 82, 'hofdx': 98}


def func2():
    return 85


def func3():
    return 3.75


def func4():
    return [14, 23, 7]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
