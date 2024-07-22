# Functions are assigned to variables via starred assignment
def func1():
    return (54, 4, 5)


def func2():
    return 6


def func3():
    return [35, 12, 73]


def func4():
    return 4.29

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
