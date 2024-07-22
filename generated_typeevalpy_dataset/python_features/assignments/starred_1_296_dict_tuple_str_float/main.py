# Functions are assigned to variables via starred assignment
def func1():
    return {'ltwgy': 100, 'mxrvr': 30, 'etwfz': 41}


def func2():
    return (57, 27, 88)


def func3():
    return 'qsqrr'


def func4():
    return 80.37

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
