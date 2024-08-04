# Functions are assigned to variables via starred assignment
def func1():
    return 'pgubx'


def func2():
    return {'wnlpc': 14, 'ddfub': 75, 'qewuc': 63}


def func3():
    return 83


def func4():
    return [70, 73, 19]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
