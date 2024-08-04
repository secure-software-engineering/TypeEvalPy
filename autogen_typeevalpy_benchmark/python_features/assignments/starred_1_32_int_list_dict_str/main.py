# Functions are assigned to variables via starred assignment
def func1():
    return 99


def func2():
    return [54, 51, 22]


def func3():
    return {'nqnvd': 59, 'dqnjz': 1, 'thlsg': 45}


def func4():
    return 'xfzwc'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
