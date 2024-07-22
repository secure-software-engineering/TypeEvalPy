# Functions are assigned to variables via starred assignment
def func1():
    return [72, 100, 30]


def func2():
    return (86, 89, 47)


def func3():
    return 65


def func4():
    return 'dndci'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
