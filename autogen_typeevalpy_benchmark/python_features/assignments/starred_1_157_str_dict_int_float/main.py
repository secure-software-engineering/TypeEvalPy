# Functions are assigned to variables via starred assignment
def func1():
    return 'gzftz'


def func2():
    return {'rrxrf': 86, 'jqvod': 54, 'vnziy': 31}


def func3():
    return 94


def func4():
    return 47.62

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
