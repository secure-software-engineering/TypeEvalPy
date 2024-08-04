# Functions are assigned to variables via starred assignment
def func1():
    return 1.15


def func2():
    return {'hxwdw': 28, 'slntb': 33, 'fidyt': 39}


def func3():
    return 'rfpku'


def func4():
    return (49, 96, 95)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
