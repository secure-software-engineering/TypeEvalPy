# Functions are assigned to variables via starred assignment
def func1():
    return 'dhcrc'


def func2():
    return [97, 53, 56]


def func3():
    return 78.13


def func4():
    return {'coxyw': 47, 'duqhw': 65, 'vpolt': 61}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
