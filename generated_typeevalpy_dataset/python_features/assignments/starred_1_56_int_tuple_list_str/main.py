# Functions are assigned to variables via starred assignment
def func1():
    return 7


def func2():
    return (71, 54, 61)


def func3():
    return [10, 18, 99]


def func4():
    return 'gcjei'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
