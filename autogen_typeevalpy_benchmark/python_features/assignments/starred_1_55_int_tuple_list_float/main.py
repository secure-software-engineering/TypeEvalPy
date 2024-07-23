# Functions are assigned to variables via starred assignment
def func1():
    return 75


def func2():
    return (48, 46, 27)


def func3():
    return [32, 54, 15]


def func4():
    return 80.77

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
