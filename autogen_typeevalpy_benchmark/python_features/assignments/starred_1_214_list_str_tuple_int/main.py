# Functions are assigned to variables via starred assignment
def func1():
    return [56, 25, 74]


def func2():
    return 'avzyu'


def func3():
    return (51, 25, 35)


def func4():
    return 74

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
