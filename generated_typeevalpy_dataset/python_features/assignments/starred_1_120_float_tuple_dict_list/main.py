# Functions are assigned to variables via starred assignment
def func1():
    return 59.42


def func2():
    return (31, 46, 46)


def func3():
    return {'eocau': 93, 'fijlf': 6, 'haczd': 10}


def func4():
    return [42, 21, 25]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
