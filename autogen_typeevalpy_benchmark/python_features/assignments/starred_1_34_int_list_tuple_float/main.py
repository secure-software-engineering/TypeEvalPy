# Functions are assigned to variables via starred assignment
def func1():
    return 84


def func2():
    return [27, 13, 61]


def func3():
    return (72, 88, 43)


def func4():
    return 46.46

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
