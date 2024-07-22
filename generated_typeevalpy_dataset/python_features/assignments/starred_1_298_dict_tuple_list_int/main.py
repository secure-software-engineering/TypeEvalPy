# Functions are assigned to variables via starred assignment
def func1():
    return {'kbbvn': 12, 'gweut': 4, 'dpnax': 46}


def func2():
    return (4, 86, 13)


def func3():
    return [61, 34, 49]


def func4():
    return 15

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
