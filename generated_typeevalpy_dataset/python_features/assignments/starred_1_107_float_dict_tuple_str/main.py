# Functions are assigned to variables via starred assignment
def func1():
    return 27.51


def func2():
    return {'myckq': 38, 'kpzfm': 52, 'vbiek': 26}


def func3():
    return (30, 39, 24)


def func4():
    return 'zktbh'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
