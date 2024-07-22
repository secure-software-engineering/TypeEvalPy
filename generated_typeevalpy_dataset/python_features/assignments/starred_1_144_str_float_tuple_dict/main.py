# Functions are assigned to variables via starred assignment
def func1():
    return 'ljdsr'


def func2():
    return 12.17


def func3():
    return (31, 72, 29)


def func4():
    return {'pxnye': 59, 'frazl': 4, 'sqlbi': 80}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
