# Functions are assigned to variables via starred assignment
def func1():
    return (64, 61, 68)


def func2():
    return {'jmhxi': 21, 'slocb': 81, 'heixx': 80}


def func3():
    return 57


def func4():
    return [1, 30, 17]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
