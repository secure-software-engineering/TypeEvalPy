# Functions are assigned to variables via starred assignment
def func1():
    return {'ojzrh': 16, 'vucpz': 61, 'ogaly': 1}


def func2():
    return 'rurmx'


def func3():
    return (47, 22, 6)


def func4():
    return 48.47

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
