# Functions are assigned to variables via starred assignment
def func1():
    return (73, 96, 61)


def func2():
    return {'vdrao': 89, 'kshok': 39, 'imgsp': 61}


def func3():
    return 80


def func4():
    return 'kvvmy'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
