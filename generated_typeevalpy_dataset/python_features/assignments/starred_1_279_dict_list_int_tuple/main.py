# Functions are assigned to variables via starred assignment
def func1():
    return {'mbyte': 50, 'lvvrp': 11, 'kuxdz': 88}


def func2():
    return [7, 18, 19]


def func3():
    return 1


def func4():
    return (41, 96, 93)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
