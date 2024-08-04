# Functions are assigned to variables via starred assignment
def func1():
    return (98, 32, 35)


def func2():
    return 34


def func3():
    return {'plybx': 10, 'mkbsl': 49, 'tdsqd': 97}


def func4():
    return 74.89

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
