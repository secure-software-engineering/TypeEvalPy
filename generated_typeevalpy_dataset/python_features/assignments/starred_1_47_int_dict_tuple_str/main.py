# Functions are assigned to variables via starred assignment
def func1():
    return 56


def func2():
    return {'ijubs': 54, 'kuhnk': 45, 'mxiwa': 82}


def func3():
    return (33, 6, 100)


def func4():
    return 'qzvtq'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
