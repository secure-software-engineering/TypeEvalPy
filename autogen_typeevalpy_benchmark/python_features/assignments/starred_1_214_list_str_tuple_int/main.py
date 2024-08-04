# Functions are assigned to variables via starred assignment
def func1():
    return [7, 81, 84]


def func2():
    return 'lpdsd'


def func3():
    return (68, 45, 55)


def func4():
    return 43

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
