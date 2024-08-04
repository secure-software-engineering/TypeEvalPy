# Functions are assigned to variables via starred assignment
def func1():
    return 'pzith'


def func2():
    return [63, 47, 65]


def func3():
    return {'ckbux': 1, 'ugquk': 39, 'gtrzh': 3}


def func4():
    return 60

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
