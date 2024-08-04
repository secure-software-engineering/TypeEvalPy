# Functions are assigned to variables via starred assignment
def func1():
    return (45, 1, 6)


def func2():
    return [25, 40, 43]


def func3():
    return 76.71


def func4():
    return 97

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
