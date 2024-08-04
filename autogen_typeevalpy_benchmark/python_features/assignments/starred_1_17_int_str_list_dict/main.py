# Functions are assigned to variables via starred assignment
def func1():
    return 35


def func2():
    return 'ylmwa'


def func3():
    return [100, 26, 1]


def func4():
    return {'dnfxm': 17, 'mjpvf': 67, 'iqvse': 48}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
