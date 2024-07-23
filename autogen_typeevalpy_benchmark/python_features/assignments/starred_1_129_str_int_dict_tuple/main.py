# Functions are assigned to variables via starred assignment
def func1():
    return 'oyfot'


def func2():
    return 52


def func3():
    return {'hknyr': 27, 'gjphk': 18, 'fyydh': 2}


def func4():
    return (4, 69, 37)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
