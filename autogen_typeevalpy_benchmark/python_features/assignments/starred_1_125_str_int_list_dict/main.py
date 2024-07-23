# Functions are assigned to variables via starred assignment
def func1():
    return 'iwajt'


def func2():
    return 61


def func3():
    return [80, 91, 11]


def func4():
    return {'vwfhg': 41, 'uwher': 97, 'ronbr': 64}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
