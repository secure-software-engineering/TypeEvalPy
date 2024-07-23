# Functions are assigned to variables via starred assignment
def func1():
    return [41, 35, 92]


def func2():
    return (4, 7, 15)


def func3():
    return 26.51


def func4():
    return 23

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
