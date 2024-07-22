# Functions are assigned to variables via starred assignment
def func1():
    return (42, 45, 94)


def func2():
    return 'xrtba'


def func3():
    return 11.82


def func4():
    return 24

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
