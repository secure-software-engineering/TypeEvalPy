# Functions are assigned to variables via starred assignment
def func1():
    return 6.86


def func2():
    return (1, 76, 82)


def func3():
    return [70, 63, 80]


def func4():
    return 100

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
