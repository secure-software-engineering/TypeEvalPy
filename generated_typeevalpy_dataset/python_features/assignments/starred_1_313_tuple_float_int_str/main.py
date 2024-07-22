# Functions are assigned to variables via starred assignment
def func1():
    return (36, 37, 87)


def func2():
    return 46.18


def func3():
    return 31


def func4():
    return 'pplan'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
