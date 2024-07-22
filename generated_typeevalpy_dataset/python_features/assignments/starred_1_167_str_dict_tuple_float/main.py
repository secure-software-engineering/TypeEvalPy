# Functions are assigned to variables via starred assignment
def func1():
    return 'ddeuy'


def func2():
    return {'fdwkh': 14, 'ldmdi': 42, 'feuvs': 34}


def func3():
    return (16, 91, 73)


def func4():
    return 58.05

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
