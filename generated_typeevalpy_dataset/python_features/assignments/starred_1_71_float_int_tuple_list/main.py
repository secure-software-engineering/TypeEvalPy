# Functions are assigned to variables via starred assignment
def func1():
    return 12.03


def func2():
    return 30


def func3():
    return (85, 88, 54)


def func4():
    return [31, 16, 100]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
