# Functions are assigned to variables via starred assignment
def func1():
    return (46, 60, 36)


def func2():
    return [85, 71, 58]


def func3():
    return 71


def func4():
    return 'pcjng'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
