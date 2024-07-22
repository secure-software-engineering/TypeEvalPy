# Functions are assigned to variables via starred assignment
def func1():
    return (82, 28, 94)


def func2():
    return 'dbjzc'


def func3():
    return [46, 89, 54]


def func4():
    return 10

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
