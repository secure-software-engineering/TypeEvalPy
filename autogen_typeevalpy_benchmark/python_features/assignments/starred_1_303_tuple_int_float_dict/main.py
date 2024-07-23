# Functions are assigned to variables via starred assignment
def func1():
    return (57, 10, 81)


def func2():
    return 64


def func3():
    return 46.47


def func4():
    return {'jeset': 100, 'fmquj': 41, 'zksbd': 94}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
