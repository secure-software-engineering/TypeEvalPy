# Functions are assigned to variables via starred assignment
def func1():
    return 'vtzir'


def func2():
    return (37, 8, 73)


def func3():
    return 92.77


def func4():
    return 40

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
