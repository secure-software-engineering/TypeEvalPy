# Functions are assigned to variables via starred assignment
def func1():
    return 53


def func2():
    return 22.18


def func3():
    return {'ffcxb': 63, 'dqxrw': 37, 'nzusz': 18}


def func4():
    return 'fwmjm'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
