# Functions are assigned to variables via starred assignment
def func1():
    return [54, 91, 27]


def func2():
    return 23


def func3():
    return (89, 70, 35)


def func4():
    return 45.92

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
