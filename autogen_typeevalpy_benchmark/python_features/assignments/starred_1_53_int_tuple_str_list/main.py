# Functions are assigned to variables via starred assignment
def func1():
    return 80


def func2():
    return (77, 44, 10)


def func3():
    return 'lmbis'


def func4():
    return [93, 79, 76]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
