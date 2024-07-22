# Functions are assigned to variables via starred assignment
def func1():
    return {'hfxes': 38, 'txyuv': 58, 'hxari': 55}


def func2():
    return 4


def func3():
    return 'gcnzk'


def func4():
    return 47.22

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
