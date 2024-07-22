# Functions are assigned to variables via starred assignment
def func1():
    return [1, 22, 13]


def func2():
    return 95


def func3():
    return 9.7


def func4():
    return {'vtrit': 65, 'bkkah': 67, 'snfkf': 61}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
