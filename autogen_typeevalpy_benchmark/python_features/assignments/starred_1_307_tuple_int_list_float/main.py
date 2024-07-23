# Functions are assigned to variables via starred assignment
def func1():
    return (59, 95, 82)


def func2():
    return 86


def func3():
    return [18, 47, 89]


def func4():
    return 59.06

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
