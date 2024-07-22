# Functions are assigned to variables via starred assignment
def func1():
    return 'yaxbx'


def func2():
    return {'nkffu': 7, 'wbyva': 82, 'itrfr': 85}


def func3():
    return [31, 65, 66]


def func4():
    return 55.76

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
