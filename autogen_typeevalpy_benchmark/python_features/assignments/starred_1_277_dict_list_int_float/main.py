# Functions are assigned to variables via starred assignment
def func1():
    return {'vmedi': 22, 'ekcxw': 40, 'gitnt': 51}


def func2():
    return [24, 28, 92]


def func3():
    return 56


def func4():
    return 97.72

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
