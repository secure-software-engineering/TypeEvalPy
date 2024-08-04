# Functions are assigned to variables via starred assignment
def func1():
    return 47.28


def func2():
    return [41, 40, 82]


def func3():
    return 'dvzrq'


def func4():
    return (66, 23, 50)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
