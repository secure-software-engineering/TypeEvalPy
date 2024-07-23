# Functions are assigned to variables via starred assignment
def func1():
    return 83


def func2():
    return [48, 81, 75]


def func3():
    return {'gkrrd': 92, 'yvidy': 38, 'rqwct': 97}


def func4():
    return 'dqkqb'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
