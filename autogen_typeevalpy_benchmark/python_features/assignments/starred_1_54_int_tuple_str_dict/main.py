# Functions are assigned to variables via starred assignment
def func1():
    return 51


def func2():
    return (96, 18, 82)


def func3():
    return 'jcvre'


def func4():
    return {'chxfm': 1, 'yefaj': 50, 'nspte': 81}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
