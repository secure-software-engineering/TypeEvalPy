# Functions are assigned to variables via starred assignment
def func1():
    return [22, 52, 88]


def func2():
    return 88


def func3():
    return 'ogebw'


def func4():
    return 40.43

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
