# Functions are assigned to variables via starred assignment
def func1():
    return (88, 6, 7)


def func2():
    return 'caoyd'


def func3():
    return 71.5


def func4():
    return [37, 82, 84]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
