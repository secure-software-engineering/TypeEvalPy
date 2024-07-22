# Functions are assigned to variables via starred assignment
def func1():
    return (12, 33, 82)


def func2():
    return [28, 80, 36]


def func3():
    return 83.62


def func4():
    return 47

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
