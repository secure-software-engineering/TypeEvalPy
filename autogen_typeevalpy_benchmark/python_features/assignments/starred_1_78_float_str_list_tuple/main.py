# Functions are assigned to variables via starred assignment
def func1():
    return 83.61


def func2():
    return 'wmpre'


def func3():
    return [49, 33, 87]


def func4():
    return (23, 9, 47)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
