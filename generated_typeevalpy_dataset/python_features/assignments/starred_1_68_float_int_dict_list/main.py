# Functions are assigned to variables via starred assignment
def func1():
    return 81.31


def func2():
    return 63


def func3():
    return {'tgzqp': 97, 'zeyox': 11, 'bnxip': 83}


def func4():
    return [86, 5, 40]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
