# Functions are assigned to variables via starred assignment
def func1():
    return 'bmuee'


def func2():
    return (19, 78, 32)


def func3():
    return {'biohb': 77, 'gzgvd': 27, 'obbyg': 96}


def func4():
    return 72.8

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
