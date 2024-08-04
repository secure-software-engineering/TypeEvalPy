# Functions are assigned to variables via starred assignment
def func1():
    return [53, 72, 71]


def func2():
    return {'rfbbg': 11, 'hfbcy': 90, 'zocaz': 91}


def func3():
    return 'gidwr'


def func4():
    return 40

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
