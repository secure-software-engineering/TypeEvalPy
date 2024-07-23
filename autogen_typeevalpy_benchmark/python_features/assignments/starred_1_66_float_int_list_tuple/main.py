# Functions are assigned to variables via starred assignment
def func1():
    return 61.59


def func2():
    return 4


def func3():
    return [76, 8, 97]


def func4():
    return (93, 55, 2)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
