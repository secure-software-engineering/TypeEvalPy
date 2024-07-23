# Functions are assigned to variables via starred assignment
def func1():
    return (76, 28, 60)


def func2():
    return 55.73


def func3():
    return 15


def func4():
    return [83, 21, 71]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
