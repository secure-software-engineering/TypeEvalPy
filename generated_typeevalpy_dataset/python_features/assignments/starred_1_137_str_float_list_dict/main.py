# Functions are assigned to variables via starred assignment
def func1():
    return 'idxaz'


def func2():
    return 29.46


def func3():
    return [64, 37, 12]


def func4():
    return {'sgvwo': 36, 'dlgnc': 4, 'sqaie': 36}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
