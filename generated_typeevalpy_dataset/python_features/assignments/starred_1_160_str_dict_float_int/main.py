# Functions are assigned to variables via starred assignment
def func1():
    return 'keywn'


def func2():
    return {'seedb': 31, 'mnunh': 94, 'vbwgi': 48}


def func3():
    return 69.37


def func4():
    return 46

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
