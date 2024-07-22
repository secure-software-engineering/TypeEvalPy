# Functions are assigned to variables via starred assignment
def func1():
    return 80


def func2():
    return 8.27


def func3():
    return {'ltwxd': 36, 'hjaxn': 43, 'rgktk': 63}


def func4():
    return [97, 48, 93]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
