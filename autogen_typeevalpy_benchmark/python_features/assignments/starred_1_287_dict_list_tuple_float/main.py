# Functions are assigned to variables via starred assignment
def func1():
    return {'lmiat': 51, 'ojfor': 11, 'abrwi': 82}


def func2():
    return [74, 10, 28]


def func3():
    return (70, 41, 10)


def func4():
    return 24.05

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
