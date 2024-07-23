# Functions are assigned to variables via starred assignment
def func1():
    return 17.53


def func2():
    return 45


def func3():
    return (54, 21, 71)


def func4():
    return [87, 36, 21]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
