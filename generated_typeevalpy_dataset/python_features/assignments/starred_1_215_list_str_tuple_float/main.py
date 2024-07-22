# Functions are assigned to variables via starred assignment
def func1():
    return [7, 89, 30]


def func2():
    return 'smysa'


def func3():
    return (23, 69, 37)


def func4():
    return 31.36

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
