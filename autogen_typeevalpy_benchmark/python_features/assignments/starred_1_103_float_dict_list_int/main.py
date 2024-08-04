# Functions are assigned to variables via starred assignment
def func1():
    return 72.15


def func2():
    return {'gnrdf': 46, 'lkmvx': 60, 'lfdlh': 60}


def func3():
    return [55, 23, 87]


def func4():
    return 53

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
