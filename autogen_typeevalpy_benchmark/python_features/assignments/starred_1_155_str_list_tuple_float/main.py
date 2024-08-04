# Functions are assigned to variables via starred assignment
def func1():
    return 'mgwus'


def func2():
    return [77, 53, 6]


def func3():
    return (63, 8, 59)


def func4():
    return 13.68

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
