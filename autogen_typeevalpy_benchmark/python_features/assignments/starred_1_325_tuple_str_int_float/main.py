# Functions are assigned to variables via starred assignment
def func1():
    return (2, 89, 54)


def func2():
    return 'emoso'


def func3():
    return 91


def func4():
    return 13.29

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
