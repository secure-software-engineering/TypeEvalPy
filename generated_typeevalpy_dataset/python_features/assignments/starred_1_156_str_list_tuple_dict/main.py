# Functions are assigned to variables via starred assignment
def func1():
    return 'nsvmb'


def func2():
    return [45, 3, 18]


def func3():
    return (48, 6, 13)


def func4():
    return {'addzc': 8, 'llxia': 51, 'sphix': 54}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
