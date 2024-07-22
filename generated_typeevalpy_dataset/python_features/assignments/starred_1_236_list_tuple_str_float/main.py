# Functions are assigned to variables via starred assignment
def func1():
    return [16, 26, 33]


def func2():
    return (28, 30, 81)


def func3():
    return 'ghvmt'


def func4():
    return 87.14

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
