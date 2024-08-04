# Functions are assigned to variables via starred assignment
def func1():
    return 14


def func2():
    return 92.3


def func3():
    return (67, 41, 49)


def func4():
    return {'hcvlg': 27, 'cyaxu': 62, 'rkpsq': 90}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
