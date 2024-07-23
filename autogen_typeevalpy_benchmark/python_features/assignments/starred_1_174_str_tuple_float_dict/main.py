# Functions are assigned to variables via starred assignment
def func1():
    return 'likbo'


def func2():
    return (1, 7, 93)


def func3():
    return 84.75


def func4():
    return {'yvtyb': 91, 'bqrwi': 65, 'asvby': 36}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
