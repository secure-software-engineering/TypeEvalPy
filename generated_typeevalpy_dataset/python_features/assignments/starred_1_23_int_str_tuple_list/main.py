# Functions are assigned to variables via starred assignment
def func1():
    return 68


def func2():
    return 'jidrc'


def func3():
    return (91, 39, 4)


def func4():
    return [2, 82, 25]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
