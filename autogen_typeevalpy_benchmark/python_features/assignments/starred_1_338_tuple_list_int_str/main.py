# Functions are assigned to variables via starred assignment
def func1():
    return (74, 66, 31)


def func2():
    return [35, 65, 35]


def func3():
    return 77


def func4():
    return 'eslso'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
