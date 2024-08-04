# Functions are assigned to variables via starred assignment
def func1():
    return {'tanit': 79, 'vlpbj': 5, 'hsnch': 66}


def func2():
    return [8, 28, 44]


def func3():
    return 50.83


def func4():
    return 22

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
