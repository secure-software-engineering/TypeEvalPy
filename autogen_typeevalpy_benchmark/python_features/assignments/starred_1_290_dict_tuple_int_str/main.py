# Functions are assigned to variables via starred assignment
def func1():
    return {'inxzv': 59, 'zlaeg': 12, 'rveqo': 94}


def func2():
    return (97, 22, 27)


def func3():
    return 96


def func4():
    return 'eawyn'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
