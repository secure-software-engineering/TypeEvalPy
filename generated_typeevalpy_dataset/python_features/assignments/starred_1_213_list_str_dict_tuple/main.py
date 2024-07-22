# Functions are assigned to variables via starred assignment
def func1():
    return [30, 87, 5]


def func2():
    return 'dktoi'


def func3():
    return {'nvczr': 58, 'zgtco': 58, 'riaqm': 61}


def func4():
    return (59, 47, 32)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
