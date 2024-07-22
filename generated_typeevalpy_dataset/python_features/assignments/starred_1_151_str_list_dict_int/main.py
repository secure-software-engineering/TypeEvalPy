# Functions are assigned to variables via starred assignment
def func1():
    return 'kburb'


def func2():
    return [2, 29, 57]


def func3():
    return {'cpbay': 7, 'gbxuq': 92, 'frqgm': 55}


def func4():
    return 66

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
