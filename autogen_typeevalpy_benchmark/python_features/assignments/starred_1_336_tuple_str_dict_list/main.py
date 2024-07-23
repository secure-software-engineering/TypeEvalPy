# Functions are assigned to variables via starred assignment
def func1():
    return (93, 61, 16)


def func2():
    return 'nxwjt'


def func3():
    return {'feqrq': 37, 'ardsn': 25, 'rlruk': 88}


def func4():
    return [63, 2, 70]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
