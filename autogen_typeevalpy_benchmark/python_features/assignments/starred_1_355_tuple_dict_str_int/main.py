# Functions are assigned to variables via starred assignment
def func1():
    return (93, 23, 18)


def func2():
    return {'zavws': 71, 'zfsuq': 14, 'xczto': 47}


def func3():
    return 'slyle'


def func4():
    return 28

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
