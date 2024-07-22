# Functions are assigned to variables via starred assignment
def func1():
    return [69, 90, 51]


def func2():
    return {'jsgze': 55, 'vtwwn': 20, 'gxkpt': 52}


def func3():
    return 40.91


def func4():
    return 75

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
