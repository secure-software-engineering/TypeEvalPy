# Functions are assigned to variables via starred assignment
def func1():
    return [31, 8, 51]


def func2():
    return 80.7


def func3():
    return 'ruwiv'


def func4():
    return (11, 93, 84)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
