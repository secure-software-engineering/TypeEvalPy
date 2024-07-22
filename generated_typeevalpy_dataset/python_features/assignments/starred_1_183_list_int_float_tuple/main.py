# Functions are assigned to variables via starred assignment
def func1():
    return [88, 61, 72]


def func2():
    return 49


def func3():
    return 31.86


def func4():
    return (20, 73, 47)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
