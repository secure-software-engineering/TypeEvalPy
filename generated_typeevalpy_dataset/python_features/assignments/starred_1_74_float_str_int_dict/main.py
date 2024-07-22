# Functions are assigned to variables via starred assignment
def func1():
    return 37.46


def func2():
    return 'pqlih'


def func3():
    return 6


def func4():
    return {'spcvr': 86, 'xlgyo': 18, 'upcnx': 25}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
