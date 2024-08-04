# Functions are assigned to variables via starred assignment
def func1():
    return [43, 76, 55]


def func2():
    return (58, 36, 30)


def func3():
    return 30


def func4():
    return 24.1

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
