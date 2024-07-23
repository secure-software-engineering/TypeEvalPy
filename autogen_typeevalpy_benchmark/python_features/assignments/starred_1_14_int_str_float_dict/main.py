# Functions are assigned to variables via starred assignment
def func1():
    return 48


def func2():
    return 'qjlei'


def func3():
    return 71.89


def func4():
    return {'ivaex': 76, 'vyelh': 31, 'rlcyw': 5}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
