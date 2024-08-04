# Functions are assigned to variables via starred assignment
def func1():
    return {'wbtjk': 40, 'impwc': 98, 'elpoa': 43}


def func2():
    return 47.31


def func3():
    return 'zlgtr'


def func4():
    return 12

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
