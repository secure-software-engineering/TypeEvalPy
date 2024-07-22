# Functions are assigned to variables via starred assignment
def func1():
    return [90, 28, 35]


def func2():
    return {'tmakt': 41, 'msbjm': 21, 'uxwjr': 34}


def func3():
    return (31, 57, 6)


def func4():
    return 40

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
