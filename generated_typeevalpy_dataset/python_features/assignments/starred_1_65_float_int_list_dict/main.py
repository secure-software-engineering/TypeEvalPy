# Functions are assigned to variables via starred assignment
def func1():
    return 25.14


def func2():
    return 54


def func3():
    return [25, 2, 31]


def func4():
    return {'yitte': 75, 'mbang': 1, 'hxbva': 73}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
