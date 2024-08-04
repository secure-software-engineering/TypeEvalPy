# Functions are assigned to variables via starred assignment
def func1():
    return [39, 72, 60]


def func2():
    return 31


def func3():
    return {'pedpn': 56, 'oseqy': 91, 'zxsgy': 60}


def func4():
    return (62, 22, 97)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
