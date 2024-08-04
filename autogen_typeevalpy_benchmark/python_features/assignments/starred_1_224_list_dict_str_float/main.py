# Functions are assigned to variables via starred assignment
def func1():
    return [40, 58, 5]


def func2():
    return {'nkohb': 98, 'zkcrn': 50, 'nbfgu': 35}


def func3():
    return 'idtlr'


def func4():
    return 47.77

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
