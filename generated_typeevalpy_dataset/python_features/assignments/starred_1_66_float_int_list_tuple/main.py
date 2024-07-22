# Functions are assigned to variables via starred assignment
def func1():
    return 30.6


def func2():
    return 83


def func3():
    return [55, 51, 9]


def func4():
    return (85, 60, 96)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
