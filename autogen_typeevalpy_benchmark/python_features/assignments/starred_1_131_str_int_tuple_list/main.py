# Functions are assigned to variables via starred assignment
def func1():
    return 'aefxq'


def func2():
    return 28


def func3():
    return (90, 63, 86)


def func4():
    return [72, 2, 75]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
