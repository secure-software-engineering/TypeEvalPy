# Functions are assigned to variables via starred assignment
def func1():
    return [32, 86, 74]


def func2():
    return {'kjalu': 85, 'cnvdc': 87, 'pudiy': 77}


def func3():
    return 15.16


def func4():
    return (39, 93, 63)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
