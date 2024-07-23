# Functions are assigned to variables via starred assignment
def func1():
    return 'kiggp'


def func2():
    return [89, 40, 31]


def func3():
    return 67.94


def func4():
    return (48, 34, 96)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
