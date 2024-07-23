# Functions are assigned to variables via starred assignment
def func1():
    return 43.24


def func2():
    return (10, 65, 84)


def func3():
    return {'atsat': 49, 'dftrx': 92, 'wxyyt': 60}


def func4():
    return [10, 19, 46]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
