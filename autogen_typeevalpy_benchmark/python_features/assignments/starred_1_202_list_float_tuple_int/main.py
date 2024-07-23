# Functions are assigned to variables via starred assignment
def func1():
    return [97, 74, 9]


def func2():
    return 36.65


def func3():
    return (87, 77, 91)


def func4():
    return 36

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
