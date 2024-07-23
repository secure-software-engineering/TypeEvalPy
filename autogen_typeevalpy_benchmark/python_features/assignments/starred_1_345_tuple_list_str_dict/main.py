# Functions are assigned to variables via starred assignment
def func1():
    return (52, 7, 3)


def func2():
    return [28, 100, 69]


def func3():
    return 'nowbw'


def func4():
    return {'jknwu': 30, 'qlcqr': 88, 'uarfy': 25}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
