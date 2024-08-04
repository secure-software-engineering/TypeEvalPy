# Functions are assigned to variables via starred assignment
def func1():
    return [17, 60, 41]


def func2():
    return 84


def func3():
    return 74.23


def func4():
    return (100, 13, 46)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
