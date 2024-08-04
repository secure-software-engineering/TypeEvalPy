# Functions are assigned to variables via starred assignment
def func1():
    return 48.41


def func2():
    return 32


def func3():
    return [95, 49, 77]


def func4():
    return {'atphm': 56, 'mbadg': 31, 'suzxl': 35}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
