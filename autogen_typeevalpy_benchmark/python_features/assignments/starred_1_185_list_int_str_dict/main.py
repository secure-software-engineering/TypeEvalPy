# Functions are assigned to variables via starred assignment
def func1():
    return [29, 19, 68]


def func2():
    return 38


def func3():
    return 'aobnh'


def func4():
    return {'uvicd': 70, 'lpdkn': 32, 'zspaf': 85}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
