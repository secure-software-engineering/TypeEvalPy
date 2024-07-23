# Functions are assigned to variables via starred assignment
def func1():
    return 82


def func2():
    return (8, 39, 89)


def func3():
    return {'bcttl': 32, 'arctb': 64, 'tarde': 21}


def func4():
    return 75.61

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
