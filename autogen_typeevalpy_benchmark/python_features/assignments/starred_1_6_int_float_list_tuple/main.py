# Functions are assigned to variables via starred assignment
def func1():
    return 38


def func2():
    return 50.83


def func3():
    return [35, 17, 50]


def func4():
    return (33, 99, 70)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
