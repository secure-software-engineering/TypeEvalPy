# Functions are assigned to variables via starred assignment
def func1():
    return {'gzgwl': 80, 'yyyyk': 95, 'wctqg': 43}


def func2():
    return 28


def func3():
    return 29.27


def func4():
    return 'vyhbt'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
