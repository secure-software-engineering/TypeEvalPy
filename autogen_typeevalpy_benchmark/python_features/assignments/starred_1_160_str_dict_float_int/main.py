# Functions are assigned to variables via starred assignment
def func1():
    return 'kbjrm'


def func2():
    return {'sfyxo': 52, 'szqmn': 64, 'fwqwi': 36}


def func3():
    return 81.74


def func4():
    return 97

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
