# Functions are assigned to variables via starred assignment
def func1():
    return (37, 91, 18)


def func2():
    return {'ederc': 61, 'rbfrb': 94, 'ipulz': 54}


def func3():
    return 'tuzkd'


def func4():
    return 64.59

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
