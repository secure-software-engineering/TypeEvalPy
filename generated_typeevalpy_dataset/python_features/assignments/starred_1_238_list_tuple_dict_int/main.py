# Functions are assigned to variables via starred assignment
def func1():
    return [77, 5, 1]


def func2():
    return (20, 70, 7)


def func3():
    return {'jhzdw': 54, 'qfgeo': 32, 'expgl': 70}


def func4():
    return 19

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
