# Functions are assigned to variables via starred assignment
def func1():
    return {'bjxvs': 74, 'hqjnh': 4, 'ogqro': 82}


def func2():
    return [95, 27, 70]


def func3():
    return 40


def func4():
    return 'plkuw'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
