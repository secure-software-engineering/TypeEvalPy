# Functions are assigned to variables via starred assignment
def func1():
    return [79, 8, 5]


def func2():
    return 74.31


def func3():
    return (94, 43, 48)


def func4():
    return 'qdgfz'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
