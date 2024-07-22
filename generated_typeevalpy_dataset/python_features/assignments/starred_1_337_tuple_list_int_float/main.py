# Functions are assigned to variables via starred assignment
def func1():
    return (99, 13, 96)


def func2():
    return [59, 12, 34]


def func3():
    return 47


def func4():
    return 50.71

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
