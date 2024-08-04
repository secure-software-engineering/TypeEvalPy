# Functions are assigned to variables via starred assignment
def func1():
    return {'itnle': 22, 'odkds': 54, 'nstyz': 74}


def func2():
    return 'oxgsj'


def func3():
    return [75, 42, 18]


def func4():
    return 95

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
