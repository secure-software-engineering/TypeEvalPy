# Functions are assigned to variables via starred assignment
def func1():
    return 41


def func2():
    return 35.87


def func3():
    return (7, 26, 6)


def func4():
    return [80, 82, 2]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
