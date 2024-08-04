# Functions are assigned to variables via starred assignment
def func1():
    return [31, 30, 45]


def func2():
    return 5.44


def func3():
    return (10, 52, 7)


def func4():
    return 17

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
