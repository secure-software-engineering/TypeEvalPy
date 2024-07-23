# Functions are assigned to variables via starred assignment
def func1():
    return 'oszdt'


def func2():
    return 96.28


def func3():
    return 38


def func4():
    return {'kbugf': 98, 'yvvde': 36, 'fcqxu': 92}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
