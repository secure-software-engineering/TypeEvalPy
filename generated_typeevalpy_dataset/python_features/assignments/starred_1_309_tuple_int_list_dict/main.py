# Functions are assigned to variables via starred assignment
def func1():
    return (21, 18, 7)


def func2():
    return 52


def func3():
    return [89, 35, 70]


def func4():
    return {'hzytr': 40, 'qrqot': 31, 'iqzjc': 47}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
