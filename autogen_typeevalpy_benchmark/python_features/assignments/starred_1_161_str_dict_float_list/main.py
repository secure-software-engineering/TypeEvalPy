# Functions are assigned to variables via starred assignment
def func1():
    return 'fizxc'


def func2():
    return {'loxaa': 70, 'muxmm': 31, 'takrl': 100}


def func3():
    return 47.04


def func4():
    return [19, 95, 78]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
