# Functions are assigned to variables via starred assignment
def func1():
    return 'kbsjq'


def func2():
    return [2, 1, 56]


def func3():
    return (83, 91, 56)


def func4():
    return 38.65

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
