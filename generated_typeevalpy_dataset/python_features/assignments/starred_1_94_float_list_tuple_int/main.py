# Functions are assigned to variables via starred assignment
def func1():
    return 8.64


def func2():
    return [74, 72, 81]


def func3():
    return (32, 71, 13)


def func4():
    return 62

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
