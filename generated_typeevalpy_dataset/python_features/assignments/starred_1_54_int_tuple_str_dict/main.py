# Functions are assigned to variables via starred assignment
def func1():
    return 60


def func2():
    return (20, 71, 30)


def func3():
    return 'mhpkw'


def func4():
    return {'rhunt': 99, 'pqbwk': 13, 'zjics': 68}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
