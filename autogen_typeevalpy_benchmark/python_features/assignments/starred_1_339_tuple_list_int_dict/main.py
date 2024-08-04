# Functions are assigned to variables via starred assignment
def func1():
    return (53, 88, 23)


def func2():
    return [79, 53, 45]


def func3():
    return 8


def func4():
    return {'wurgi': 64, 'idmjh': 62, 'unnlp': 74}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
