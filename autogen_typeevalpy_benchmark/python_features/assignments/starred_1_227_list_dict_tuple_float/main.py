# Functions are assigned to variables via starred assignment
def func1():
    return [3, 8, 36]


def func2():
    return {'lykpw': 14, 'jqpnh': 4, 'gbaqk': 7}


def func3():
    return (59, 60, 1)


def func4():
    return 75.6

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
