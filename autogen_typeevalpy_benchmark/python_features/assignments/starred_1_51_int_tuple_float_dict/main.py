# Functions are assigned to variables via starred assignment
def func1():
    return 33


def func2():
    return (50, 13, 18)


def func3():
    return 84.74


def func4():
    return {'rvjls': 57, 'welwe': 51, 'lnnnu': 21}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
