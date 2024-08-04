# Functions are assigned to variables via starred assignment
def func1():
    return [35, 7, 59]


def func2():
    return {'safzl': 79, 'gqpzl': 37, 'pfpsk': 12}


def func3():
    return 'eqzbv'


def func4():
    return (3, 29, 22)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
