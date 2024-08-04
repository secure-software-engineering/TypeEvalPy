# Functions are assigned to variables via starred assignment
def func1():
    return 34.85


def func2():
    return {'efryl': 8, 'arxtw': 95, 'amwoc': 32}


def func3():
    return (40, 75, 97)


def func4():
    return 'rvcpt'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
