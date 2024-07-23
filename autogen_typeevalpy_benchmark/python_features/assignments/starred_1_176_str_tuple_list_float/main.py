# Functions are assigned to variables via starred assignment
def func1():
    return 'bxwqg'


def func2():
    return (100, 67, 31)


def func3():
    return [78, 25, 17]


def func4():
    return 57.07

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
