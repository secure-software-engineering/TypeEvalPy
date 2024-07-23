# Functions are assigned to variables via starred assignment
def func1():
    return (28, 72, 3)


def func2():
    return [34, 18, 79]


def func3():
    return 'htdtb'


def func4():
    return 6.46

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
