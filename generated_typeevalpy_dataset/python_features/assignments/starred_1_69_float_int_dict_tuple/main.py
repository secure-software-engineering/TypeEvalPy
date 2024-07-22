# Functions are assigned to variables via starred assignment
def func1():
    return 57.43


def func2():
    return 71


def func3():
    return {'lrrzi': 35, 'unfhg': 49, 'opldh': 27}


def func4():
    return (54, 38, 30)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
