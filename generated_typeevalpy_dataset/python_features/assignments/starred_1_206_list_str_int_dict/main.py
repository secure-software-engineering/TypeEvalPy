# Functions are assigned to variables via starred assignment
def func1():
    return [30, 82, 5]


def func2():
    return 'gfrjl'


def func3():
    return 38


def func4():
    return {'rtskr': 34, 'tzwbd': 26, 'yongf': 88}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
