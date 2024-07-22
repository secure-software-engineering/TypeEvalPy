# Functions are assigned to variables via starred assignment
def func1():
    return (36, 15, 22)


def func2():
    return 31.03


def func3():
    return 'cvhvb'


def func4():
    return 35

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
