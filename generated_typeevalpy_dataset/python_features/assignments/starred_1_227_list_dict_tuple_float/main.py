# Functions are assigned to variables via starred assignment
def func1():
    return [96, 18, 16]


def func2():
    return {'mfgup': 53, 'yqpsz': 53, 'mmtfr': 16}


def func3():
    return (76, 53, 68)


def func4():
    return 68.66

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
