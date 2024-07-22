# Functions are assigned to variables via starred assignment
def func1():
    return [20, 10, 92]


def func2():
    return 96.63


def func3():
    return 'nsmxu'


def func4():
    return (70, 43, 54)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
