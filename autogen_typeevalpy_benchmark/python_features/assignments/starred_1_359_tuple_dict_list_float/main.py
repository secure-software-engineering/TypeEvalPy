# Functions are assigned to variables via starred assignment
def func1():
    return (71, 53, 91)


def func2():
    return {'nyboq': 1, 'bvdnf': 13, 'fdosr': 29}


def func3():
    return [66, 41, 41]


def func4():
    return 75.17

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
