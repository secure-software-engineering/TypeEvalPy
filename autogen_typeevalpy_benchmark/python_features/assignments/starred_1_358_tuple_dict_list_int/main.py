# Functions are assigned to variables via starred assignment
def func1():
    return (55, 1, 39)


def func2():
    return {'pbmgh': 94, 'lxdtc': 74, 'cevbt': 88}


def func3():
    return [52, 90, 41]


def func4():
    return 45

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
