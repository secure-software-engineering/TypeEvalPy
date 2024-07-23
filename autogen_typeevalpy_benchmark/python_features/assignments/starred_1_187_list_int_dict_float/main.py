# Functions are assigned to variables via starred assignment
def func1():
    return [10, 90, 96]


def func2():
    return 41


def func3():
    return {'ncehu': 82, 'oukyq': 30, 'vletf': 69}


def func4():
    return 9.98

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
