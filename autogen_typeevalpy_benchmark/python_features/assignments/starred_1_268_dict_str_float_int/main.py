# Functions are assigned to variables via starred assignment
def func1():
    return {'sbrka': 3, 'etgos': 24, 'zvyly': 88}


def func2():
    return 'eblyr'


def func3():
    return 40.64


def func4():
    return 59

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
