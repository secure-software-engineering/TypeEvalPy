# Functions are assigned to variables via starred assignment
def func1():
    return 'sxtcf'


def func2():
    return 25.3


def func3():
    return 27


def func4():
    return {'bxnls': 35, 'rvmkm': 94, 'ayhuf': 36}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
