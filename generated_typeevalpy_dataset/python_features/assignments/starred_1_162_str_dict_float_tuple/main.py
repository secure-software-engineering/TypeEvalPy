# Functions are assigned to variables via starred assignment
def func1():
    return 'pombn'


def func2():
    return {'dfeps': 47, 'cfxfg': 79, 'gntyd': 84}


def func3():
    return 10.77


def func4():
    return (67, 88, 45)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
