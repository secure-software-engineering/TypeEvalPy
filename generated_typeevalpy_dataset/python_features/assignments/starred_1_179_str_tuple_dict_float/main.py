# Functions are assigned to variables via starred assignment
def func1():
    return 'qtrap'


def func2():
    return (50, 39, 20)


def func3():
    return {'txlsh': 19, 'uteuu': 98, 'xbfkp': 58}


def func4():
    return 86.51

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
