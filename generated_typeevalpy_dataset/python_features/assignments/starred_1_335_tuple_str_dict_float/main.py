# Functions are assigned to variables via starred assignment
def func1():
    return (52, 57, 59)


def func2():
    return 'qafmf'


def func3():
    return {'oaatn': 60, 'kzexm': 34, 'lhvzk': 16}


def func4():
    return 41.81

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
