# Functions are assigned to variables via starred assignment
def func1():
    return 73


def func2():
    return 'ovkjt'


def func3():
    return 52.61


def func4():
    return {'rebws': 20, 'wizfe': 70, 'jopkl': 48}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
