# Functions are assigned to variables via starred assignment
def func1():
    return 45.33


def func2():
    return {'fcsxi': 95, 'hffje': 78, 'lzezo': 58}


def func3():
    return 91


def func4():
    return 'drrjw'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
