# Functions are assigned to variables via starred assignment
def func1():
    return [84, 74, 30]


def func2():
    return 77.96


def func3():
    return 10


def func4():
    return (81, 72, 67)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
