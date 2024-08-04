# Functions are assigned to variables via starred assignment
def func1():
    return 20.38


def func2():
    return (7, 9, 42)


def func3():
    return {'fevhl': 59, 'nrcbz': 53, 'tjori': 95}


def func4():
    return [91, 56, 31]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
