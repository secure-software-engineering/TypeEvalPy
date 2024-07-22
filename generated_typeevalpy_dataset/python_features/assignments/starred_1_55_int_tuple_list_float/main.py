# Functions are assigned to variables via starred assignment
def func1():
    return 66


def func2():
    return (23, 49, 94)


def func3():
    return [91, 67, 97]


def func4():
    return 48.94

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
