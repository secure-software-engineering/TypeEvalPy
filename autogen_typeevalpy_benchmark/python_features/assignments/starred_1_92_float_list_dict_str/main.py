# Functions are assigned to variables via starred assignment
def func1():
    return 87.0


def func2():
    return [16, 52, 18]


def func3():
    return {'gdbrf': 38, 'ikcdf': 94, 'vvieq': 86}


def func4():
    return 'eilab'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
