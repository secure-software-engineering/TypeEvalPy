# Functions are assigned to variables via starred assignment
def func1():
    return {'sjssd': 95, 'uobno': 8, 'zqqgx': 90}


def func2():
    return 85.23


def func3():
    return 40


def func4():
    return 'mkytr'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
