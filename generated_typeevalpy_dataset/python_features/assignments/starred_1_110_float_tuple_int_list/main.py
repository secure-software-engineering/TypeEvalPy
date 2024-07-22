# Functions are assigned to variables via starred assignment
def func1():
    return 13.1


def func2():
    return (67, 78, 57)


def func3():
    return 91


def func4():
    return [14, 41, 3]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
