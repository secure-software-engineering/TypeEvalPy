# Functions are assigned to variables via starred assignment
def func1():
    return [4, 38, 48]


def func2():
    return {'slsvy': 78, 'qqmck': 6, 'zpvld': 44}


def func3():
    return 44.8


def func4():
    return 41

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
