# Functions are assigned to variables via starred assignment
def func1():
    return [26, 17, 3]


def func2():
    return 6.08


def func3():
    return 'jbmso'


def func4():
    return 97

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
