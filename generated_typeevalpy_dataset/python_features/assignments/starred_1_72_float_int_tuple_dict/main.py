# Functions are assigned to variables via starred assignment
def func1():
    return 80.21


def func2():
    return 50


def func3():
    return (68, 54, 72)


def func4():
    return {'inrja': 10, 'feqsn': 64, 'tlttg': 60}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
