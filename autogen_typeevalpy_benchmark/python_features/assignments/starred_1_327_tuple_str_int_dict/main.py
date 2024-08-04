# Functions are assigned to variables via starred assignment
def func1():
    return (61, 90, 90)


def func2():
    return 'zvdin'


def func3():
    return 2


def func4():
    return {'cztzy': 87, 'wqlhl': 16, 'rhtpg': 53}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
