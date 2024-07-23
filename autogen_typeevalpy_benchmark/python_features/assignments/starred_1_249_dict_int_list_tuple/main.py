# Functions are assigned to variables via starred assignment
def func1():
    return {'tpdod': 51, 'qqwps': 16, 'ojegf': 64}


def func2():
    return 32


def func3():
    return [44, 80, 26]


def func4():
    return (29, 40, 64)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
