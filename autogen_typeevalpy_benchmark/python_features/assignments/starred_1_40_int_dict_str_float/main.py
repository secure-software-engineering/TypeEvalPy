# Functions are assigned to variables via starred assignment
def func1():
    return 45


def func2():
    return {'vhtss': 13, 'hiqpd': 20, 'ejhju': 10}


def func3():
    return 'vdmmc'


def func4():
    return 44.07

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
