# Functions are assigned to variables via starred assignment
def func1():
    return 'pomsm'


def func2():
    return [57, 18, 75]


def func3():
    return 21


def func4():
    return {'fdjav': 70, 'gfdxq': 17, 'mezht': 40}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
