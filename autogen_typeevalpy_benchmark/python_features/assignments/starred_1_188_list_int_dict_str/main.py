# Functions are assigned to variables via starred assignment
def func1():
    return [75, 44, 65]


def func2():
    return 21


def func3():
    return {'pcnyx': 60, 'xvcvu': 43, 'qcpzx': 59}


def func4():
    return 'hwzzx'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
