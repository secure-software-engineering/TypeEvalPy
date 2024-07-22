# Functions are assigned to variables via starred assignment
def func1():
    return [13, 16, 60]


def func2():
    return 66.57


def func3():
    return 42


def func4():
    return 'ecbbe'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
