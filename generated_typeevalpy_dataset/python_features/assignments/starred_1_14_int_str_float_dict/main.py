# Functions are assigned to variables via starred assignment
def func1():
    return 51


def func2():
    return 'uekex'


def func3():
    return 75.69


def func4():
    return {'ljrbp': 85, 'yqmkj': 95, 'sonus': 100}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
