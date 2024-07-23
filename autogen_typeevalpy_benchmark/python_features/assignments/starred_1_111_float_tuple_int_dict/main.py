# Functions are assigned to variables via starred assignment
def func1():
    return 63.98


def func2():
    return (25, 44, 2)


def func3():
    return 11


def func4():
    return {'yutqo': 79, 'qfxrn': 83, 'japnf': 27}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
