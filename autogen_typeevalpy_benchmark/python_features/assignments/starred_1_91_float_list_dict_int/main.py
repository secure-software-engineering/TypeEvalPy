# Functions are assigned to variables via starred assignment
def func1():
    return 86.15


def func2():
    return [86, 100, 10]


def func3():
    return {'afjqe': 23, 'pzayg': 100, 'jjpyl': 22}


def func4():
    return 73

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
