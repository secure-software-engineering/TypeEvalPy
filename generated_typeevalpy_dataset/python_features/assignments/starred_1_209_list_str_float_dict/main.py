# Functions are assigned to variables via starred assignment
def func1():
    return [29, 98, 28]


def func2():
    return 'umpmi'


def func3():
    return 86.25


def func4():
    return {'hdqxv': 77, 'xpoci': 77, 'zejsg': 11}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
