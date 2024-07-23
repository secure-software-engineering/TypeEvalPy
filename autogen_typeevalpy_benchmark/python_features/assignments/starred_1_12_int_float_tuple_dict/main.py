# Functions are assigned to variables via starred assignment
def func1():
    return 77


def func2():
    return 74.53


def func3():
    return (40, 55, 83)


def func4():
    return {'lmsib': 53, 'meijn': 95, 'wyksl': 100}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
