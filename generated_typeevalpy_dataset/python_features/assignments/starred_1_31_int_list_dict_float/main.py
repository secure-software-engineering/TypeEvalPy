# Functions are assigned to variables via starred assignment
def func1():
    return 90


def func2():
    return [41, 68, 35]


def func3():
    return {'ggkjv': 12, 'mitvq': 40, 'zabvy': 87}


def func4():
    return 34.64

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
