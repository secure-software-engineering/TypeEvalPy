# Functions are assigned to variables via starred assignment
def func1():
    return 74.77


def func2():
    return 'nxfuy'


def func3():
    return [51, 44, 53]


def func4():
    return {'llllw': 70, 'anpkl': 18, 'gihnh': 1}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
