# Functions are assigned to variables via starred assignment
def func1():
    return (27, 97, 23)


def func2():
    return 50.61


def func3():
    return 40


def func4():
    return [28, 97, 53]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
